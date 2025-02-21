---
title: Portfolio
layout: page
---
### My Projects
<ul>
  {% for project in site.portfolio %}
    <li><a href="{{ project.url }}">{{ project.title }}</a></li>
  {% endfor %}
</ul>