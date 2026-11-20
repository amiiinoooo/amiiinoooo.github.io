(() => {
  // Header gains depth once content scrolls beneath it. No other scripted motion.
  const h = document.querySelector("header");
  const f = () => h.classList.toggle("scrolled", scrollY > 8);
  f(); addEventListener("scroll", f, { passive: true });
})();
