---
layout: archive          # veya mevcut temanızda çalışan başka bir layout
title:  "Blog Posts"
permalink: /blog-posts/
author_profile: true
entries_layout: list
---

{% comment %} Tüm postları tarihe göre tersten sırala {% endcomment %}
{% assign all_posts = site.posts.blog | sort: "date" | reverse %}

{% for post in all_posts %}
  {% include archive-single.html %}
{% endfor %}

<p>
  <a href="/blog-feed.xml" class="btn btn--warning btn--small">
    <i class="fas fa-rss"></i> RSS Abone Ol
  </a>
</p>

