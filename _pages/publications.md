---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% include base_path %}

<div class="pub-intro">

  <p class="pub-lead">
    My publications and essays reflect my work across machine learning, time series analysis,
    stock market forecasting, public-facing data writing, and broader questions around technology,
    politics, and society.
  </p>

  <div class="research-snapshot">
    <div class="snapshot-item">
      <span class="snapshot-number">XX</span>
      <span class="snapshot-label">Citations</span>
    </div>
    <div class="snapshot-item">
      <span class="snapshot-number">X</span>
      <span class="snapshot-label">h-index</span>
    </div>
    <div class="snapshot-item">
      <span class="snapshot-number">X</span>
      <span class="snapshot-label">i10-index</span>
    </div>
  </div>

  <div class="metric-note">
    Citation metrics are shown according to Google Scholar and updated manually.
  </div>

  <div class="pub-links">
    {% if author.googlescholar %}
      <a href="{{ author.googlescholar }}">Google Scholar</a>
    {% endif %}
    <a href="https://ozancanozdemir.github.io/cv/">CV</a>
    <a href="https://medium.com/@ozancanozdemir">Medium</a>
    <a href="https://t24.com.tr/yazarlar/ozancan-ozdemir">T24</a>
    <a href="https://substack.com/@ozancanozdemir">Substack</a>
  </div>

</div>

## Academic publications

<div class="pub-section-note">
  Peer-reviewed articles, conference papers, and academic work related to machine learning,
  forecasting, time series, stock market prediction, and applied statistical modeling.
</div>

<div class="publication-list">

  {% for post in site.publications reversed %}
    <div class="publication-row">

      <div class="publication-tile {{ post.topic_class | default: 'pub' }}">
        {{ post.topic_code | default: 'PUB' }}
      </div>

      <div class="publication-main">

        <h3>
          <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
        </h3>

        <div class="publication-meta">
          {% if post.venue %}{{ post.venue }}{% endif %}
          {% if post.date %} · {{ post.date | date: "%Y" }}{% endif %}
          {% if post.pub_type %} · {{ post.pub_type }}{% endif %}
        </div>

        {% if post.short_summary %}
          <p>{{ post.short_summary }}</p>
        {% elsif post.excerpt %}
          <p>{{ post.excerpt }}</p>
        {% endif %}

        {% if post.tags %}
          <div class="publication-tags">
            {% for tag in post.tags %}
              <span>{{ tag }}</span>
            {% endfor %}
          </div>
        {% endif %}

        <div class="publication-actions">
          <a href="{{ post.url | relative_url }}">Details</a>
          {% if post.paperurl %}
            <a href="{{ post.paperurl }}">Paper</a>
          {% endif %}
        </div>

      </div>
    </div>
  {% endfor %}

</div>

## Public writing

<div class="pub-section-note">
  Selected popular science and public-facing articles, mostly written in Turkish.
</div>

<div class="simple-list">

  <div class="simple-item">
    <div class="simple-title">
      <a href="https://sarkac.org/2021/09/covid-19-asilari-ve-simpson-paradoksu/">
        COVID-19 Aşıları ve Simpson Paradoksu
      </a>
    </div>
    <div class="simple-meta">Sarkaç · 4 September 2021 · Popular science</div>
  </div>

  <div class="simple-item">
    <div class="simple-title">
      <a href="https://ayrancim.org.tr/?p=9234">Yoksullaşıyoruz</a>
    </div>
    <div class="simple-meta">Ayrancım Gazetesi · 16 September 2021 · Data essay</div>
  </div>

  <div class="simple-item">
    <div class="simple-title">
      <a href="https://ayrancim.org.tr/?p=8915">Ankara Siyasetinde Kadının Adı Yok</a>
    </div>
    <div class="simple-meta">Ayrancım Gazetesi · April 2021 · Politics and representation</div>
  </div>

  <div class="simple-item">
    <div class="simple-title">
      <a href="https://ayrancim.org.tr/?p=8626">2020’yi Geride Bırakırken: Verilerle Ankara</a>
    </div>
    <div class="simple-meta">Ayrancım Gazetesi · January 2021 · Urban data</div>
  </div>

</div>

## Stories

<div class="pub-section-note">
  Earlier literary pieces and short stories.
</div>

<div class="simple-list">

  <div class="simple-item">
    <div class="simple-title">
      <a href="https://spektif.wordpress.com/2019/08/16/babamin-defteri/">Babamın Defteri</a>
    </div>
    <div class="simple-meta">Short story · 2019</div>
  </div>

  <div class="simple-item">
    <div class="simple-title">
      <a href="https://spektif.wordpress.com/2018/11/05/hafiza/">Hafıza</a>
    </div>
    <div class="simple-meta">Short story · 2018</div>
  </div>

  <div class="simple-item">
    <div class="simple-title">
      <a href="https://spektif.wordpress.com/2017/02/26/bir-ruya/">Bir Rüya</a>
    </div>
    <div class="simple-meta">Short story · 2017</div>
  </div>

</div>

<style>
  .pub-intro {
    margin: 0 0 2rem 0;
    padding-bottom: 1.4rem;
    border-bottom: 1px solid rgba(0,0,0,.10);
  }

  .pub-lead {
    max-width: 820px;
    margin: 0 0 1.15rem 0;
    font-size: 1.02rem;
    line-height: 1.65;
    color: rgba(0,0,0,.76);
  }

  .research-snapshot {
    display: flex;
    flex-wrap: wrap;
    gap: 1.6rem;
    margin: 1.1rem 0 .35rem 0;
  }

  .snapshot-item {
    min-width: 90px;
  }

  .snapshot-number {
    display: block;
    font-size: 1.55rem;
    line-height: 1.1;
    font-weight: 700;
    letter-spacing: -0.02em;
    color: rgba(0,0,0,.88);
  }

  .snapshot-label {
    display: block;
    margin-top: .25rem;
    font-size: .82rem;
    color: rgba(0,0,0,.58);
  }

  .metric-note {
    margin-top: .4rem;
    font-size: .82rem;
    color: rgba(0,0,0,.52);
  }

  .pub-links {
    display: flex;
    flex-wrap: wrap;
    gap: .55rem .9rem;
    margin-top: 1rem;
    font-size: .92rem;
  }

  .pub-links a {
    text-decoration: none;
    border-bottom: 1px solid rgba(0,0,0,.25);
    color: rgba(0,0,0,.78);
  }

  .pub-links a:hover {
    color: rgba(0,0,0,1);
    border-bottom-color: rgba(0,0,0,.65);
  }

  .pub-section-note {
    max-width: 760px;
    margin: -.3rem 0 1rem 0;
    font-size: .92rem;
    line-height: 1.55;
    color: rgba(0,0,0,.60);
  }

  .publication-list {
    margin: .5rem 0 2.2rem 0;
  }

  .publication-row {
    display: grid;
    grid-template-columns: 64px 1fr;
    gap: 14px;
    padding: 1.05rem 0;
    border-bottom: 1px solid rgba(0,0,0,.08);
  }

  .publication-row:first-child {
    border-top: 1px solid rgba(0,0,0,.08);
  }

  .publication-tile {
    width: 56px;
    height: 56px;
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 800;
    font-size: .78rem;
    letter-spacing: .04em;
    color: rgba(0,0,0,.72);
    border: 1px solid rgba(0,0,0,.10);
    background: rgba(0,0,0,.035);
  }

  .publication-tile.env {
    background: rgba(62, 125, 91, .10);
  }

  .publication-tile.fin {
    background: rgba(70, 90, 140, .10);
  }

  .publication-tile.ml {
    background: rgba(120, 90, 160, .10);
  }

  .publication-tile.ts {
    background: rgba(90, 120, 150, .10);
  }

  .publication-tile.stat {
    background: rgba(150, 110, 70, .10);
  }

  .publication-tile.ai {
    background: rgba(80, 110, 170, .10);
  }

  .publication-main h3 {
    margin: 0;
    font-size: 1.02rem;
    line-height: 1.35;
  }

  .publication-main h3 a {
    text-decoration: none;
  }

  .publication-main h3 a:hover {
    text-decoration: underline;
    text-underline-offset: 3px;
  }

  .publication-meta {
    margin-top: .25rem;
    font-size: .86rem;
    color: rgba(0,0,0,.55);
  }

  .publication-main p {
    margin: .45rem 0 0 0;
    font-size: .92rem;
    line-height: 1.5;
    color: rgba(0,0,0,.68);
  }

  .publication-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-top: .55rem;
  }

  .publication-tags span {
    display: inline-block;
    padding: 4px 8px;
    border-radius: 999px;
    font-size: .78rem;
    background: rgba(0,0,0,.04);
    color: rgba(0,0,0,.62);
  }

  .publication-actions {
    display: flex;
    flex-wrap: wrap;
    gap: .7rem;
    margin-top: .6rem;
    font-size: .86rem;
  }

  .publication-actions a {
    text-decoration: none;
    border-bottom: 1px solid rgba(0,0,0,.22);
  }

  .publication-actions a:hover {
    border-bottom-color: rgba(0,0,0,.65);
  }

  .simple-list {
    margin: .5rem 0 2.2rem 0;
    border-top: 1px solid rgba(0,0,0,.08);
  }

  .simple-item {
    padding: .9rem 0;
    border-bottom: 1px solid rgba(0,0,0,.08);
  }

  .simple-title {
    font-size: 1rem;
    line-height: 1.35;
    font-weight: 600;
  }

  .simple-title a {
    text-decoration: none;
  }

  .simple-title a:hover {
    text-decoration: underline;
    text-underline-offset: 3px;
  }

  .simple-meta {
    margin-top: .25rem;
    font-size: .86rem;
    color: rgba(0,0,0,.55);
  }

  @media (max-width: 640px) {
    .publication-row {
      grid-template-columns: 1fr;
    }
.publication-tile.clim {
  background: rgba(73, 130, 120, .10);
}
    .publication-tile {
      width: fit-content;
      height: auto;
      padding: 6px 10px;
      border-radius: 999px;
    }
    .publication-tile.edu {
  background: rgba(110, 130, 80, .10);
}
    .publication-tile.viz {
  background: rgba(170, 115, 55, .10);
}
    .publication-tile.fcst {
  background: rgba(95, 120, 170, .10);
}
    .publication-tile.clim {
  background: rgba(73, 130, 120, .10);
}
    .publication-tile.ai {
  background: rgba(80, 110, 170, .10);
}.publication-tile.soc {
  background: rgba(120, 95, 140, .10);
}

    .research-snapshot {
      gap: 1.1rem;
    }

    .snapshot-number {
      font-size: 1.35rem;
    }
  }
</style>
