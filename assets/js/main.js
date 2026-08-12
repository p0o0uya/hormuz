(function () {
  'use strict';

  var STORAGE_KEY = 'hodc-lang';
  var toggle = document.getElementById('lang-toggle');

  function applyLang(lang) {
    var isFa = lang === 'fa';
    document.documentElement.lang = lang;
    document.documentElement.dir = isFa ? 'rtl' : 'ltr';
    document.title = isFa ? 'مرکز داده هرمز | HODC' : 'Hormuz Data Center | HODC';

    document.querySelectorAll('[data-en]').forEach(function (el) {
      var text = el.getAttribute(isFa ? 'data-fa' : 'data-en');
      if (text !== null) el.textContent = text;
    });

    toggle.textContent = isFa ? 'EN' : 'فا';

    try { localStorage.setItem(STORAGE_KEY, lang); } catch (e) { /* ignore */ }
  }

  function currentLang() {
    try {
      var saved = localStorage.getItem(STORAGE_KEY);
      if (saved === 'en' || saved === 'fa') return saved;
    } catch (e) { /* ignore */ }
    return 'fa';
  }

  toggle.addEventListener('click', function () {
    applyLang(document.documentElement.lang === 'fa' ? 'en' : 'fa');
  });

  applyLang(currentLang());
})();
