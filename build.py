# -*- coding: utf-8 -*-
"""ИП Сорока: монолит, кладка, кровля. Лида, Гродненская область."""

import json

PHONE = "+375 (25) 904-85-66"
PHONE_H = "+375259048566"
WA = "https://wa.me/375259048566"
CITY = "Лида"
AREA = "Лида и Гродненская область"
SITE = "https://romjjjke.github.io/soroka/"

NAV = [
    ("index.html", "Главная"),
    ("uslugi.html", "Работы и услуги"),
    ("raboty.html", "Объекты"),
    ("proizvodstvo.html", "Бригада"),
    ("kontakty.html", "Контакты"),
]

CRIT = """[hidden]{display:none!important}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
body{margin:0;background:#0D0D0C;color:#EFEDE6;font:400 16px/1.62 "Anonymous Pro",ui-monospace,monospace;-webkit-font-smoothing:antialiased}
img{display:block;max-width:100%;height:auto}
a{color:inherit;text-decoration:none}
h1,h2,h3,p,ul,ol,figure,dl,dd{margin:0}
ul,ol{padding:0;list-style:none}
button{font:inherit}
.head{position:sticky;top:0;z-index:60;background:#0D0D0C;border-bottom:1px solid rgba(239,237,230,.16)}
.head__row{display:flex;align-items:center;gap:16px;padding:12px clamp(14px,3.6vw,44px)}
.brand{font:400 15px/1 "Russo One",sans-serif;letter-spacing:.14em;text-transform:uppercase}
.brand small{display:block;font:400 9.5px/1.7 "Anonymous Pro",monospace;letter-spacing:.2em;color:#A8A49A;margin-top:5px}
.nav{display:flex;gap:16px;margin-left:auto;font:400 10.5px/1 "Anonymous Pro",monospace;letter-spacing:.14em;text-transform:uppercase}
.head__tel{margin-left:16px;font:400 12.5px/1 "Anonymous Pro",monospace;border-bottom:1px solid #FF3B00;padding-bottom:4px}
.burger{display:none;width:44px;height:38px;margin-left:auto;border:1px solid #EFEDE6;background:transparent;cursor:pointer;padding:9px}
.burger span{display:block;height:1.5px;background:#EFEDE6;margin:4px 0}
.hero{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr);border-bottom:1px solid rgba(239,237,230,.16);min-height:min(88vh,860px)}
.hero__body{padding:clamp(22px,4vw,60px) clamp(14px,3.6vw,44px);display:flex;flex-direction:column;justify-content:space-between;gap:26px}
.hero__media{position:relative;overflow:hidden;background:#191918}
.hero__media img{width:100%;height:100%;object-fit:cover;filter:contrast(1.05)}
.kicker{font:400 10px/1.4 "Anonymous Pro",monospace;letter-spacing:.22em;text-transform:uppercase;color:#FF3B00}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;padding:14px 20px;border:1px solid #EFEDE6;background:transparent;color:#EFEDE6;font:400 10.5px/1 "Anonymous Pro",monospace;letter-spacing:.16em;text-transform:uppercase;cursor:pointer;transition:.2s}
.btn--solid{background:#FF3B00;border-color:#FF3B00;color:#0D0D0C}
.wrap{padding-inline:clamp(14px,3.6vw,44px);max-width:1560px;margin:0 auto}
.drawer{position:fixed;inset:0;z-index:90;background:#0D0D0C;color:#EFEDE6;overflow-y:auto;overscroll-behavior:contain}
.drawer__inner{padding:clamp(54px,9vw,80px) clamp(16px,5vw,54px) clamp(24px,5vw,44px);display:flex;flex-direction:column;gap:22px;min-height:100%}
.drawer__close{position:fixed;top:12px;right:12px;width:46px;height:46px;border:1px solid rgba(239,237,230,.45);background:transparent;color:#EFEDE6;font-size:24px;line-height:1;cursor:pointer}
.drawer__nav{display:flex;flex-direction:column}
.drawer__nav a{font:400 clamp(1.3rem,.9rem + 2.2vw,2rem)/1.16 "Russo One",sans-serif;letter-spacing:.04em;text-transform:uppercase;padding:13px 0;border-bottom:1px solid rgba(239,237,230,.16)}
.drawer__meta{font:400 12px/1.8 "Anonymous Pro",monospace;color:rgba(239,237,230,.78);display:flex;flex-direction:column;gap:6px}
body.is-locked{overflow:hidden}
.foot{border-top:1px solid rgba(239,237,230,.16);padding:clamp(22px,4vw,42px) clamp(14px,3.6vw,44px) 22px}
.foot__grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:22px;max-width:1560px;margin:0 auto}
.foot__name{font:400 13px/1.35 "Russo One",sans-serif;letter-spacing:.1em;text-transform:uppercase}
.foot__small{font-size:11.5px;line-height:1.7;color:#A8A49A;max-width:34ch}
.foot__h{font:400 9.5px/1.7 "Anonymous Pro",monospace;letter-spacing:.2em;text-transform:uppercase;color:#A8A49A;margin-bottom:9px}
.foot__col a{display:block;font-size:12.5px;padding:3px 0}
.foot__bottom{display:flex;flex-wrap:wrap;gap:12px;justify-content:space-between;margin-top:24px;padding-top:13px;border-top:1px solid rgba(239,237,230,.16);font-size:10.5px;line-height:1.7;color:#A8A49A;max-width:1560px;margin-inline:auto}
@media (max-width:1180px){.nav{display:none}.burger{display:block}}
@media (max-width:1024px){.hero{grid-template-columns:1fr;min-height:0}.hero__media{min-height:clamp(240px,46vh,420px)}.foot__grid{grid-template-columns:1fr 1fr}}
@media (max-width:640px){.head__tel{display:none}.foot__grid{grid-template-columns:1fr}}
"""

HEAD = """<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="__SITE__{slug}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:locale" content="ru_BY">
<meta property="og:url" content="__SITE__{slug}">
<meta name="theme-color" content="#0D0D0C">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Russo+One&family=Anonymous+Pro:wght@400;700&display=swap" rel="stylesheet">
<style>__CRIT__</style>
<link rel="stylesheet" href="assets/css/style.v2.css">
<script type="application/ld+json">{ld}</script>
</head>
<body>
"""

HEADER = """<header class="head">
  <div class="head__row">
    <a class="brand" href="index.html">Сорока<small>Монолит · кладка · кровля · Лида</small></a>
    <nav class="nav" aria-label="Разделы">{nav}</nav>
    <a class="head__tel" href="tel:__PH__">__PHONE__</a>
    <button class="burger" id="burger" type="button" aria-expanded="false" aria-controls="drawer" aria-label="Меню"><span></span><span></span><span></span></button>
  </div>
</header>
"""

DRAWER = """<div class="drawer" id="drawer" hidden>
  <div class="drawer__inner">
    <button class="drawer__close" type="button" id="drawer-close" aria-label="Закрыть меню">×</button>
    <nav class="drawer__nav" aria-label="Мобильная навигация">{drawer_nav}</nav>
    <div class="drawer__meta">
      <a href="tel:__PH__">__PHONE__</a>
      <p>__CITY__, Гродненская область</p>
      <p>Монолит, кладка блоков и кирпича, кровля. Опыт больше 10 лет.</p>
    </div>
  </div>
</div>
"""

FOOT = """</main>
<footer class="foot">
  <div class="foot__grid">
    <div class="foot__col">
      <p class="foot__name">ИП Сорока</p>
      <p class="foot__small">Монолитные работы, кладка блоков и кирпича, кровля. __AREA__. Опыт больше 10 лет.</p>
    </div>
    <div class="foot__col">
      <p class="foot__h">Разделы</p>
      {nav_foot}
    </div>
    <div class="foot__col">
      <p class="foot__h">Связь</p>
      <a href="tel:__PH__">__PHONE__</a>
      <p class="foot__small">__CITY__, Гродненская область</p>
      <p class="foot__small">Звонок или WhatsApp: фото объекта и объём работ.</p>
    </div>
  </div>
  <div class="foot__bottom">
    <p>© <span id="year">2026</span> ИП Сорока. УНП уточняется</p>
    <p>Стоимость — после осмотра объекта. <a href="politika.html">Политика обработки данных</a></p>
  </div>
</footer>
"""

NEXT = """  <section class="next">
    <a class="next__link" href="{href}">
      <span class="next__label">Дальше</span>
      <span class="next__title">{title}</span>
      <span class="next__arrow" aria-hidden="true">→</span>
    </a>
  </section>
"""

LD = {
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "ИП Сорока",
    "description": "Монолитные работы, кладка блоков и кирпича, кровельные работы, строительство домов и хозпостроек с материалом от 750 руб./м². Лида, Гродненская область.",
    "telephone": PHONE_H,
    "address": {"@type": "PostalAddress", "addressLocality": "Лида", "addressRegion": "Гродненская область", "addressCountry": "BY"},
    "areaServed": {"@type": "AdministrativeArea", "name": "Гродненская область"},
    "url": SITE,
}

# ---------- схема разреза ----------

PATTERNS = """<defs>
  <pattern id="p-concrete" width="14" height="14" patternUnits="userSpaceOnUse">
    <rect width="14" height="14" fill="#B9B5AA"/>
    <circle cx="4" cy="5" r="1.1" fill="#8E8A80"/><circle cx="10" cy="9" r="1.3" fill="#8E8A80"/><circle cx="12" cy="3" r=".9" fill="#8E8A80"/>
  </pattern>
  <pattern id="p-brick" width="28" height="14" patternUnits="userSpaceOnUse">
    <rect width="28" height="14" fill="#A8563C"/>
    <path d="M0 0h28M0 14h28M14 0v14" stroke="#C9C5BB" stroke-width="1.6"/>
  </pattern>
  <pattern id="p-block" width="34" height="17" patternUnits="userSpaceOnUse">
    <rect width="34" height="17" fill="#C9C5BB"/>
    <path d="M0 0h34M0 17h34M17 0v17" stroke="#9E9A90" stroke-width="1.4"/>
  </pattern>
  <pattern id="p-insul" width="16" height="16" patternUnits="userSpaceOnUse">
    <rect width="16" height="16" fill="#EFEDE6"/>
    <path d="M0 12 L5 4 L10 12 L15 4" stroke="#B0ACA2" stroke-width="1.2" fill="none"/>
  </pattern>
  <pattern id="p-gravel" width="12" height="12" patternUnits="userSpaceOnUse">
    <rect width="12" height="12" fill="#9C988D"/>
    <circle cx="3" cy="3" r="1.6" fill="#C9C5BB"/><circle cx="8" cy="7" r="1.3" fill="#C9C5BB"/><circle cx="10" cy="2" r="1" fill="#C9C5BB"/>
  </pattern>
  <pattern id="p-memb" width="18" height="10" patternUnits="userSpaceOnUse">
    <rect width="18" height="10" fill="#3A3A37"/>
    <path d="M2 5h13" stroke="#FF3B00" stroke-width="2"/>
  </pattern>
  <pattern id="p-timber" width="20" height="12" patternUnits="userSpaceOnUse">
    <rect width="20" height="12" fill="#7A5A3A"/>
    <path d="M0 4h20M0 9h20" stroke="#5C452C" stroke-width="1"/>
  </pattern>
</defs>"""

PANELS = [
    ("found", "Фундамент", [
        ("Грунт основания", "p-gravel", "Снимаем растительный слой и проверяем, что под подошвой нет насыпного грунта. На слабом основании любая кладка даст трещины.", 70),
        ("Песчано-щебёночная подушка", "p-gravel", "Выравнивает основание и распределяет нагрузку. Укладывается послойно с уплотнением, а не одной кучей.", 52),
        ("Монолитное тело", "p-concrete", "Бетон заливается в опалубку целыми захватами. Рабочие швы стараемся не оставлять в напряжённых местах.", 78),
        ("Армокаркас", "p-timber", "Арматура держит растяжение: бетон сам работает только на сжатие. Важен не только диаметр, но и защитный слой.", 44),
        ("Гидроизоляция и цоколь", "p-memb", "Отсекает капиллярную влагу. Без неё стена тянет воду из грунта, и никакая отделка не спасёт.", 36),
    ]),
    ("wall", "Стена", [
        ("Кладка: блок или кирпич", "p-block", "Ведём по шнуру и уровню с обязательной перевязкой. Без перевязки швов стена теряет прочность, как бы ровно ни выглядела.", 130),
        ("Кладочный шов", "p-brick", "Толщина и заполнение шва влияют и на прочность, и на теплопотери. Пустошовка снаружи недопустима.", 40),
        ("Утеплитель", "p-insul", "Ставим снаружи, чтобы стена оставалась в тёплой зоне и не промерзала по толщине.", 60),
        ("Отделка и облицовка", "p-block", "Защищает утеплитель и кладку от влаги. Крепление считается под вес облицовки.", 44),
        ("Армопояс и перемычки", "p-concrete", "Связывают стену в жёсткое кольцо и держат плиты перекрытия. Экономить на нём нельзя.", 36),
    ]),
    ("roof", "Кровля", [
        ("Кровельное покрытие", "p-memb", "Металл, гибкая черепица или профлист. Уклон определяет и покрытие, и схему вентиляции под ним.", 44),
        ("Обрешётка и контробрешётка", "p-timber", "Контробрешётка даёт вентзазор: конденсат уходит наружу, а не остаётся в утеплителе.", 46),
        ("Гидроизоляционная плёнка", "p-insul", "Защищает утеплитель от подкровельного конденсата и снега, задутого при косом ветре.", 30),
        ("Утеплитель", "p-insul", "Основной барьер тепла. Основная ошибка — разрывы и щели на стыках и у мауэрлата.", 78),
        ("Пароизоляция и обшивка", "p-memb", "Ставится со стороны помещения: не пускает влажный воздух в утеплитель.", 32),
    ]),
]


def panel_svg(pid, bands, active_default=0):
    y = 20
    parts = ['<svg viewBox="0 0 560 320" class="section-svg" role="img" aria-label="Схема разреза: %s">' % pid]
    parts.append(PATTERNS)
    for i, (label, pat, desc, h) in enumerate(bands):
        cls = "seg" + (" is-active" if i == active_default else "")
        parts.append('<rect class="%s" data-i="%d" x="24" y="%d" width="512" height="%d" fill="url(#%s)"/>'
                     % (cls, i, y, h, pat))
        parts.append('<text class="seg-num" x="24" y="%d">%02d</text>' % (y + h / 2 + 4, i + 1))
        y += h
    parts.append('</svg>')
    return "".join(parts)


def panel_list(pid, bands):
    out = ['<ol class="layers" data-panel="%s">' % pid]
    for i, (label, pat, desc, h) in enumerate(bands):
        out.append('<li><button type="button" class="layer%s" data-i="%d">'
                   '<span class="layer__n">%02d</span>'
                   '<span class="layer__t">%s</span>'
                   '<span class="layer__d">%s</span></button></li>'
                   % (" is-active" if i == 0 else "", i, i + 1, label, desc))
    out.append('</ol>')
    return "".join(out)


INDEX = """
<section class="hero">
  <div class="hero__body">
    <p class="ticker">Лида · Гродненская область · опыт больше 10 лет</p>
    <h1 class="hero__h1">
      <span>Монолит</span>
      <span class="out">Кладка</span>
      <span>Кровля</span>
    </h1>
    <div class="hero__bottom">
      <p class="hero__lead">Фундамент, стены из блока и кирпича, крыша. Делаем весь конструктив дома, а не один этап: так стыки между работами не превращаются в проблему. Строим дома и хозпостройки с материалом — от 750 руб./м².</p>
      <div class="hero__actions">
        <a class="btn btn--solid" href="kontakty.html">Вызвать на объект</a>
        <a class="btn" href="tel:__PH__">__PHONE__</a>
      </div>
    </div>
  </div>
  <div class="hero__media">
    <img src="assets/img/mono.jpg" alt="Заливка монолитной конструкции на объекте" width="760" height="974" fetchpriority="high">
  </div>
</section>

<section class="mosaic">
  <div class="wrap">
    <p class="kicker">01 · Что делаем</p>
    <div class="mosaic__grid">
      <a class="tile tile--a" href="uslugi.html#monolit">
        <span class="tile__n">01</span>
        <span class="tile__t">Монолитные работы</span>
        <span class="tile__d">Плиты, армопояса, лестницы, перекрытия. Опалубка, армирование, заливка.</span>
      </a>
      <a class="tile tile--b" href="uslugi.html#found">
        <span class="tile__n">02</span>
        <span class="tile__t">Фундаменты</span>
        <span class="tile__d">Лента и плита под дом или пристройку, с подготовкой и гидроизоляцией.</span>
      </a>
      <a class="tile tile--c" href="uslugi.html#block">
        <span class="tile__n">03</span>
        <span class="tile__t">Кладка блоков</span>
        <span class="tile__d">Газоблок, керамоблок, шлакоблок. Перевязка, армопояс, ровная геометрия.</span>
      </a>
      <a class="tile tile--d" href="uslugi.html#brick">
        <span class="tile__n">04</span>
        <span class="tile__t">Кладка кирпича</span>
        <span class="tile__d">Несущие стены, перегородки, облицовка фасада, арки и сложные узлы.</span>
      </a>
      <a class="tile tile--e" href="uslugi.html#roof">
        <span class="tile__n">05</span>
        <span class="tile__t">Кровельные работы</span>
        <span class="tile__d">Стропильная система, утепление, плёнки, покрытие, водосток.</span>
      </a>
      <a class="tile tile--f" href="uslugi.html#doma">
        <span class="tile__n">06</span>
        <span class="tile__t">Дома и хозпостройки</span>
        <span class="tile__price">от 750 руб./м²</span>
        <span class="tile__d">Строительство с материалом: газоблок, кирпич, перекрытия, кровля. Цена за квадратный метр, а не «по факту».</span>
      </a>
      <div class="tile tile--img">
        <img src="assets/img/brick.jpg" alt="Кладка кирпичной стены с уровнем" width="900" height="782" loading="lazy">
      </div>
    </div>
  </div>
</section>

<section class="cut">
  <div class="wrap">
    <header class="cut__head">
      <div>
        <p class="kicker">02 · Разрез</p>
        <h2 class="h2">Из чего состоит конструкция</h2>
      </div>
      <p class="cut__hint">Три узла: фундамент, стена, кровля. Нажмите на слой, чтобы прочитать, зачем он нужен и что бывает, если его пропустить.</p>
    </header>
    <div class="cut__tabs" role="tablist" aria-label="Узлы конструкции">
      {tabs}
    </div>
    <div class="cut__body">
      <div class="cut__svgs">
        {svgs}
      </div>
      <div class="cut__lists">
        {lists}
      </div>
    </div>
    <p class="cut__note">Схема условная и показывает порядок слоёв, а не проект. Состав пирога и толщины определяются проектом и грунтом на участке.</p>
  </div>
</section>

<section class="claim">
  <div class="wrap claim__in">
    <p class="claim__big">10<span>+</span></p>
    <div>
      <p class="claim__text">лет работаем на объектах в Лиде и районе. За это время сложилось простое правило: сначала конструктив, потом красота. Дом, у которого повело стены, ничем не украсить.</p>
      <ol class="steps">
        <li><span>01</span><b>Смотрим объект</b><p>Грунт, доступ, что уже сделано. По телефону видно далеко не всё.</p></li>
        <li><span>02</span><b>Считаем объём</b><p>Кубы кладки, метры кровли, бетон и арматура — по факту, а не на глаз.</p></li>
        <li><span>03</span><b>Работаем</b><p>Своя бригада, свой инструмент. Этапы сдаём по мере готовности.</p></li>
        <li><span>04</span><b>Отвечаем за шов</b><p>Если через сезон пошла трещина по нашей кладке — приезжаем и разбираемся.</p></li>
      </ol>
    </div>
  </div>
</section>

<section class="cta">
  <div class="wrap cta__in">
    <h2 class="cta__h">Есть проект или только участок?</h2>
    <div class="cta__side">
      <p class="cta__text">Позвоните, опишите, что нужно: фундамент, стены, крыша или всё вместе. Скажем, реально ли уложиться в ваш бюджет, и что делать в первую очередь.</p>
      <div class="cta__actions">
        <a class="btn btn--solid" href="tel:__PH__">__PHONE__</a>
        <a class="btn" href="__WA__" target="_blank" rel="noopener">WhatsApp</a>
      </div>
    </div>
  </div>
</section>
"""

USLUGI = """
<section class="phead">
  <div class="wrap">
    <p class="kicker">Работы и услуги · 01</p>
    <h1 class="h1">Шесть видов работ, <br><span class="out">один конструктив</span></h1>
    <p class="phead__lead">Можно взять отдельный этап, можно весь дом целиком — с материалом, от 750 руб./м². Второе чаще выходит дешевле: не надо дважды разводить бригады и подгонять чужие швы.</p>
  </div>
</section>

<section class="svc" id="monolit">
  <div class="wrap svc__grid">
    <div class="svc__side">
      <p class="svc__n">01</p>
      <h2 class="h2">Монолитные работы</h2>
    </div>
    <div class="svc__body">
      <p>Плиты перекрытия, армопояса, лестницы, монолитные участки стен и крыльцо. Опалубка выставляется по геометрии, армирование — по расчёту, бетон принимаем и уплотняем на месте.</p>
      <p class="svc__note"><b>Что нужно от вас:</b> проект или эскиз с размерами, марка бетона, если уже заказан. Если проекта нет — обсудим конструкцию и предложим решение.</p>
    </div>
    <figure class="svc__fig"><img src="assets/img/mono-wide.jpg" alt="Монолитные работы: бетонирование" width="1300" height="722" loading="lazy"></figure>
  </div>
</section>

<section class="svc svc--flip" id="found">
  <div class="wrap svc__grid">
    <div class="svc__side">
      <p class="svc__n">02</p>
      <h2 class="h2">Фундаменты</h2>
    </div>
    <div class="svc__body">
      <p>Ленточный фундамент и монолитная плита под дом, гараж или пристройку. Разметка, выборка грунта, подушка, опалубка, армирование, заливка, гидроизоляция и обратная засыпка.</p>
      <p class="svc__note"><b>Что нужно от вас:</b> размеры дома или проект, тип грунта, если известен, и подъезд для миксера. На узкий заезд бетон придётся подавать иначе — это влияет на срок.</p>
    </div>
    <figure class="svc__fig"><img src="assets/img/slab.jpg" alt="Монолитная плита фундамента" width="980" height="700" loading="lazy"></figure>
  </div>
</section>

<section class="svc" id="block">
  <div class="wrap svc__grid">
    <div class="svc__side">
      <p class="svc__n">03</p>
      <h2 class="h2">Кладка блоков</h2>
    </div>
    <div class="svc__body">
      <p>Газоблок, керамоблок, шлакоблок. Кладём по шнуру с перевязкой, армируем ряды, выводим геометрию по углам и диагоналям. Армопояс под перекрытие — отдельный этап, который не откладывают.</p>
      <p class="svc__note"><b>Что нужно от вас:</b> проект или план с толщиной стен, материал и его наличие. Если блок ваш — проверим геометрию партии: кривой блок не кладётся ровно.</p>
    </div>
    <figure class="svc__fig"><img src="assets/img/block.jpg" alt="Кладка газобетонных блоков" width="900" height="782" loading="lazy"></figure>
  </div>
</section>

<section class="svc svc--flip" id="brick">
  <div class="wrap svc__grid">
    <div class="svc__side">
      <p class="svc__n">04</p>
      <h2 class="h2">Кладка кирпича</h2>
    </div>
    <div class="svc__body">
      <p>Несущие стены, перегородки, облицовка фасада. Кирпич требует аккуратности в шве: расшивка видна всегда, и на фасаде это главное, что замечают.</p>
      <p class="svc__note"><b>Что нужно от вас:</b> вид кладки и размер кирпича, объём в м² или м³, наличие материала и поддонов.</p>
    </div>
    <figure class="svc__fig"><img src="assets/img/brick.jpg" alt="Кирпичная кладка" width="900" height="782" loading="lazy"></figure>
  </div>
</section>

<section class="svc" id="roof">
  <div class="wrap svc__grid">
    <div class="svc__side">
      <p class="svc__n">05</p>
      <h2 class="h2">Кровельные работы</h2>
    </div>
    <div class="svc__body">
      <p>Стропильная система, обрешётка и контробрешётка, утепление, паро- и гидроизоляция, покрытие, водосток. Утепляем так, чтобы точка росы не оказалась внутри стены или стропила.</p>
      <p class="svc__note"><b>Что нужно от вас:</b> размеры дома и уклон, тип покрытия. Если крыша уже есть — фото стропил и узлов примыкания.</p>
    </div>
    <figure class="svc__fig"><img src="assets/img/roof.jpg" alt="Стропильная система и кровельное покрытие" width="900" height="782" loading="lazy"></figure>
  </div>
</section>

<section class="svc svc--flip" id="doma">
  <div class="wrap svc__grid">
    <div class="svc__side">
      <p class="svc__n">06</p>
      <h2 class="h2">Дома и хозпостройки</h2>
      <p class="svc__price">от 750 <span>руб./м²</span></p>
      <p class="svc__priceNote">с материалом</p>
    </div>
    <div class="svc__body">
      <p>Строим дома и хозяйственные постройки с материалом: газоблок и кирпич, перекрытия, кровля. Цена считается по площади — от 750 руб./м². Одна бригада ведёт объект от фундамента до крыши, поэтому стыки между этапами не становятся вашей проблемой.</p>
      <p>Хозпостройки — отдельная история, которая не требует проекта на 40 листов: гараж, баня, сарай, летняя кухня. Считаем так же, по квадратному метру.</p>
      <p class="svc__note"><b>Что входит в цену:</b> материал и работа по конструктиву. <b>Что уточняем до сметы:</b> проект или эскиз, размеры, этажность, тип кровли и подъезд к участку. Отделка, окна и инженерия считаются отдельно — их можно взять у нас или у своих.</p>
    </div>
    <figure class="svc__fig"><img src="assets/img/house.jpg" alt="Построенный дом из газоблока под кровлей" width="980" height="700" loading="lazy"></figure>
  </div>
</section>

<section class="cta">
  <div class="wrap cta__in">
    <h2 class="cta__h">Не знаете, с чего начать?</h2>
    <div class="cta__side">
      <p class="cta__text">Начните с фундамента: остальное считается после него. Позвоните, и мы скажем, что нужно подготовить на участке.</p>
      <div class="cta__actions">
        <a class="btn btn--solid" href="tel:__PH__">__PHONE__</a>
        <a class="btn" href="kontakty.html">Оставить заявку</a>
      </div>
    </div>
  </div>
</section>
"""

RABOTY = """
<section class="phead">
  <div class="wrap">
    <p class="kicker">Объекты · 02</p>
    <h1 class="h1">Как это выглядит <br><span class="out">на объекте</span></h1>
    <p class="phead__lead">Монолит, кладка и кровля. Фильтр ниже делит снимки по виду работ.</p>
    <div class="chips" id="chips" role="tablist" aria-label="Фильтр объектов">
      <button class="chip is-on" data-cat="all" type="button">Всё</button>
      <button class="chip" data-cat="monolit" type="button">Монолит</button>
      <button class="chip" data-cat="kladka" type="button">Кладка</button>
      <button class="chip" data-cat="krovlya" type="button">Кровля</button>
    </div>
  </div>
</section>

<section class="masonry">
  <div class="wrap">
    <figure class="shot shot--tall" data-cat="monolit">
      <img src="assets/img/mono-wide.jpg" alt="Бетонирование монолитной конструкции" width="1300" height="722" loading="lazy">
      <figcaption><b>Монолит</b><span>заливка захватом</span></figcaption>
    </figure>
    <figure class="shot" data-cat="kladka">
      <img src="assets/img/block.jpg" alt="Кладка блоков на объекте" width="900" height="782" loading="lazy">
      <figcaption><b>Кладка блока</b><span>по шнуру и уровню</span></figcaption>
    </figure>
    <figure class="shot shot--tall" data-cat="kladka">
      <img src="assets/img/brick.jpg" alt="Кирпичная кладка крупным планом" width="900" height="782" loading="lazy">
      <figcaption><b>Кирпич</b><span>расшивка шва</span></figcaption>
    </figure>
    <figure class="shot" data-cat="krovlya">
      <img src="assets/img/roof.jpg" alt="Стропильная система под покрытие" width="900" height="782" loading="lazy">
      <figcaption><b>Кровля</b><span>стропила и обрешётка</span></figcaption>
    </figure>
    <figure class="shot" data-cat="monolit">
      <img src="assets/img/slab.jpg" alt="Монолитная плита" width="980" height="700" loading="lazy">
      <figcaption><b>Плита</b><span>подготовка и заливка</span></figcaption>
    </figure>
    <figure class="shot shot--tall" data-cat="kladka">
      <img src="assets/img/house.jpg" alt="Дом из газоблока в процессе строительства" width="1080" height="720" loading="lazy">
      <figcaption><b>Коробка дома</b><span>стены и фронтон</span></figcaption>
    </figure>
    <figure class="shot" data-cat="krovlya">
      <img src="assets/img/mono.jpg" alt="Работа на объекте" width="760" height="974" loading="lazy">
      <figcaption><b>Объект</b><span>конструктив целиком</span></figcaption>
    </figure>
  </div>
</section>

<section class="cta">
  <div class="wrap cta__in">
    <h2 class="cta__h">Похожий объём?</h2>
    <div class="cta__side">
      <p class="cta__text">Скажите размеры дома и что уже стоит на участке. Этого хватит, чтобы назвать порядок цен.</p>
      <div class="cta__actions">
        <a class="btn btn--solid" href="kontakty.html">Оставить заявку</a>
        <a class="btn" href="tel:__PH__">__PHONE__</a>
      </div>
    </div>
  </div>
</section>
"""

PROIZVODSTVO = """
<section class="phead">
  <div class="wrap">
    <p class="kicker">Бригада · 03</p>
    <h1 class="h1">Больше 10 лет <br><span class="out">в Лиде и районе</span></h1>
    <p class="phead__lead">Небольшая бригада без посредников: тот, кто считает объект, сам на нём и работает. Ниже — принципы, по которым строим, и то, о чём обычно молчат.</p>
  </div>
</section>

<section class="duo">
  <div class="wrap duo__grid">
    <figure class="duo__fig">
      <img src="assets/img/house.jpg" alt="Дом из газоблока в процессе строительства" width="1080" height="720" loading="lazy">
    </figure>
    <div class="duo__copy">
      <h2 class="h2">Почему конструктив целиком</h2>
      <p>Когда фундамент, стены и крышу делает одна бригада, исчезает главная проблема стройки — стык между подрядчиками. Не бывает так, что «фундамент ровный, но стена пошла», потому что фундамент делал один, а стену другой.</p>
      <p>Мы отвечаем за геометрию на всех этапах: фундамент выводим по диагоналям, кладку ведём от углов, кровлю ставим по фактическим размерам коробки, а не по проекту «как должно быть».</p>
      <ul class="ul">
        <li>Своя опалубка, инструмент и леса — не зависим от арендных графиков.</li>
        <li>Материал заказываем вместе с вами: видно, за что платите.</li>
        <li>Этапы сдаём по готовности, а не «в конце всё сразу».</li>
      </ul>
    </div>
  </div>
</section>

<section class="duo duo--flip">
  <div class="wrap duo__grid">
    <div class="duo__copy">
      <h2 class="h2">На чём нельзя экономить</h2>
      <p>Армопояс под перекрытие, перевязка кладки, вентзазор под кровлей и пароизоляция — четыре вещи, которые почти не видны в готовом доме, но именно они определяют, будет ли он стоять ровно и не заплачет ли конденсатом.</p>
      <p>Ещё один частый случай: кривой блок из дешёвой партии. Кладка по нему выходит с перекосом, а исправлять приходится штукатуркой по 5 см. Мы проверяем геометрию материала до начала работ и говорим, если партия не годится.</p>
      <p class="duo__note">Если вы уже купили материал и он лежит на участке — посмотрим и скажем честно, можно ли с ним работать.</p>
    </div>
    <figure class="duo__fig">
      <img src="assets/img/block.jpg" alt="Кладка блоков с уровнем" width="900" height="782" loading="lazy">
    </figure>
  </div>
</section>

<section class="duo">
  <div class="wrap duo__grid">
    <figure class="duo__fig">
      <img src="assets/img/roof.jpg" alt="Кровельные работы" width="900" height="782" loading="lazy">
    </figure>
    <div class="duo__copy">
      <h2 class="h2">Как считаем</h2>
      <p>Объём считаем по факту: кубы кладки, квадраты кровли, кубы бетона, тонны арматуры. По телефону называем порядок цифр, точную сумму — после осмотра объекта или проекта.</p>
      <p>Смета разбита по этапам, чтобы можно было остановиться на любом. Выезд на объект в Лиде и районе обсуждаем отдельно: всё зависит от расстояния и от того, есть ли что смотреть, кроме пустого участка.</p>
      <p class="duo__note">Работаем по договору с фиксированной стоимостью этапа. Предоплата — на материалы, а не на работу.</p>
    </div>
  </div>
</section>

<section class="cta">
  <div class="wrap cta__in">
    <h2 class="cta__h">Звоните, если нужен совет</h2>
    <div class="cta__side">
      <p class="cta__text">Даже если строить будете не с нами — скажем, что видно по вашему объекту. Это дешевле, чем переделывать армирование.</p>
      <div class="cta__actions">
        <a class="btn btn--solid" href="tel:__PH__">__PHONE__</a>
        <a class="btn" href="__WA__" target="_blank" rel="noopener">WhatsApp</a>
      </div>
    </div>
  </div>
</section>
"""

KONTAKTY = """
<section class="phead">
  <div class="wrap">
    <p class="kicker">Контакты · 04</p>
    <h1 class="h1">Позвонить <br><span class="out">или написать</span></h1>
    <p class="phead__lead">Один номер — и телефон, и WhatsApp. Туда можно сразу прислать фото участка или проект.</p>
  </div>
</section>

<section class="contact">
  <div class="wrap contact__grid">
    <div class="contact__side">
      <a class="contact__tel" href="tel:__PH__">__PHONE__</a>
      <p class="contact__note">WhatsApp на этот же номер.</p>
      <dl class="defs">
        <div><dt>Город</dt><dd>__CITY__</dd></div>
        <div><dt>Область</dt><dd>Гродненская</dd></div>
        <div><dt>Опыт</dt><dd>Больше 10 лет</dd></div>
        <div><dt>Работы</dt><dd>Монолит, кладка блоков и кирпича, кровля, дома и хозпостройки с материалом</dd></div>
      </dl>
      <p class="contact__note">Что помогает сразу: размеры дома или проект, что уже сделано на участке, есть ли подъезд для бетона. Для дома с материалом достаточно эскиза и площади — назовём цену за квадратный метр.</p>
    </div>
    <form class="form" id="lead-form" novalidate>
      <p class="form__title">Заявка на работы</p>
      <label for="f-name">Имя</label>
      <input id="f-name" name="name" required autocomplete="name" placeholder="Как к вам обращаться">
      <label for="f-contact">Телефон или мессенджер</label>
      <input id="f-contact" name="contact" required placeholder="+375 …">
      <label for="f-what">Что нужно</label>
      <select id="f-what" name="what">
        <option>Фундамент</option>
        <option>Монолитные работы</option>
        <option>Кладка блоков</option>
        <option>Кладка кирпича</option>
        <option>Кровельные работы</option>
        <option>Всё вместе: дом под конструктив</option>
        <option>Дом или хозпостройка с материалом, от 750 руб./м²</option>
        <option>Пока не знаю, нужен совет</option>
      </select>
      <label for="f-note">Объект, размеры, что уже сделано</label>
      <textarea id="f-note" name="note" rows="3" placeholder="Например: дом 9 × 11, фундамент нужен весной, участок в Лиде"></textarea>
      <button class="btn btn--solid form__btn" type="submit">Собрать заявку</button>
      <p class="form__note">Кнопка соберёт текст и откроет WhatsApp с ним.</p>
      <div class="form__ok" id="form-ok" hidden>
        <p class="form__ok-title">Заявка готова</p>
        <pre id="order-text"></pre>
        <div class="form__ok-actions">
          <a class="btn btn--solid" id="order-send" href="__WA__" target="_blank" rel="noopener">Открыть WhatsApp</a>
          <button class="btn" type="button" id="order-copy">Скопировать</button>
        </div>
      </div>
    </form>
  </div>
</section>
"""

POLITIKA = """
<section class="phead">
  <div class="wrap">
    <p class="kicker">Документ</p>
    <h1 class="h1">Политика обработки <br><span class="out">персональных данных</span></h1>
  </div>
</section>
<section class="textpage">
  <div class="wrap textpage__in">
    <p>Политика описывает, как ИП Сорока (__CITY__, Гродненская область) обрабатывает персональные данные, переданные через сайт.</p>
    <h2>Какие данные</h2>
    <p>Имя, телефон или мессенджер, описание объекта, а также фото и файлы, которые вы присылаете добровольно.</p>
    <h2>Зачем</h2>
    <p>Чтобы ответить на обращение, оценить объём работ и согласовать их выполнение. Данные не передаются третьим лицам и не используются для рассылок.</p>
    <h2>Хранение</h2>
    <p>Переписка и материалы хранятся столько, сколько нужно для выполнения работ и гарантийных обязательств, после чего удаляются.</p>
    <h2>Ваши права</h2>
    <p>Вы можете запросить удаление данных или уточнить, что именно хранится: позвоните по номеру __PHONE__.</p>
    <h2>Технические данные</h2>
    <p>Сайт не использует рекламные трекеры и аналитические cookie. Форма не отправляет данные на сервер: текст заявки формируется в браузере и передаётся вами в мессенджер.</p>
    <p class="textpage__date">Редакция от 6 ноября 2026 года. УНП уточняется.</p>
  </div>
</section>
"""

NEXT_MAP = {
    "index.html": ("uslugi.html", "Работы и услуги"),
    "uslugi.html": ("raboty.html", "Объекты"),
    "raboty.html": ("proizvodstvo.html", "Бригада"),
    "proizvodstvo.html": ("kontakty.html", "Контакты"),
}

PAGES = [
    ("index.html", "Монолит, кладка, кровля, дома с материалом от 750 руб./м² — ИП Сорока, Лида",
     "Монолитные работы, фундаменты, кладка блоков и кирпича, кровля, строительство домов и хозпостроек с материалом от 750 руб./м². Лида и Гродненская область, опыт больше 10 лет.", None),
    ("uslugi.html", "Работы и услуги: монолит, фундамент, кладка, кровля, дома от 750 руб./м² | ИП Сорока, Лида",
     "Шесть видов работ: монолит, фундаменты, кладка газоблока и кирпича, кровля, строительство домов и хозпостроек с материалом от 750 руб./м². Что нужно от заказчика и как считается объём.", USLUGI),
    ("raboty.html", "Объекты: монолит, кладка, кровля | ИП Сорока, Лида",
     "Фотографии работ: бетонирование, кладка блоков и кирпича, стропильная система и кровля.", RABOTY),
    ("proizvodstvo.html", "Бригада: больше 10 лет в Лиде и районе | ИП Сорока",
     "Небольшая бригада без посредников: конструктив целиком, своя опалубка и инструмент, смета по этапам, на чём нельзя экономить.", PROIZVODSTVO),
    ("kontakty.html", "Контакты: +375 (25) 904-85-66, заявка на работы | ИП Сорока",
     "Телефон и WhatsApp +375 (25) 904-85-66. Лида, Гродненская область. Заявка на монолит, кладку, кровлю или дом с материалом.", KONTAKTY),
    ("politika.html", "Политика обработки персональных данных | ИП Сорока",
     "Как обрабатываются данные, переданные через сайт: цели, хранение, права.", POLITIKA),
]


def nav_html(current):
    return "".join('<a href="%s"%s>%s</a>' % (h, ' aria-current="page"' if h == current else "", l) for h, l in NAV)


def build_index():
    tabs, svgs, lists = [], [], []
    for i, (pid, label, bands) in enumerate(PANELS):
        tabs.append('<button class="tab%s" type="button" data-panel="%s" role="tab" aria-selected="%s">%s</button>'
                    % (" is-on" if i == 0 else "", pid, "true" if i == 0 else "false", label))
        svgs.append('<div class="svg-panel%s" data-panel="%s">%s</div>'
                    % ("" if i == 0 else " is-hidden", pid, panel_svg(label, bands)))
        lists.append('<div class="list-panel%s" data-panel="%s">%s</div>'
                     % ("" if i == 0 else " is-hidden", pid, panel_list(pid, bands)))
    return INDEX.replace("{tabs}", "".join(tabs)).replace("{svgs}", "".join(svgs)).replace("{lists}", "".join(lists))


def build():
    for slug, title, desc, body in PAGES:
        page_body = build_index() if body is None else body
        head = (HEAD.replace("{title}", title).replace("{desc}", desc).replace("{slug}", slug)
                    .replace("__CRIT__", CRIT).replace("__SITE__", SITE)
                    .replace("{ld}", json.dumps(LD, ensure_ascii=False)))
        header = HEADER.replace("{nav}", nav_html(slug)).replace("__PH__", PHONE_H).replace("__PHONE__", PHONE)
        nxt = NEXT_MAP.get(slug)
        nextblk = NEXT.replace("{href}", nxt[0]).replace("{title}", nxt[1]) if nxt else ""
        drawer = (DRAWER.replace("{drawer_nav}", nav_html(slug))
                        .replace("__PH__", PHONE_H).replace("__PHONE__", PHONE).replace("__CITY__", CITY))
        foot = (FOOT.replace("{nav_foot}", "".join('<a href="%s">%s</a>' % (h, l) for h, l in NAV))
                    .replace("__PH__", PHONE_H).replace("__PHONE__", PHONE)
                    .replace("__CITY__", CITY).replace("__AREA__", AREA))
        page = (page_body.replace("__PH__", PHONE_H).replace("__PHONE__", PHONE)
                         .replace("__CITY__", CITY).replace("__AREA__", AREA).replace("__WA__", WA))
        html = head + header + page + nextblk + foot + drawer + '<script src="assets/js/main.v2.js" defer></script>\n</body>\n</html>\n'
        open(slug, "w", encoding="utf-8").write(html)
        print("built", slug, len(html))

    urls = "\n".join('  <url><loc>%s%s</loc><priority>%s</priority></url>'
                     % (SITE, s, "1.0" if s == "index.html" else "0.7") for s, *_ in PAGES)
    open("sitemap.xml", "w", encoding="utf-8").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s\n</urlset>\n' % urls)
    open("robots.txt", "w", encoding="utf-8").write("User-agent: *\nAllow: /\nSitemap: %ssitemap.xml\n" % SITE)


if __name__ == "__main__":
    build()
