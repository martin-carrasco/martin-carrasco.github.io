---
layout: about
title: about
permalink: /
subtitle: ELLIS PhD @ AIDOS

profile:
  align: right
  image: prof_pic.jpeg
  image_circular: false # crops the image to make it circular

news: true # includes a list of news items
selected_papers: false # includes a list of papers marked as "selected={true}"
social: true # includes social icons at the bottom of the page
---

I am [ELLIS](https://ellis.eu/phd-postdoc) Doctoral Student @ [AIDOS](https://aidos.group) supervised by [Prof. Bastian Rieck](https://bastian.rieck.me) and co-supervised by [Prof. Søren Hauberg](https://www2.compute.dtu.dk/~sohau/).

My research focuses on *geometrical* and *topological* methods in machine learning. In a nutshell, I
**really** like graphs and shapes. Also seems like they can be useful in AI.

## Past work

### On efficient TDL
I started my journey in applications of [topological deep learning](https://en.wikipedia.org/wiki/Topological_deep_learning) when working with [Dr. Telyatnikov](https://scholar.google.com/citations?user=MzFz-tcAAAAJ&hl=en) and [Dr. Bernardez](https://scholar.google.es/citations?user=YUye6xwAAAAJ&hl=es) from [REAL AI](https://www.ai.ece.ucsb.edu). We have a preprint out on **efficient** ways to perform *higher-order message passing*. Check it out [here](https://arxiv.org/abs/2505.15405v1?trk=feed-detail_main-feed-card_feed-article-content) .

### On graph metrics
For my M.Sc. thesis I was supervised by [Prof. Erik Bekkers](https://ebekkers.github.io) from [AMLab](http://amlab.science.uva.nl) and [Prof. Bastian Rieck](https://bastian.rieck.me). I explored an alternative metric that fully characterizes attributed graphs (in expectation), it's relationship to homomorphism counts and how it can be used as an inductive bias in *message passing neural netowrks* (MPNN). We put out a preprint with some of our findings [here](https://arxiv.org/abs/2511.03068)

## My current interests (and takes)

### On Datasets

The traditional datasets for graph learning have been useful {% cite morris2020tudataset --file about %},
but in the case where we want to asses either a) fully topological (not only combinatorial) tasks and b) a mixture of topological/geometrical tasks there are just no good options out there. Can we really say we 
are doing better if we can't meassure *good* ?

----

{% bibliography --file about --cited_in_order %}

<!-- @Morris2020
[Morris, 2020][https://arxiv.org/abs/2007.08663]
[Morris, C., Kriege, N. M., Bause, F., Kersting, K., Mutzel, P., & Neumann, M. (2020). Tudataset: A collection of benchmark datasets for learning with graphs. arXiv preprint arXiv:2007.08663.][https://arxiv.org/abs/2007.08663]

[2] Coupette, C., Wayland, J., Simons, E., & Rieck, B. (2025). No metric to rule them all: Toward principled evaluations of graph-learning datasets. arXiv preprint arXiv:2502.02379. -->