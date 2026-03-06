---
layout: default
title: Archive
---

<h1>Research Archive</h1>

{% assign posts_by_year = site.posts | group_by_exp: 'post', 'post.date | date: "%Y"' %}

{% for year in posts_by_year %}
<div class="archive-year">
    <h3>{{ year.name }}</h3>
    
    {% assign posts_by_month = year.items | group_by_exp: 'post', 'post.date | date: "%B"' %}
    
    {% for month in posts_by_month %}
    <div class="archive-month">
        <h4>{{ month.name }}</h4>
        <ul>
            {% for post in month.items %}
            <li>
                <span class="post-date">{{ post.date | date: '%d' }}</span> — 
                <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
                {% if post.topic %}
                <span class="topic">{{ post.topic }}</span>
                {% endif %}
            </li>
            {% endfor %}
        </ul>
    </div>
    {% endfor %}
</div>
{% endfor %}
