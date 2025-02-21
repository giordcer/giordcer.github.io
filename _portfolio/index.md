---
title: Portfolio
layout: page
---
<h1>Portfolio</h1>
<ul>
  {% for project in site.portfolio %}
    <li><a href="{{ project.url }}">{{ project.title }}</a></li>
  {% endfor %}
</ul>