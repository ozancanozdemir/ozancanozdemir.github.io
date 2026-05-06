---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% include base_path %}

<div class="pub-hero">
  <div class="pub-kicker">Research · Public Scholarship · Essays</div>
  <h1>Publications</h1>
  <p>
    My work brings together machine learning, time series analysis, stock market forecasting,
    public-facing data writing, and broader reflections on society, politics, and technology.
  </p>

  <div class="pub-actions">
    {% if author.googlescholar %}
      <a class="pub-btn primary" href="{{ author.googlescholar }}">Google Scholar</a>
    {% endif %}
    <a class="pub-btn" href="https://medium.com/@ozancanozdemir">Medium</a>
    <a class="pub-btn" href="https://t24.com.tr/yazarlar/ozancan-ozdemir">T24 Column</a>
  </div>
</div>

---

## Academic Publications

<div class="section-note">
  Peer-reviewed papers, conference publications, and academic work related to machine learning,
  forecasting, time series, and applied statistical modeling.
</div>

<div class="academic-list">
  {% for post in site.publications reversed %}
    {% include archive-single.html %}
  {% endfor %}
</div>

---

## Popular Science & Public Writing

<div class="section-note">
  Selected pieces written for a broader audience, mostly in Turkish, combining data, statistics,
  politics, and public reasoning.
</div>

<div class="pub-grid">

  <a class="pub-card" href="https://sarkac.org/2021/09/covid-19-asilari-ve-simpson-paradoksu/">
    <div class="pub-card-top">
      <span class="tag">Popular Science</span>
      <span class="date">Sep 2021</span>
    </div>
    <h3>COVID-19 Aşıları ve Simpson Paradoksu</h3>
    <p>
      A public-facing explanation of Simpson’s paradox through COVID-19 vaccination data.
    </p>
    <div class="source">Sarkaç →</div>
  </a>

  <a class="pub-card" href="https://ayrancim.org.tr/?p=9234">
    <div class="pub-card-top">
      <span class="tag">Data Essay</span>
      <span class="date">Sep 2021</span>
    </div>
    <h3>Yoksullaşıyoruz</h3>
    <p>
      A data-informed reflection on economic hardship, inequality, and everyday life.
    </p>
    <div class="source">Ayrancım Gazetesi →</div>
  </a>

  <a class="pub-card" href="https://ayrancim.org.tr/?p=8915">
    <div class="pub-card-top">
      <span class="tag">Politics</span>
      <span class="date">Apr 2021</span>
    </div>
    <h3>Ankara Siyasetinde Kadının Adı Yok</h3>
    <p>
      An article on gender representation and the absence of women in Ankara politics.
    </p>
    <div class="source">Ayrancım Gazetesi →</div>
  </a>

  <a class="pub-card" href="https://ayrancim.org.tr/?p=8626">
    <div class="pub-card-top">
      <span class="tag">Urban Data</span>
      <span class="date">Jan 2021</span>
    </div>
    <h3>2020’yi Geride Bırakırken: Verilerle Ankara</h3>
    <p>
      A data-based look at Ankara at the end of 2020.
    </p>
    <div class="source">Ayrancım Gazetesi →</div>
  </a>

</div>

---

## Stories

<div class="section-note">
  Earlier literary pieces and short stories — a different side of my writing, shaped by memory,
  place, and personal reflection.
</div>

<div class="story-grid">

  <a class="story-card" href="https://spektif.wordpress.com/2019/08/16/babamin-defteri/">
    <div class="story-mark">Story</div>
    <h3>Babamın Defteri</h3>
    <p>A short story on memory, family, and traces left behind.</p>
  </a>

  <a class="story-card" href="https://spektif.wordpress.com/2018/11/05/hafiza/">
    <div class="story-mark">Story</div>
    <h3>Hafıza</h3>
    <p>A literary reflection on memory and the persistence of the past.</p>
  </a>

  <a class="story-card" href="https://spektif.wordpress.com/2017/02/26/bir-ruya/">
    <div class="story-mark">Story</div>
    <h3>Bir Rüya</h3>
    <p>A short fictional piece with a dreamlike atmosphere.</p>
  </a>

</div>

<style>
  /* Hero */
  .pub-hero {
    border-radius: 20px;
    padding: 28px;
    margin-bottom: 1.4rem;
    background:
      radial-gradient(circle at top left, rgba(45, 96, 255, .16), transparent 34%),
      radial-gradient(circle at bottom right, rgba(0, 0, 0, .08), transparent 30%),
      linear-gradient(135deg, rgba(255,255,255,.96), rgba(248,248,248,.86));
    border: 1px solid rgba(0,0,0,.08);
  }

  .pub-kicker {
    font-size: .9rem;
    letter-spacing: .3px;
    text-transform: uppercase;
    font-weight: 800;
    opacity: .68;
    margin-bottom: .35rem;
  }

  .pub-hero h1 {
    margin: 0;
    font-size: 2.25rem;
    line-height: 1.1;
  }

  .pub-hero p {
    max-width: 860px;
    margin: .75rem 0 0 0;
    font-size: 1.02rem;
    line-height: 1.55;
    opacity: .82;
  }

  .pub-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 1.1rem;
  }

  .pub-btn {
    display: inline-block;
    padding: 10px 14px;
    border-radius: 999px;
    text-decoration: none;
    border: 1px solid rgba(0,0,0,.12);
    background: rgba(255,255,255,.78);
    font-weight: 700;
  }

  .pub-btn.primary {
    background: rgba(0,0,0,.88);
    color: #fff;
    border-color: rgba(0,0,0,.88);
  }

  .pub-btn:hover {
    transform: translateY(-1px);
    transition: transform .12s ease;
  }

  /* Section note */
  .section-note {
    max-width: 850px;
    margin: -.25rem 0 1rem 0;
    padding: 12px 14px;
    border-left: 4px solid rgba(0,0,0,.18);
    background: rgba(0,0,0,.025);
    border-radius: 0 12px 12px 0;
    color: rgba(0,0,0,.72);
    line-height: 1.5;
  }

  /* Academic list wrapper */
  .academic-list {
    margin-top: .5rem;
  }

  .academic-list .archive__item {
    padding: 14px 16px;
    border: 1px solid rgba(0,0,0,.08);
    border-radius: 14px;
    margin-bottom: 12px;
    background: rgba(255,255,255,.78);
  }

  .academic-list .archive__item-title {
    margin-top: 0;
  }

  /* Public writing cards */
  .pub-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 14px;
    margin-top: 1rem;
  }

  .pub-card {
    display: block;
    text-decoration: none;
    padding: 16px;
    border-radius: 18px;
    border: 1px solid rgba(0,0,0,.10);
    background:
      linear-gradient(135deg, rgba(255,255,255,.95), rgba(250,250,250,.78));
  }

  .pub-card:hover {
    transform: translateY(-2px);
    transition: transform .14s ease;
  }

  .pub-card-top {
    display: flex;
    justify-content: space-between;
    gap: 8px;
    align-items: center;
    margin-bottom: 10px;
  }

  .tag {
    display: inline-block;
    padding: 5px 9px;
    border-radius: 999px;
    background: rgba(0,0,0,.06);
    color: rgba(0,0,0,.78);
    font-size: .82rem;
    font-weight: 800;
  }

  .date {
    font-size: .85rem;
    opacity: .62;
  }

  .pub-card h3 {
    margin: 0 0 7px 0;
    line-height: 1.25;
    color: rgba(0,0,0,.9);
  }

  .pub-card p {
    margin: 0;
    line-height: 1.45;
    color: rgba(0,0,0,.68);
  }

  .source {
    margin-top: 12px;
    font-weight: 800;
    color: rgba(0,0,0,.84);
  }

  /* Stories */
  .story-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 14px;
    margin-top: 1rem;
  }

  .story-card {
    display: block;
    text-decoration: none;
    padding: 16px;
    border-radius: 18px;
    border: 1px solid rgba(0,0,0,.10);
    background:
      radial-gradient(circle at top right, rgba(0,0,0,.07), transparent 35%),
      rgba(255,255,255,.82);
  }

  .story-card:hover {
    transform: translateY(-2px);
    transition: transform .14s ease;
  }

  .story-mark {
    display: inline-block;
    font-size: .78rem;
    text-transform: uppercase;
    letter-spacing: .3px;
    font-weight: 900;
    opacity: .62;
    margin-bottom: 9px;
  }

  .story-card h3 {
    margin: 0 0 7px 0;
    color: rgba(0,0,0,.9);
  }

  .story-card p {
    margin: 0;
    color: rgba(0,0,0,.68);
    line-height: 1.45;
  }

  /* Responsive */
  @media (max-width: 980px) {
    .pub-grid,
    .story-grid {
      grid-template-columns: 1fr;
    }

    .pub-hero {
      padding: 22px;
    }

    .pub-hero h1 {
      font-size: 2rem;
    }
  }
</style>
