# -*- coding: utf-8 -*-
"""Собирает весь сайт Сороки в один HTML-файл: страницы, стили, скрипт и фото внутри."""
import base64, json, re, pathlib, build as b

OUT = "soroka-single.html"
ROOT = pathlib.Path(".")

from PIL import Image
import io

def datauri(path, optimize=True):
    p = ROOT / path
    if not p.exists():
        raise SystemExit("нет файла " + path)
    if p.suffix.lower() == ".svg":
        return "data:image/svg+xml;base64,%s" % base64.b64encode(p.read_bytes()).decode()
    if optimize:
        im = Image.open(p).convert("RGB")
        if im.width > 1200:
            im = im.resize((1200, round(im.height * 1200 / im.width)), Image.LANCZOS)
        buf = io.BytesIO()
        im.save(buf, "JPEG", quality=80, optimize=True, progressive=True)
        return "data:image/jpeg;base64,%s" % base64.b64encode(buf.getvalue()).decode()
    mime = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png", ".webp": "image/webp"}[p.suffix.lower()]
    return "data:%s;base64,%s" % (mime, base64.b64encode(p.read_bytes()).decode())

def collect_images(*chunks):
    names = set()
    for c in chunks:
        names.update(re.findall(r'src="(assets/img/[^"]+)"', c))
    return {n: datauri(n) for n in sorted(names)}

def to_hash(html):
    html = re.sub(r'href="index\.html"', 'href="#/"', html)
    html = re.sub(r'href="([a-z]+)\.html#([a-z]+)"', r'href="#/\1/\2"', html)
    html = re.sub(r'href="(uslugi|raboty|proizvodstvo|kontakty|politika)\.html"', r'href="#/\1"', html)
    return html

# --- страницы
sections, meta = [], {}
for slug, title, desc, body in b.PAGES:
    raw = b.build_index() if body is None else body
    raw = (raw.replace("__PH__", b.PHONE_H).replace("__PHONE__", b.PHONE)
              .replace("__CITY__", b.CITY).replace("__AREA__", b.AREA).replace("__WA__", b.WA))
    key = "index" if slug == "index.html" else slug[:-5]
    meta[key] = (title, desc)
    attr = "" if key == "index" else " hidden"
    sections.append('<div class="pg" id="pg-%s" data-title="%s" data-desc="%s"%s>\n%s\n</div>'
                    % (key, title.replace('"', "&quot;"), desc.replace('"', "&quot;"), attr, raw))

css = b.CRIT + "\n" + (ROOT / "assets/css/style.v2.css").read_text(encoding="utf-8")
css += """
/* --- одностраничный режим --- */
.pg[hidden]{display:none!important}
html{scroll-behavior:auto}
"""
js = (ROOT / "assets/js/main.v3.js").read_text(encoding="utf-8")

header = b.HEADER.replace("{nav}", b.nav_html("index.html")).replace("__PH__", b.PHONE_H).replace("__PHONE__", b.PHONE)
foot = (b.FOOT.replace("{nav_foot}", "".join('<a href="%s">%s</a>' % (h, l) for h, l in b.NAV))
              .replace("__PH__", b.PHONE_H).replace("__PHONE__", b.PHONE)
              .replace("__CITY__", b.CITY).replace("__AREA__", b.AREA))
drawer = (b.DRAWER.replace("{drawer_nav}", b.nav_html("index.html"))
                .replace("__PH__", b.PHONE_H).replace("__PHONE__", b.PHONE).replace("__CITY__", b.CITY))

router = """
/* --- переключение страниц внутри одного файла --- */
(function(){
  var pages = [].slice.call(document.querySelectorAll('.pg'));
  var links = [].slice.call(document.querySelectorAll('a[href^="#/"]'));
  var ids = {'': 'index', '/': 'index'};
  pages.forEach(function(p){ ids['/' + p.id.replace('pg-', '')] = p.id.replace('pg-', ''); });

  function parse(){
    var h = location.hash.replace(/^#/, '') || '/';
    var parts = h.split('/').filter(Boolean);
    return { page: parts[0] || 'index', anchor: parts[1] || '' };
  }
  function show(scroll){
    var s = parse();
    var key = ids['/' + s.page] || 'index';
    var target = document.getElementById('pg-' + key);
    if (!target) return;
    pages.forEach(function(p){ p.hidden = p !== target; });
    document.title = target.dataset.title;
    var md = document.querySelector('meta[name="description"]');
    if (md) md.setAttribute('content', target.dataset.desc);
    links.forEach(function(a){
      var k = 'index';
      var m = a.getAttribute('href').match(/^#\\/([a-z]+)/);
      if (m) k = m[1];
      if (a.closest('.nav, .drawer__nav, .foot__nav')) a.classList.toggle('is-current', k === key);
    });
    if (s.anchor) {
      var el = document.getElementById(s.anchor);
      if (el) { el.scrollIntoView({block: 'start'}); return; }
    }
    if (scroll) window.scrollTo(0, 0);
  }
  window.addEventListener('hashchange', function(){ show(true); });
  show(false);
})();
"""

html = """<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
<meta name="description" content="%s">
<meta name="theme-color" content="#0D0D0C">
<meta property="og:type" content="website">
<meta property="og:locale" content="ru_BY">
<link rel="icon" href="%s" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Russo+One&family=Anonymous+Pro:wght@400;700&display=swap" rel="stylesheet">
<style>%s</style>
<script type="application/ld+json">%s</script>
</head>
<body>
%s
%s
%s
%s
<script>%s</script>
<script>%s</script>
</body>
</html>
""" % (b.PAGES[0][1], b.PAGES[0][2], datauri("favicon.svg"), css,
       json.dumps(b.LD, ensure_ascii=False),
       to_hash(header), "\n".join(sections), to_hash(foot), to_hash(drawer), js, router)

img_map = collect_images(header, foot, drawer, *sections)
img_script = "var IMG=%s;\n" % json.dumps(img_map, ensure_ascii=False)
img_script += "(function(){var m=IMG;for(var k in m){if(!m.hasOwnProperty(k))continue;}\n" \
              "document.querySelectorAll('img[src^=\"assets/img/\"]').forEach(function(i){var u=m[i.getAttribute('src')];if(u)i.src=u;});})();\n"
html = html.replace('<script>' + js + '</script>', '<script>' + img_script + '</script>\n<script>' + js + '</script>')
pathlib.Path(OUT).write_text(html, encoding="utf-8")
print("уникальных фото:", len(img_map))
print("собран", OUT, round(len(html.encode()) / 1024 / 1024, 2), "МБ")
