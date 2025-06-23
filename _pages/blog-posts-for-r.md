---
layout: archive          # veya mevcut temanızda çalışan başka bir layout
title:  "Blog Posts for R"
permalink: /blog-posts-for-r/
author_profile: true
entries_layout: list
---

{% comment %}
Bu sayfa, tags: [r] içeren tüm yazıları manual Liquid döngüyle listeler.
Temada “layout: tag” eksik olsa bile çalışır.
{% endcomment %}

{% assign r_posts = site.tags.r | sort: "date" | reverse %}
{% for post in r_posts %}
  {% include archive-single.html %}
{% endfor %}
