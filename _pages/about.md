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

My research focuses on *geometrical* and *topological* methods in machine learning. Coming from CS and
having ventured a bit on competitive programming, I've taken to really like graphs on their incredible
usefulnes as a modeling tool and to study other spaces.

## Past work

### On efficient TDL
I started my journey in applications of [topological deep learning](https://en.wikipedia.org/wiki/Topological_deep_learning) when working with [Dr. Telyatnikov](https://scholar.google.com/citations?user=MzFz-tcAAAAJ&hl=en) and [Dr. Bernardez](https://scholar.google.es/citations?user=YUye6xwAAAAJ&hl=es) from [REAL AI](https://www.ai.ece.ucsb.edu). We have a preprint out on **efficient** ways to perform *higher-order message passing*. Check it out [here](https://arxiv.org/abs/2505.15405v1?trk=feed-detail_main-feed-card_feed-article-content) .

### On graph metrics
For my M.Sc. thesis I was supervised by [Prof. Erik Bekkers](https://ebekkers.github.io) from [AMLab](http://amlab.science.uva.nl) and [Prof. Bastian Rieck](https://bastian.rieck.me). I explored an alternative metric that fully characterizes attributed graphs (in expectation), it's relationship to homomorphism counts and how it can be used as an inductive bias in *message passing neural netowrks* (MPNN). We put out a preprint with some of our findings [here](https://arxiv.org/abs/2511.03068). 

I also got to work with professionals on well-studied metrics on graphs in [here](https://arxiv.org/abs/2605.06466). It was a joy to work with [Katharina](https://limbeckkat.github.io) and [Nadja](https://nadja.topology.rocks) for the first time :).

### On topological deep learning
On my first official project in the lab [Johannes](https://j-s-schmidt.topology.rocks) and I look into *higher-order message passing* under the hood and find strong evidence it's more brittle than we thought! 

Naturally we were lead by a great supervision team, [Nello](https://blasern.github.io), [Bastian](https://bastian.rieck.me) along with a new collaboration with [Guy](https://guywolf.org). 


We find that graph-based models on  more parsimonious representations of simplicial complexes (one skeleton, dual graph or hasse diagram) are good alternative to HOMP. Suprisingly, we learn all of these models are **terrible** at topological generalization. You can try your hand at our benchmark using the [MANTRA](https://github.com/aidos-lab/mantra) dataset and/or read our [preprint](https://arxiv.org/abs/2605.06467).