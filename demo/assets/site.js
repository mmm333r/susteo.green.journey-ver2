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

  /* ---- ページ内タブ ----
     [data-tabs] のなかの role="tab" と、aria-controls が指す role="tabpanel" を
     対応づける。パネルの id をそのまま #ハッシュで開ける。
     「すべて表示」に切り替えると、全パネルを開いてタブ列を目次として使う。 */
  var VIEW_KEY = 'susteo.view';
  var tabGroups = Array.prototype.slice.call(document.querySelectorAll('[data-tabs]'));

  var readView = function () {
    try { return window.localStorage.getItem(VIEW_KEY); } catch (e) { return null; }
  };
  var writeView = function (value) {
    try { window.localStorage.setItem(VIEW_KEY, value); } catch (e) { /* 保存できなくても動作に影響しない */ }
  };

  tabGroups.forEach(function (group) {
    // 入れ子の [data-tabs] は、それぞれが自分のタブだけを受け持つ
    var own = function (selector) {
      return Array.prototype.slice.call(group.querySelectorAll(selector)).filter(function (el) {
        return el.closest('[data-tabs]') === group;
      });
    };
    var tabs = own('[role="tab"], [data-tab]');
    if (!tabs.length) return;
    var list = tabs[0].parentNode;
    var panels = tabs.map(function (t) { return document.getElementById(t.getAttribute('aria-controls')); });

    var expanded = false;
    var current = 0;

    var applyTabs = function () {
      list.setAttribute('role', 'tablist');
      tabs.forEach(function (tab, i) {
        var on = i === current;
        tab.setAttribute('role', 'tab');
        tab.setAttribute('aria-selected', String(on));
        tab.classList.remove('is-active');
        tab.tabIndex = on ? 0 : -1;
        if (panels[i]) {
          panels[i].setAttribute('role', 'tabpanel');
          panels[i].hidden = !on;
        }
      });
    };

    var applyExpanded = function () {
      list.removeAttribute('role');
      tabs.forEach(function (tab, i) {
        tab.removeAttribute('role');
        tab.removeAttribute('aria-selected');
        tab.tabIndex = 0;
        tab.classList.toggle('is-active', i === current);
        if (panels[i]) {
          panels[i].removeAttribute('role');
          panels[i].hidden = false;
        }
      });
    };

    var render = function () { expanded ? applyExpanded() : applyTabs(); };

    var select = function (index, moveFocus) {
      current = index;
      render();
      if (moveFocus) tabs[index].focus();
    };

    tabs.forEach(function (tab, i) {
      tab.addEventListener('click', function () {
        current = i;
        render();
        if (expanded && panels[i]) {
          panels[i].scrollIntoView({ block: 'start', behavior: 'smooth' });
        }
        var id = tab.getAttribute('aria-controls');
        if (id && window.history && window.history.replaceState) {
          window.history.replaceState(null, '', '#' + id);
        }
      });
      tab.addEventListener('keydown', function (e) {
        if (expanded) return;
        var step = { ArrowRight: 1, ArrowDown: 1, ArrowLeft: -1, ArrowUp: -1 }[e.key];
        if (step) {
          e.preventDefault();
          select((i + step + tabs.length) % tabs.length, true);
        } else if (e.key === 'Home') {
          e.preventDefault(); select(0, true);
        } else if (e.key === 'End') {
          e.preventDefault(); select(tabs.length - 1, true);
        }
      });
    });

    var indexForHash = function (hash) {
      if (!hash) return -1;
      for (var i = 0; i < tabs.length; i++) {
        if (tabs[i].getAttribute('aria-controls') === hash) return i;
      }
      return -1;
    };

    group.openByHash = function (hash, scroll) {
      var i = indexForHash(hash);
      if (i < 0) return false;
      current = i;
      render();
      if (scroll && panels[i]) panels[i].scrollIntoView({ block: 'start', behavior: 'auto' });
      return true;
    };

    group.setExpanded = function (value) {
      expanded = value;
      group.dataset.expanded = String(value);
      render();
    };

    // 全表示のときは、読んでいる節をタブ列に反映する
    group.syncActive = function () {
      if (!expanded) return;
      var line = window.innerHeight * 0.3;
      var at = 0;
      panels.forEach(function (panel, i) {
        if (panel && panel.getBoundingClientRect().top <= line) at = i;
      });
      if (at !== current) { current = at; applyExpanded(); }
    };

    var initial = indexForHash(window.location.hash.replace('#', ''));
    current = initial < 0 ? 0 : initial;
    render();
    if (initial > 0) group.scrollIntoView({ block: 'start', behavior: 'auto' });
  });

  if (tabGroups.length) {
    var toggles = Array.prototype.slice.call(document.querySelectorAll('[data-viewtoggle]'));

    var setExpandedAll = function (value, remember) {
      tabGroups.forEach(function (g) { if (g.setExpanded) g.setExpanded(value); });
      toggles.forEach(function (btn) {
        btn.setAttribute('aria-pressed', String(value));
        btn.textContent = value ? 'タブ表示に戻す' : 'すべて表示';
      });
      if (remember) writeView(value ? 'all' : 'tabs');
    };

    toggles.forEach(function (btn) {
      btn.addEventListener('click', function () {
        setExpandedAll(btn.getAttribute('aria-pressed') !== 'true', true);
      });
    });

    // 前回「すべて表示」を選んでいた場合は、その状態で開く
    if (toggles.length && readView() === 'all' && !window.location.hash) {
      setExpandedAll(true, false);
    }

    var pending = false;
    window.addEventListener('scroll', function () {
      if (pending) return;
      pending = true;
      window.requestAnimationFrame(function () {
        pending = false;
        tabGroups.forEach(function (g) { if (g.syncActive) g.syncActive(); });
      });
    }, { passive: true });

    window.addEventListener('hashchange', function () {
      var hash = window.location.hash.replace('#', '');
      tabGroups.some(function (g) { return g.openByHash(hash, true); });
    });
    document.addEventListener('click', function (e) {
      var link = e.target.closest ? e.target.closest('a[href^="#"]') : null;
      if (!link) return;
      var hash = link.getAttribute('href').slice(1);
      var opened = tabGroups.some(function (g) { return g.openByHash(hash, true); });
      if (opened) e.preventDefault();
    });
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
    var meterEl = document.getElementById('sim-meter');
    var fillEl = document.getElementById('sim-fill');
    var cutEl = document.getElementById('sim-cut');
    var leftEl = document.getElementById('sim-left');

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
        if (meterEl) meterEl.hidden = true;
        return;
      }

      var baseline = volume * DIESEL_FACTOR;
      var reduction = baseline * ratio();
      var remaining = baseline - reduction;
      outEl.dataset.state = 'ok';
      valueEl.textContent = '約 ' + reduction.toFixed(1);
      unitEl.textContent = 't-CO₂ / 年';
      msgEl.textContent = productName() + 'に切り替えた場合の概算値です。';
      if (meterEl) {
        var share = ratio() * 100;
        meterEl.hidden = false;
        fillEl.style.width = share + '%';
        fillEl.dataset.full = String(share >= 100);
        cutEl.textContent = reduction.toFixed(1) + ' t-CO₂';
        leftEl.textContent = remaining.toFixed(1) + ' t-CO₂';
      }
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
