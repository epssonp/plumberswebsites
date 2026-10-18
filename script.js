(function () {
  'use strict';

  var toggle = document.querySelector('.mobile-menu-toggle');
  var mobileNav = document.getElementById('mobile-navigation');

  if (!toggle || !mobileNav) {
    return;
  }

  function setMenuOpen(open) {
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    mobileNav.classList.toggle('is-open', open);
  }

  function isMenuOpen() {
    return toggle.getAttribute('aria-expanded') === 'true';
  }

  toggle.addEventListener('click', function () {
    setMenuOpen(!isMenuOpen());
  });

  toggle.addEventListener('keydown', function (event) {
    if (event.key === 'Enter' || event.key === ' ') {
      event.preventDefault();
      setMenuOpen(!isMenuOpen());
    }
  });

  mobileNav.querySelectorAll('a').forEach(function (link) {
    link.addEventListener('click', function () {
      setMenuOpen(false);
    });
  });

  document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape' && isMenuOpen()) {
      setMenuOpen(false);
      toggle.focus();
    }
  });
})();
