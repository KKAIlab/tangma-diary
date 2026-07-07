---
layout: page
title: 全部文章
permalink: /archive/
---

{% assign postsByYear = site.posts | group_by_exp: "post", "post.date | date: '%Y'" %}
{% for year in postsByYear %}
<h2 class="archive-year">{{ year.name }} 年</h2>
<ul class="post-list">
  {% for post in year.items %}
  <li><a href="{{ post.url | relative_url }}">{{ post.title }}</a><span class="post-list-date">{{ post.date | date: "%m-%d" }}</span></li>
  {% endfor %}
</ul>
{% endfor %}
