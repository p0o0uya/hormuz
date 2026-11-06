(function () {
  'use strict';

  var STORAGE_KEY = 'hormuz-lang';
  var toggle = document.getElementById('lang-toggle');
  var slider = document.querySelector('.hero-slider');
  var slides = slider ? Array.prototype.slice.call(slider.querySelectorAll('.slide')) : [];
  var dots = slider ? Array.prototype.slice.call(slider.querySelectorAll('.slider-dot')) : [];
  var activeSlide = 0;
  var autoplayTimer;

  function applyLang(lang) {
    var isFa = lang === 'fa';
    document.documentElement.lang = lang;
    document.documentElement.dir = isFa ? 'rtl' : 'ltr';
    document.title = 'Hormuz | هرمز';

    document.querySelectorAll('[data-en]').forEach(function (el) {
      var text = el.getAttribute(isFa ? 'data-fa' : 'data-en');
      if (text !== null) el.textContent = text;
    });

    toggle.textContent = isFa ? 'EN' : 'فا';

    if (slider) {
      slider.setAttribute('aria-label', slider.getAttribute(isFa ? 'data-fa-label' : 'data-en-label'));
    }

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

  function showSlide(index) {
    if (!slides.length) return;
    activeSlide = (index + slides.length) % slides.length;
    slides.forEach(function (slide, i) {
      var active = i === activeSlide;
      slide.classList.toggle('is-active', active);
      slide.setAttribute('aria-hidden', active ? 'false' : 'true');
      dots[i].classList.toggle('is-active', active);
      dots[i].setAttribute('aria-selected', active ? 'true' : 'false');
    });
  }

  function restartAutoplay() {
    window.clearInterval(autoplayTimer);
    if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      autoplayTimer = window.setInterval(function () { showSlide(activeSlide + 1); }, 6000);
    }
  }

  if (slider) {
    slider.querySelector('.slider-prev').addEventListener('click', function () { showSlide(activeSlide - 1); restartAutoplay(); });
    slider.querySelector('.slider-next').addEventListener('click', function () { showSlide(activeSlide + 1); restartAutoplay(); });
    dots.forEach(function (dot, index) {
      dot.addEventListener('click', function () { showSlide(index); restartAutoplay(); });
    });
    slider.addEventListener('mouseenter', function () { window.clearInterval(autoplayTimer); });
    slider.addEventListener('mouseleave', restartAutoplay);
    slider.addEventListener('focusin', function () { window.clearInterval(autoplayTimer); });
    slider.addEventListener('focusout', restartAutoplay);
    restartAutoplay();
  }

  applyLang(currentLang());
})();
