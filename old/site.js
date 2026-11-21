(() => {
  // Header gains depth once content scrolls beneath it
  const h = document.querySelector("header");
  const f = () => h.classList.toggle("scrolled", scrollY > 8);
  f(); addEventListener("scroll", f, { passive: true });

  // Sections and card grids reveal once as they enter the viewport
  const els = [...document.querySelectorAll("main section, main section > .grid")];
  els.forEach(e => e.classList.add("reveal"));
  if (!("IntersectionObserver" in window)) { els.forEach(e => e.classList.add("in")); return; }
  const io = new IntersectionObserver(es => es.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
  }), { rootMargin: "0px 0px -60px 0px" });
  els.forEach(e => io.observe(e));
})();
