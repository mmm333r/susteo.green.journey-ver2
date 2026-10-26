/* バイオ燃料HVO サステオ ｜ デモ版の挙動
   ナビゲーション、ページ内目次の現在地表示、記事の絞り込み、
   CO2削減量シミュレーション、フォームの送信抑止。 */
(function () {
  'use strict';

  /* ---- ヘッダーのナビゲーション（狭い画面） ---- */
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');

  function isNarrow() {
    return window.matchMedia('(max-width: 1040px)').matches;
  }

  function syncNav() {
    if (!nav) return;
    if (isNarrow()) {
      nav.hidden = nav.dataset.open !== 'true';
    } else {
      nav.hidden = false;
    }
    if (toggle) toggle.setAttribute('aria-expanded', String(nav.dataset.open === 'true' && isNarrow()));
  }

  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      nav.dataset.open = nav.dataset.open === 'true' ? 'false' : 'true';
      syncNav();
    });
    nav.addEventListener('click', function (e) {
      if (e.target.tagName === 'A' && isNarrow()) {
        nav.dataset.open = 'false';
        syncNav();
      }
    });
    window.addEventListener('resize', syncNav);
    syncNav();
  }

  /* ---- ページ内目次：現在読んでいる節を示す ---- */
  var railLinks = Array.prototype.slice.call(document.querySelectorAll('.rail a[href^="#"]'));
  var sections = railLinks
    .map(function (a) { return document.getElementById(a.getAttribute('href').slice(1)); })
    .filter(Boolean);

  if (sections.length) {
    var mark = function (id) {
      railLinks.forEach(function (a) {
        a.classList.toggle('is-active', a.getAttribute('href') === '#' + id);
      });
    };

    /* 画面上から約3割の位置を「読んでいる行」とみなし、
       その行より上で最も下にある節を現在地とする。 */
    var pending = false;
    var updateSpy = function () {
      pending = false;
      var line = window.innerHeight * 0.3;
      var current = sections[0];
      for (var i = 0; i < sections.length; i++) {
        if (sections[i].getBoundingClientRect().top <= line) current = sections[i];
      }
      // ページ最下部では最後の節を現在地にする
      if (window.innerHeight + window.scrollY >= document.body.scrollHeight - 2) {
        current = sections[sections.length - 1];
      }
      mark(current.id);
    };
    var requestSpy = function () {
      if (pending) return;
      pending = true;
      window.requestAnimationFrame(updateSpy);
    };

    window.addEventListener('scroll', requestSpy, { passive: true });
    window.addEventListener('resize', requestSpy);
    updateSpy();
  }

  /* ---- 記事一覧の絞り込み ---- */
  var tabs = Array.prototype.slice.call(document.querySelectorAll('.tab[data-filter]'));
  var articles = Array.prototype.slice.call(document.querySelectorAll('[data-cat]'));
  var countEl = document.getElementById('article-count');

  if (tabs.length && articles.length) {
    var applyFilter = function (value) {
      var shown = 0;
      articles.forEach(function (item) {
        var hit = value === 'all' || item.dataset.cat === value;
        item.hidden = !hit;
        if (hit) shown++;
      });
      tabs.forEach(function (t) {
        t.setAttribute('aria-pressed', String(t.dataset.filter === value));
      });
      if (countEl) countEl.textContent = shown + '件';
    };
    tabs.forEach(function (t) {
      t.addEventListener('click', function () { applyFilter(t.dataset.filter); });
    });
    applyFilter('all');
  }

  /* ---- CO2削減量シミュレーション ----
     削減量(t-CO2) = 軽油使用量(kL) × 2.62 × HVO混合率
     軽油のCO2排出係数 2.62 t-CO2/kL（温対法 算定・報告・公表制度）  */
  var DIESEL_FACTOR = 2.62;
  var simForm = document.getElementById('sim');

  if (simForm) {
    var volumeInput = document.getElementById('sim-volume');
    var valueEl = document.getElementById('sim-value');
    var unitEl = document.getElementById('sim-unit');
    var msgEl = document.getElementById('sim-msg');
    var outEl = document.getElementById('sim-out');
    var detailEl = document.getElementById('sim-detail');

    var ratio = function () {
      var picked = simForm.querySelector('input[name="product"]:checked');
      return picked && picked.value === '51' ? 0.51 : 1;
    };
    var productName = function () {
      return ratio() === 1 ? 'サステオ100' : 'サステオ51';
    };

    var calc = function () {
      var raw = volumeInput.value.trim();
      var volume = raw === '' ? NaN : Number(raw);

      if (!isFinite(volume) || volume <= 0) {
        outEl.dataset.state = 'error';
        valueEl.textContent = '—';
        unitEl.textContent = '';
        msgEl.textContent = '軽油の年間使用量を入力してください';
        if (detailEl) detailEl.textContent = '';
        return;
      }

      var reduction = volume * DIESEL_FACTOR * ratio();
      outEl.dataset.state = 'ok';
      valueEl.textContent = '約 ' + reduction.toFixed(1);
      unitEl.textContent = 't-CO₂ / 年';
      msgEl.textContent = productName() + 'に切り替えた場合の概算値です。';
      if (detailEl) {
        detailEl.textContent =
          '計算式：' + volume.toLocaleString('ja-JP') + ' kL × ' + DIESEL_FACTOR +
          ' t-CO₂/kL × HVO混合率 ' + Math.round(ratio() * 100) + '％ = ' + reduction.toFixed(1) + ' t-CO₂';
      }
    };

    volumeInput.addEventListener('input', calc);
    simForm.addEventListener('change', calc);
    simForm.addEventListener('submit', function (e) { e.preventDefault(); calc(); });
    calc();
  }

  /* ---- フォーム：デモ版は送信しない ---- */
  var contactForm = document.getElementById('contact-form');
  if (contactForm) {
    var result = document.getElementById('contact-result');
    contactForm.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!result) return;
      if (!contactForm.reportValidity()) return;
      result.hidden = false;
      result.textContent = 'デモ版のため送信は行われません。本番環境では、入力内容の確認画面を経て相談種別ごとの担当窓口へ送信されます。';
      result.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
    });
  }
})();
