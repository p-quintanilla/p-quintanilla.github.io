---
layout: archive
permalink: /publications/
author_profile: true
---

![](/_pages/4.png)

I am the corresponding author of 8 out of 10 of my papers:

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{[author.googlescholar](https://scholar.google.com/citations?user=1dp-SB4AAAAJ&hl=en)}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}


_You can also find my articles on [Google Scholar](https://scholar.google.com/citations?user=1dp-SB4AAAAJ&hl=en)._

## Submitted conference papers:

1. Quintanilla P, and  Gonzalez R.A. _Grey-box Identification for Mineral Processing: Recursive Parameter Estimation of a Dynamic Flotation Model_. Submitted in November 2023 for the European Control Conference 2024.
   
1. Quintanilla P, Navia D, Neethling S.J, Brito-Parada P.R. _Centralised economic model predictive control for froth flotation with experimental validation_. Submitted in November 2023 for the European Symposium on Computer-Aided Process Engineering 2024.
