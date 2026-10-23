/* Native section anchors preserve direct links, history, and no-JavaScript access. */
(() => {
  const root = document.documentElement;
  const button = document.getElementById('theme-toggle');
  const label = button.querySelector('.theme-label');
  const setTheme = (dark) => {
    root.dataset.theme = dark ? 'dark' : 'light';
    button.setAttribute('aria-pressed', String(dark));
    label.textContent = dark ? 'Light' : 'Dark';
  };
  let dark = false;
  try { dark = localStorage.getItem('hangu-theme') === 'dark'; } catch (_) { /* Storage is optional. */ }
  setTheme(dark);
  button.hidden = false;
  button.addEventListener('click', () => {
    const next = root.dataset.theme !== 'dark';
    setTheme(next);
    try { localStorage.setItem('hangu-theme', next ? 'dark' : 'light'); } catch (_) { /* Storage is optional. */ }
  });

  const address = 'hangu.chen' + '@' + 'du' + '.' + 'edu';
  document.querySelectorAll('[data-email]').forEach((link) => { link.href = 'mailto:' + address; });
  document.getElementById('year').textContent = new Date().getFullYear();

  const links = Array.from(document.querySelectorAll('.nav a'));
  const markCurrent = (id) => {
    links.forEach((link) => {
      if (link.getAttribute('href') === '#' + id) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    });
  };
  const syncHash = () => markCurrent(window.location.hash.slice(1));
  window.addEventListener('hashchange', syncHash);
  window.addEventListener('popstate', syncHash);
  syncHash();
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      const visible = entries.filter((entry) => entry.isIntersecting);
      if (visible.length) markCurrent(visible[0].target.id);
    }, { rootMargin: '-18% 0px -60% 0px', threshold: 0 });
    document.querySelectorAll('.hero, .section, #contact').forEach((section) => observer.observe(section));
  }
})();
