#!/usr/bin/env bash
# Keeps rzen-update.json's ios.latestVersion equal to the version live on the App Store.
# Only ever raises the version. Never touches enabled, minimumSupportedVersion or mandatory.
# Test without network: STORE_VERSION=3.0.1 bash scripts/sync-rzen-version.sh
set -uo pipefail
FILE="${FILE:-rzen-update.json}"
APP_ID="${APP_ID:-6786930057}"
valid='^[0-9]+(\.[0-9]+){1,2}$'

store="${STORE_VERSION:-}"
if [ -z "$store" ]; then
  body=$(curl -fsS -m 20 --retry 2 "https://itunes.apple.com/lookup?id=${APP_ID}&country=us") || { echo "::warning::App Store lookup failed; leaving $FILE unchanged"; exit 0; }
  [ "$(echo "$body" | jq -r '.resultCount')" = "1" ] || { echo "::warning::App Store returned no app; leaving $FILE unchanged"; exit 0; }
  store=$(echo "$body" | jq -r '.results[0].version')
fi
[[ "$store" =~ $valid ]] || { echo "::warning::Unexpected store version '$store'; leaving $FILE unchanged"; exit 0; }

current=$(jq -r '.ios.latestVersion' "$FILE")
[[ "$current" =~ $valid ]] || { echo "::error::Unexpected current version '$current' in $FILE"; exit 1; }

newest=$(printf '%s\n%s\n' "$current" "$store" | sort -V | tail -n1)
if [ "$store" = "$current" ] || [ "$newest" != "$store" ]; then
  echo "No change: App Store $store, file $current"; exit 0
fi

tmp=$(mktemp); jq --arg v "$store" '.ios.latestVersion=$v' "$FILE" > "$tmp" && mv "$tmp" "$FILE"
echo "latestVersion: $current -> $store"
echo "changed=true" >> "${GITHUB_OUTPUT:-/dev/null}"
echo "version=$store" >> "${GITHUB_OUTPUT:-/dev/null}"
