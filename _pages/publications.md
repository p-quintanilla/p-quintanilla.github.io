---
layout: archive
permalink: /publications/
author_profile: true
---

![](/_pages/4.png)

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{[author.googlescholar](https://scholar.google.com/citations?user=1dp-SB4AAAAJ&hl=en)}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}


_You can also find my articles on [Google Scholar](https://scholar.google.com/citations?user=1dp-SB4AAAAJ&hl=en)._

