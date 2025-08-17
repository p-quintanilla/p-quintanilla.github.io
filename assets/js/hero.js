(function () {
  const root = document.querySelector('[data-hero-slider]');
  if (!root) return;

  const slides = Array.from(root.querySelectorAll('.hero-slide'));
  const dots = Array.from(root.querySelectorAll('.hero-dots .dot'));
  if (slides.length <= 1) return;

  let i = 0;
  let timer = null;
  const delay = 5000; // ms

  function show(n) {
    slides[i].classList.remove('is-active');
    slides[i].setAttribute('aria-hidden', 'true');
    dots[i].classList.remove('is-active');

    i = (n + slides.length) % slides.length;

    slides[i].classList.add('is-active');
    slides[i].setAttribute('aria-hidden', 'false');
    dots[i].classList.add('is-active');
  }

  function play() {
    stop();
    timer = setInterval(() => show(i + 1), delay);
  }
  function stop() { if (timer) { clearInterval(timer); timer = null; } }

  // start
  play();

  // pause on hover/focus (desktop)
  root.addEventListener('mouseenter', stop);
  root.addEventListener('mouseleave', play);
  root.addEventListener('focusin', stop);
  root.addEventListener('focusout', play);

  // dots
  dots.forEach(btn => btn.addEventListener('click', () => show(+btn.dataset.goto)));

  // keyboard (left/right arrows)
  root.setAttribute('tabindex', '0');
  root.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight') { stop(); show(i + 1); }
    if (e.key === 'ArrowLeft')  { stop(); show(i - 1); }
  });

  // touch swipe (simple)
  let x0 = null;
  root.addEventListener('touchstart', (e) => { x0 = e.touches[0].clientX; }, { passive: true });
  root.addEventListener('touchend', (e) => {
    if (x0 === null) return;
    const dx = e.changedTouches[0].clientX - x0;
    if (Math.abs(dx) > 40) { stop(); show(i + (dx < 0 ? 1 : -1)); }
    x0 = null;
  }, { passive: true });
})();
