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
  const packTrack = document.querySelector('#legacy-pack-track');
  const packSlides = [...packTrack.querySelectorAll('[data-pack-id]')];
  const packUI = document.querySelector('[data-carousel-ui]');
  const packPrev = document.querySelector('[data-pack-prev]');
  const packNext = document.querySelector('[data-pack-next]');
  const packDots = [...document.querySelectorAll('[data-pack-dot]')];
  const packStatus = document.querySelector('[data-pack-status]');
  let packIndex = 0;
  let packIntent = null;
  function packPosition(index) { return packSlides[index].offsetLeft - 2; }
  function describePack(index) {
    packIndex = index;
    packPrev.disabled = index === 0;
    packNext.disabled = index === packSlides.length - 1;
    packDots.forEach((dot, i) => dot.setAttribute('aria-current', String(i === index)));
    const label = `${index + 1} / ${packSlides.length} · ${packSlides[index].querySelector('h3').textContent}`;
    if (packStatus.textContent !== label) packStatus.textContent = label;
  }
  function nearestPack() {
    return packSlides.reduce((best, _, index) =>
      Math.abs(packPosition(index) - packTrack.scrollLeft) < Math.abs(packPosition(best) - packTrack.scrollLeft) ? index : best, 0);
  }
  function goToPack(index, animate = true) {
    const next = Math.max(0, Math.min(index, packSlides.length - 1));
    const destination = Math.min(Math.max(0, packPosition(next)), packTrack.scrollWidth - packTrack.clientWidth);
    const smooth = animate && !reducedMotion.matches;
    packIntent = smooth && Math.abs(packTrack.scrollLeft - destination) >= 2 ? next : null;
    describePack(next);
    packTrack.scrollTo({ left:destination, behavior:smooth ? 'smooth' : 'instant' });
  }
  packUI.hidden = false;
  describePack(0);
  packPrev.addEventListener('click', () => goToPack((packIntent ?? packIndex) - 1));
  packNext.addEventListener('click', () => goToPack((packIntent ?? packIndex) + 1));
  packDots.forEach((dot, i) => dot.addEventListener('click', () => goToPack(i)));
  let packScrollFrame = 0;
  packTrack.addEventListener('scroll', () => {
    if (packScrollFrame) return;
    packScrollFrame = requestAnimationFrame(() => {
      describePack(nearestPack());
      if (packIntent !== null) {
        const destination = Math.min(Math.max(0, packPosition(packIntent)), packTrack.scrollWidth - packTrack.clientWidth);
        if (Math.abs(packTrack.scrollLeft - destination) < 2) packIntent = null;
      }
      packScrollFrame = 0;
    });
  }, { passive:true });
  packTrack.addEventListener('keydown', event => {
    if (event.target !== packTrack) return;
    if (!['ArrowLeft','ArrowRight','Home','End'].includes(event.key)) return;
    event.preventDefault();
    goToPack(event.key === 'Home' ? 0 : event.key === 'End' ? packSlides.length - 1 : (packIntent ?? packIndex) + (event.key === 'ArrowRight' ? 1 : -1));
  });
  let packDrag = null;
  packTrack.addEventListener('wheel', () => { packIntent = null; }, { passive:true });
  packTrack.addEventListener('dragstart', event => event.preventDefault());
  packTrack.addEventListener('pointerdown', event => {
    packIntent = null;
    if (event.pointerType !== 'mouse' || event.button !== 0 || event.target.closest('button,a,summary,details[open]')) return;
    packTrack.scrollTo({ left:packTrack.scrollLeft, behavior:'instant' });
    packDrag = { id:event.pointerId, x:event.clientX, left:packTrack.scrollLeft, moved:false };
    packTrack.setPointerCapture(event.pointerId);
  });
  packTrack.addEventListener('pointermove', event => {
    if (!packDrag || event.pointerId !== packDrag.id) return;
    const distance = event.clientX - packDrag.x;
    if (!packDrag.moved && Math.abs(distance) < 6) return;
    packDrag.moved = true;
    packTrack.classList.add('is-dragging');
    event.preventDefault();
    packTrack.scrollLeft = packDrag.left - distance;
  });
  function finishPackDrag(event) {
    if (!packDrag || event.pointerId !== packDrag.id) return;
    const moved = packDrag.moved;
    if (packTrack.hasPointerCapture(packDrag.id)) packTrack.releasePointerCapture(packDrag.id);
    packDrag = null;
    packTrack.classList.remove('is-dragging');
    if (moved) goToPack(nearestPack());
  }
  packTrack.addEventListener('pointerup', finishPackDrag);
  packTrack.addEventListener('pointercancel', finishPackDrag);
  let packWidth = packTrack.clientWidth;
  function resizePacks() {
    if (packWidth === packTrack.clientWidth) return;
    packWidth = packTrack.clientWidth;
    goToPack(packIndex, false);
  }
  if ('ResizeObserver' in window) new ResizeObserver(resizePacks).observe(packTrack);
  else window.addEventListener('resize', resizePacks);
})();
