---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{https://scholar.google.com.tr/citations?user=JnC6fesAAAAJ&hl=tr}}">my Google Scholar profile</a>.</u>
{% endif %}
author.googlescholar
{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
