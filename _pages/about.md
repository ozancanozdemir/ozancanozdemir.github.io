---
permalink: /
title: "Ozancan Ozdemir"
excerpt: "PhD Candidate • ML for Sequential Data • Public Writing"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<img src="https://upload.wikimedia.org/wikipedia/commons/5/5d/Gezicht_op_Ankara_Rijksmuseum_SK-A-2055.jpeg" width="700" height="250" alt="View of Ankara from the Rijksmuseum">

# Hi — I’m Ozancan.

I’m a **PhD Candidate at the University of Groningen (Bernoulli Institute)**. My research sits at the intersection of **machine learning**, **deep learning**, and **sequential data**—with a particular focus on **time series**. I care about how models behave when the data are messy, the stakes are real, and the world changes: **forecasting**, **representation learning**, and **robust evaluation** are recurring themes in my work.

Alongside academia, I write and speak about **AI as a social and institutional force**—how it reshapes education, media, and democratic life, and how metrics and incentives quietly steer what we optimize. I like bridging technical ideas with public reasoning: less “AI hype,” more clarity about **trade-offs, failure modes, and what should be measured**.

<div style="display:flex; gap:10px; flex-wrap:wrap; margin: 1rem 0 1.2rem 0;">
  <a href="/publications/" style="padding:10px 14px; border:1px solid #ddd; border-radius:999px; text-decoration:none;">Publications</a>
  <a href="/talks/" style="padding:10px 14px; border:1px solid #ddd; border-radius:999px; text-decoration:none;">Talks</a>
  <a href="https://ozancanozdemir.github.io/cv/" style="padding:10px 14px; border:1px solid #ddd; border-radius:999px; text-decoration:none;">CV</a>
  <a href="https://t24.com.tr/yazarlar/ozancan-ozdemir" style="padding:10px 14px; border:1px solid #ddd; border-radius:999px; text-decoration:none;">T24</a>
  <a href="https://substack.com/@ozancanozdemir" style="padding:10px 14px; border:1px solid #ddd; border-radius:999px; text-decoration:none;">Substack</a>
  <a href="https://x.com/OzancanOzdemir" style="padding:10px 14px; border:1px solid #ddd; border-radius:999px; text-decoration:none;">X</a>
</div>

---

## Latest writing (T24)
{% assign t24 = site.data.t24 %}
{% if t24 and t24.items %}
<ul>
  {% for item in t24.items %}
    <li><a href="{{ item.url }}">{{ item.title }}</a></li>
  {% endfor %}
</ul>
{% else %}
<p>not loaded</p>
{% endif %}
---

## Latest posts (Substack)
{% assign ss = site.data.substack %}
{% if ss and ss.items %}
<ul>
  {% for item in ss.items %}
    <li><a href="{{ item.url }}">{{ item.title }}</a></li>
  {% endfor %}
</ul>
{% endif %}
---

## What I’m currently focused on

- **ML for sequential data:** time series forecasting, sequence modeling, representation learning  
- **Evaluation in the wild:** distribution shift, robustness, metric design  
- **Public scholarship:** AI literacy, governance, and the politics of optimization


---

## Recent talks

A few highlights from recent presentations (full list on the talks page):

- **APPIS 2026 (Las Palmas)** — *Predicting Excess Returns: A Comparative ML Study with Novel Feature Selection and Fundamental Indicators*  
- **AMALEA 2025 (Cetraro)** — *Predicting Stock Excess Returns Using Fundamental Analysis and Machine Learning*  
- **APPIS 2025** — *A Comprehensive Review of Fundamental Indicators and ML Techniques for Stock Market Forecasting*

➡️ See all talks: **/talks/**

---

## Short bio (for speaker pages)

**Ozancan Ozdemir** is a PhD Candidate at the University of Groningen (Bernoulli Institute). His work focuses on machine learning for sequential data—especially time series forecasting and robust evaluation. He also writes and speaks about AI’s societal impacts, with an emphasis on metrics, incentives, and governance.

---
## Find me

- **T24:** https://t24.com.tr/yazarlar/ozancan-ozdemir  
- **Substack:** https://substack.com/@ozancanozdemir  
- **Talks:** /talks/  
- **Publications:** /publications/  

<a class="twitter-timeline" data-width="420" data-height="320" data-theme="light" href="https://twitter.com/OzancanOzdemir?ref_src=twsrc%5Etfw">Tweets by OzancanOzdemir</a>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

<style>
  .latest-list { margin-top: .6rem; }
  .latest-list li { margin: .35rem 0; line-height: 1.35; }
  .latest-meta { opacity: .7; font-size: .85em; margin-top: .4rem; }
</style>
