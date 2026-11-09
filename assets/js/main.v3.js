/* ИП Сорока: панель меню, разрез конструкции, фильтр объектов, заявка */

var WA_BASE = 'https://wa.me/375259048566';

document.addEventListener('DOMContentLoaded', function () {
  initDrawer();
  initCut();
  initWorks();
  initForm();
  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();
});

/* Панель меню: fixed-слой, блокировка прокрутки, ловушка фокуса, Escape */
function initDrawer() {
  var burger = document.getElementById('burger');
  var drawer = document.getElementById('drawer');
  if (!burger || !drawer) return;
  var lastFocus = null;

  function open() {
    lastFocus = document.activeElement;
    drawer.hidden = false;
    burger.setAttribute('aria-expanded', 'true');
    document.body.classList.add('is-locked');
    var btn = document.getElementById('drawer-close');
    if (btn) btn.focus({ preventScroll: true });
  }

  function close() {
    drawer.hidden = true;
    burger.setAttribute('aria-expanded', 'false');
    document.body.classList.remove('is-locked');
    if (lastFocus) lastFocus.focus({ preventScroll: true });
  }

  burger.addEventListener('click', function () {
    if (drawer.hidden) open(); else close();
  });

  var closeBtn = document.getElementById('drawer-close');
  if (closeBtn) closeBtn.addEventListener('click', close);

  drawer.addEventListener('click', function (e) {
    if (e.target.closest('a')) { close(); return; }
    if (!e.target.closest('.drawer__inner')) close();
  });

  document.addEventListener('keydown', function (e) {
    if (drawer.hidden) return;
    if (e.key === 'Escape') { close(); return; }
    if (e.key !== 'Tab') return;
    var items = drawer.querySelectorAll('a, button');
    if (!items.length) return;
    var first = items[0], last = items[items.length - 1];
    if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
    else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
  });

  window.addEventListener('resize', function () {
    if (window.innerWidth > 1180 && !drawer.hidden) close();
  });
}

/* Разрез конструкции: вкладки + выбор слоя */
function initCut() {
  var tabs = document.querySelectorAll('.cut__tabs .tab');
  if (!tabs.length) return;
  var svgs = document.querySelectorAll('.svg-panel');
  var lists = document.querySelectorAll('.list-panel');

  function showPanel(pid) {
    [].forEach.call(tabs, function (t) {
      var on = t.getAttribute('data-panel') === pid;
      t.classList.toggle('is-on', on);
      t.setAttribute('aria-selected', String(on));
    });
    [].forEach.call(svgs, function (s) {
      s.classList.toggle('is-hidden', s.getAttribute('data-panel') !== pid);
    });
    [].forEach.call(lists, function (l) {
      l.classList.toggle('is-hidden', l.getAttribute('data-panel') !== pid);
    });
  }

  function activateLayer(panel, i) {
    var host = document.querySelector('.list-panel[data-panel="' + panel + '"]');
    var svgHost = document.querySelector('.svg-panel[data-panel="' + panel + '"]');
    if (!host || !svgHost) return;
    [].forEach.call(host.querySelectorAll('.layer'), function (b) {
      b.classList.toggle('is-active', b.getAttribute('data-i') === String(i));
    });
    [].forEach.call(svgHost.querySelectorAll('.seg'), function (s) {
      s.classList.toggle('is-active', s.getAttribute('data-i') === String(i));
    });
  }

  [].forEach.call(tabs, function (t) {
    t.addEventListener('click', function () {
      var pid = t.getAttribute('data-panel');
      showPanel(pid);
      activateLayer(pid === 'found' ? 'found' : pid, 0);
    });
  });

  [].forEach.call(lists, function (host) {
    var pid = host.getAttribute('data-panel');
    host.addEventListener('click', function (e) {
      var b = e.target.closest('.layer');
      if (!b) return;
      activateLayer(pid, b.getAttribute('data-i'));
    });
  });

  [].forEach.call(svgs, function (host) {
    var pid = host.getAttribute('data-panel');
    host.addEventListener('click', function (e) {
      var r = e.target.closest('.seg');
      if (!r) return;
      activateLayer(pid, r.getAttribute('data-i'));
      var li = document.querySelector('.list-panel[data-panel="' + pid + '"] .layer[data-i="' + r.getAttribute('data-i') + '"]');
      if (li && window.innerWidth < 900) li.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
    });
  });
}

/* Фильтр объектов */
function initWorks() {
  var chips = document.getElementById('chips');
  if (!chips) return;
  var shots = [].slice.call(document.querySelectorAll('.shot'));
  chips.addEventListener('click', function (e) {
    var btn = e.target.closest('.chip');
    if (!btn) return;
    var cat = btn.getAttribute('data-cat');
    [].forEach.call(chips.querySelectorAll('.chip'), function (c) {
      c.classList.toggle('is-on', c === btn);
      c.setAttribute('aria-selected', String(c === btn));
    });
    var shown = 0;
    shots.forEach(function (s) {
      var hit = cat === 'all' || s.getAttribute('data-cat') === cat;
      s.classList.toggle('is-hidden', !hit);
      if (hit) shown++;
    });
    var lead = document.querySelector('.phead__lead');
    if (lead && !lead.dataset.base) lead.dataset.base = lead.textContent;
    if (lead) lead.textContent = cat === 'all'
      ? lead.dataset.base
      : 'Показано ' + shown + ' из ' + shots.length + ': ' + btn.textContent.trim().toLowerCase() + '.';
  });
}

/* Заявка */
function initForm() {
  var form = document.getElementById('lead-form');
  if (!form) return;
  var ok = document.getElementById('form-ok');
  var out = document.getElementById('order-text');
  var send = document.getElementById('order-send');
  var copy = document.getElementById('order-copy');

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var name = document.getElementById('f-name');
    var contact = document.getElementById('f-contact');
    var what = document.getElementById('f-what');
    var note = document.getElementById('f-note');
    var bad = false;
    [name, contact].forEach(function (el) {
      if (!el.value.trim()) { el.style.borderColor = '#FF3B00'; bad = true; }
      else el.style.borderColor = '';
    });
    if (bad) return;

    var text = 'Заявка с сайта: ИП Сорока\n' +
      'Имя: ' + name.value.trim() + '\n' +
      'Контакт: ' + contact.value.trim() + '\n' +
      'Работы: ' + what.value + '\n' +
      (note.value.trim() ? 'Объект: ' + note.value.trim() + '\n' : '') +
      'Фото приложу в чате.';
    out.textContent = text;
    send.href = WA_BASE + '?text=' + encodeURIComponent(text);
    if (ok.hidden) {
      ok.hidden = false;
      form.querySelectorAll('input, select, textarea, .form__btn').forEach(function (el) { el.disabled = true; });
    }
    ok.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
  });

  if (copy) {
    copy.addEventListener('click', function () {
      var text = out.textContent || '';
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text);
      } else {
        var ta = document.createElement('textarea');
        ta.value = text; document.body.appendChild(ta); ta.select();
        document.execCommand('copy'); document.body.removeChild(ta);
      }
      copy.textContent = 'Скопировано';
      setTimeout(function () { copy.textContent = 'Скопировать'; }, 1800);
    });
  }
}
