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
<ul class="latest-list">
  {% for item in t24.items %}
    <li><a href="{{ item.url }}">{{ item.title }}</a></li>
  {% endfor %}
</ul>
<div class="latest-meta">Updated: {{ t24.fetched_at }}</div>
{% else %}
<p><em>T24 list is not available yet.</em></p>
{% endif %}

---

## Latest posts (Substack)

{% assign ss = site.data.substack %}
{% if ss and ss.items %}
<ul class="latest-list">
  {% for item in ss.items %}
    <li>
      <a href="{{ item.url }}">{{ item.title }}</a>
      {% if item.date %}<small> — {{ item.date }}</small>{% endif %}
    </li>
  {% endfor %}
</ul>
<div class="latest-meta">Updated: {{ ss.fetched_at }}</div>
{% else %}
<p><em>Substack list is not available yet.</em></p>
{% endif %}

---

## What I’m currently focused on

- **ML for sequential data:** time series forecasting, sequence modeling, representation learning  
- **Evaluation in the wild:** distribution shift, robustness, metric design  
- **Public scholarship:** AI literacy, governance, and the politics of optimization

<style>
  .latest-list { margin-top: .6rem; }
  .latest-list li { margin: .35rem 0; line-height: 1.35; }
  .latest-meta { opacity: .7; font-size: .85em; margin-top: .4rem; }
</style>
