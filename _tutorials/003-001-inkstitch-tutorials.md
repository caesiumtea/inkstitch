---
title: "Ink/Stitch Tutorials"
permalink: /tutorials/
excerpt: ""
read_time: false
classes: wide
---
{% comment %}This is the list of keys you can set to categorize tutorials, use slugified version in tutorial file: f.e. Tutorial Type would become tutorial-type{% endcomment %}
{% assign tutorial_cats = 'Tutorial Type*Stitch Type*Techniques*User Level' | split: '*' %}

{% include display_tutorials tutorial_cats=tutorial_cats %}