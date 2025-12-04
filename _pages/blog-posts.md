---
layout: archive          # veya mevcut temanızda çalışan başka bir layout
title:  "Blog Posts"
permalink: /blog-posts/
author_profile: true
entries_layout: list
---


<p align="right">
  <a href="/blog-feed.xml" class="btn btn--warning btn--small">
    <i class="fas fa-rss"></i> RSS Abone Ol
  </a>
</p>

<div class="grid__wrapper">
  {% assign all_posts = site.posts | sort: "date" | reverse %}
  
  {% for post in all_posts %}
    {% comment %} R etiketli değilse göster {% endcomment %}
    {% unless post.tags contains 'r' %}
      {% include archive-single.html %}
    {% endunless %}
  {% endfor %}
</div>

