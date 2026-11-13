(() => {
  'use strict';
  const es = document.documentElement.lang === 'es';
  const root = document.documentElement;
  const themeButton = document.querySelector('[data-theme-toggle]');
  const preference = window.matchMedia('(prefers-color-scheme: dark)');
  const activeTheme = () => root.dataset.theme || (preference.matches ? 'dark' : 'light');
  function describeTheme() {
    const dark = activeTheme() === 'dark';
    themeButton.setAttribute('aria-label', es ? `Activar modo ${dark ? 'claro' : 'oscuro'}` : `Switch to ${dark ? 'light' : 'dark'} mode`);
    themeButton.setAttribute('aria-pressed', String(dark));
    document.querySelector('meta[name="theme-color"]').content = dark ? '#101e22' : '#f7f5ee';
  }
  themeButton.addEventListener('click', () => {
    root.dataset.theme = activeTheme() === 'dark' ? 'light' : 'dark';
    try { localStorage.setItem('rzen-web-theme', root.dataset.theme); } catch {}
    describeTheme();
  });
  preference.addEventListener('change', describeTheme);
  describeTheme();
  themeButton.hidden = false;
  const menuButton = document.querySelector('[data-menu-toggle]');
  const nav = document.querySelector('#navigation');
  function closeMenu() { nav.hidden = true; menuButton.setAttribute('aria-expanded', 'false'); }
  // Navigation stays available when JavaScript is disabled.
  closeMenu();
  menuButton.hidden = false;
  menuButton.addEventListener('click', () => { nav.hidden = !nav.hidden; menuButton.setAttribute('aria-expanded', String(!nav.hidden)); });
  nav.addEventListener('click', event => { if (event.target.closest('a')) closeMenu(); });
  document.addEventListener('keydown', event => { if (event.key === 'Escape' && !nav.hidden) { closeMenu(); menuButton.focus(); } });
  document.querySelector('[data-language]').addEventListener('click', event => {
    if (location.hash) event.currentTarget.href += location.hash;
  });
  const audio = document.querySelector('audio');
  const play = document.querySelector('[data-play]');
  const track = document.querySelector('[data-track]');
  const audioStatus = document.querySelector('[data-audio-status]');
  function describeAudio() { const playing = !audio.paused; play.textContent = playing ? 'Ⅱ' : '▶'; play.setAttribute('aria-label', es ? (playing ? 'Pausar música' : 'Reproducir música') : (playing ? 'Pause music' : 'Play music')); play.setAttribute('aria-pressed', String(playing)); }
  play.addEventListener('click', async () => {
    if (!audio.paused) return audio.pause();
    try { await audio.play(); audioStatus.textContent = ''; } catch { audioStatus.textContent = es ? 'No se pudo reproducir el audio. Inténtalo de nuevo.' : 'Audio could not play. Please try again.'; }
  });
  track.addEventListener('change', () => { audio.pause(); audio.src = track.value; audio.load(); });
  ['play', 'pause', 'ended'].forEach(name => audio.addEventListener(name, describeAudio));
  audio.addEventListener('error', () => { audioStatus.textContent = es ? 'Audio no disponible.' : 'Audio unavailable.'; });
  const dialog = document.querySelector('#screenshot-dialog');
  let returnFocus;
  document.querySelectorAll('[data-screenshot]').forEach(link => link.addEventListener('click', event => {
    if (!dialog.showModal) return;
    event.preventDefault(); returnFocus = link;
    dialog.querySelector('img').src = link.href;
    dialog.querySelector('img').alt = link.querySelector('img').alt;
    dialog.showModal();
  }));
  dialog.addEventListener('close', () => returnFocus?.focus());
  dialog.addEventListener('click', event => { if (event.target === dialog) { const r = dialog.getBoundingClientRect(); if (event.clientX < r.left || event.clientX > r.right || event.clientY < r.top || event.clientY > r.bottom) dialog.close(); } });
  document.querySelectorAll('[data-download]').forEach(link => link.addEventListener('click', () => {
    // Preserve the existing anonymous, disclosed website download-click counter.
    fetch('https://script.google.com/macros/s/AKfycbxjD3tsT3Jt5JaAjF0J_ga3QsPeEbixUgKTYe1nPhBSPMJ_nR-e7Z_8CDD3w36UMVzmnA/exec', { mode:'no-cors', keepalive:true }).catch(() => {});
  }));
  const previewSection = document.querySelector('#explore');
  const pausePreviews = document.querySelector('[data-preview-motion]');
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  let previewsPaused = false;
  function describePreviews() {
    previewSection.dataset.previewPaused = String(previewsPaused || reducedMotion.matches);
    pausePreviews.disabled = reducedMotion.matches;
    pausePreviews.setAttribute('aria-pressed', String(previewsPaused || reducedMotion.matches));
    pausePreviews.textContent = reducedMotion.matches
      ? (es ? 'Movimiento reducido activado' : 'Reduced motion enabled')
      : previewsPaused ? (es ? 'Reanudar animaciones' : 'Resume animations')
      : (es ? 'Pausar animaciones' : 'Pause animations');
  }
  pausePreviews.hidden = false;
  pausePreviews.addEventListener('click', () => { previewsPaused = !previewsPaused; describePreviews(); });
  reducedMotion.addEventListener('change', describePreviews);
  describePreviews();
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => { entry.target.dataset.previewActive = String(entry.isIntersecting); });
    }, { threshold:0.1 });
    document.querySelectorAll('.app-mode-preview').forEach(preview => observer.observe(preview));
  }
  function pageVisibility() { previewSection.dataset.previewHidden = String(document.hidden); }
  document.addEventListener('visibilitychange', pageVisibility);
  pageVisibility();
  document.querySelectorAll('[data-puzzle-choice]').forEach(button => button.addEventListener('click', () => {
    const kind = button.dataset.puzzleChoice;
    const card = button.closest('[data-app-mode="puzzles"]');
    card.querySelectorAll('[data-puzzle-kind]').forEach(demo => { demo.hidden = demo.dataset.puzzleKind !== kind; });
    card.querySelectorAll('[data-puzzle-choice]').forEach(choice => choice.setAttribute('aria-pressed', String(choice === button)));
  }));
})();
