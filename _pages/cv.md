---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}
<p>
  <a href="{{ '/files/cv.pdf' | relative_url }}" download>Download CV (PDF)</a>
</p>
## 🎓 Education

- **Master in Mathematics of Randomness (Statistics and Machine Learning)**, Université Paris Saclay — *2020–2021*
- **Major in Mathematics and Data Sciences**, CentraleSupélec — *2017–2021*
- **Bachelor in Fundamental Physics**, Université Paris Sud — *2017–2018*
- **Preparatory Classes MPSI/MP\***, CPGE Chateaubriand Rennes — *2015–2017*

---

## 📚 PhD Thesis

**Title:** Distributed control of flexible loads on the power grid  
**Advisor:** Ana Bušić  

This thesis consists in providing new flexibility resources which are particularly crucial to integrate renewable energies into the power grid. The procedure relies on new smart technologies allowing for automatic control of devices. The objective is to control a great amount of devices to provide services to the system (load shaping or ancillary services) while: - maintaining the quality of service for the users; - minimizing communications between controllable devices and the central controller. The approach combines the techniques from the theory of **controlled Markov processes**, **mean-field theory**, **optimal transport** and **automatic control**.

---

## 👨‍🏫 Teaching Experience

  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

---

## 📝 Publications

  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

---
## 💬 Talks

  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html  %}
  {% endfor %}</ul>

---

## 🤝 Community Involvement

- **Scouting:** BAFA & BAFD training (animation, leadership, logistics, finance)
- **Secours Populaire Français:** food distribution, children’s activities, fundraising

---
