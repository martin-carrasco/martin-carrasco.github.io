---
layout: distill
title: Implementation of different topological lifting techniques
description: Implementation of 4 lifting techniques for the TDL Challenge ICML 2024 
img: assets/img/VR_vis.png
category: TDL
related_publications: true
bibliography: project_1.bib
---



# Techniques
This post referes to a small explanation of a set of techniques to lift from one topological domain to another in the framework of *Topological Deep Learning*. These implementations were done as a part of the **TDL Challenge ICML 2024** as part of the GRaM Workshop. All techniques were accepted, received an award for High Contribution and will be merged to the main branch of the **TopoBenchmarkX** python library.

## N-hop Lifting
Add N-Hop lifting to combinatorial complex where the n-hop neighbourhood is a $$2+k$$ rank hyper edge. Let $$G = (V, E)$$ denote a graph and $$N(v, k)$$ denote the $k$-hop neighbours of $$v$$. We say that an $$(2+k)$$-cell $$ \sigma $$ is the set of neighbours $u$ such that $$u \in N(v, k) \cup \{v\}$$, $$rank(u) > rank(v)$$ and $$\{v\} \subset \sigma$$.  This definition fits with the properties of a **Combinatorial Complex** (CCC) as described in <d-cite key="hajij2022topological"></d-cite>. Similarly, this example is describe in a similar way in the Appendix.

The CCC after the lift will contain information of the underlying graph as hierarchical relations as well as set-relations in terms of the hyperedges added to represent $k$-hop neighbourhoods.


## Coface-Lifting
This technique lifts a **Simplicial Complex** to a **Combinatorial Complex** by taking the *co-adjacencies* of a simplex to be the components of the higher order ($$3$$-cell) cell. Given a simplex $$\sigma$$ and its co-faces $$\tau_1, \tau_2, \cdot \cdot \cdot , \tau_i$$. Then, using a purely combinatorial definition, $$\delta = \sigma \cup \tau_1 \cup \cdot \cdot \cdot \cup \tau_i$$. We can see that it holds that this is a combinatorial complex $$\mathcal{X}$$ because of the two conditions that need to be fulfilled.
1.  All nodes $$v$$ are preserved. So given that the initial point cloud is denoted $$S$$ then it still holds that $$\forall s \in S$$ then {s} $$\in \mathcal{X}$$
2. If $$\sigma,\delta \in \mathcal{X}$$ and $$\sigma \subseteq \delta$$ then $$rank(\sigma) \leq rank(\delta)$$: This hold since we set $rank(\delta)$ to $$3$$ and we are operating on the a subset of the simplifies of a simplicial complex up to dimension $$2$$.


This technique is proposed in <d-cite key="hajij2022topological"></d-cite>

As additional contributions:
1. Add code to make the SimplicialLoader work and actually return a ```Dataset``` and not a ```Data``` object.
2. Add `get_combinatorial_complex_connectivity` to generate connectivity matrices
3. Add an `HMCModel` class that operates over combinatorial complexes.

## Neighborhood Complex Lifting
Given that connections based on neighbourhoods of nodes are already present in GNN literature, the notion of a *neighbourhood complex* becomes of interest. Following from previous work, defining a neighbourhoods as the nodes with which a node shares a neighbour. Formally, $$N(G)$$ is defined in terms of a simplex. Where a simplex $$\sigma_v$$ is the neighbourhood simplex of node $$v \in V(G)$$, composed of all $$u \in V(G)$$ given that $$\exists w: (v, w) \in E(G) \wedge (u, w) \in E(G)$$. <d-cite key="lovasz1978kneser"></d-cite>. 

This structure has been proven to have certain properties that could be interesting in certain domains such  as $$k$$-colorability. As stablished by Lovasz, if $$N(G)$$ is $$(k+2)$$-connected, then,  $$G$$ is not $$k$$-colorable. Additionally, he shows a relationship between the homotopy invariance of $$N(G)$$ and the $$k$$-colorability of $$G$$.

*Neighbourhood complexes* can be used to calculate other more interesting structures in induced by graphs, such as the *dominating set* of $$G$$ which is the *Alexander dual* of $$N(\bar{G})$$(neighbourhood complex of the complement of $$G$$). This is useful for computing homology groups of *dominance complexes* without having to actually calculated the dominance set <d-cite key="matsushita2023dominance"></d-cite>. In future implementations, adding a basic transformation pertaining to the *Alexander Dual* would help in having a  **Dominating Complex**, namely, a simplicial complex composed of simplices where the complements of the nodes composing the simplifies are dominating in $$G$$.


## Random Flag Complex
A random graph $G(n, p)$ denotes a distribution of possible graphs with $n$ vertices where each edge appear with probability $p$. These graphs are also called **Erdos-Renyi** graphs and their properties are analysed as $n \rightarrow \infty$. Then, a property of $$G$$ denoted $$Q(G)$$ is said to happen **with high probability (w.h.p)** if the **probability of** $$Q(G)$$ approaches $$1$$ as $n$ approaches $$\infty$$. For example, Let $$\epsilon > 0$$ be fixed, one can say that $G$ **is connected w.h.p** according to Erdos-Renyi <d-cite key="erdds1959random"></d-cite>  if 

$$
p \geq \frac{(1+\epsilon) \log n}{n}
$$ 

More recently, the properties of random topological structures has been studied in relation the the homological properties that arise out of these. Here we implement a **Random Flag Complex**. A **Flag Complex** is another name for the **clique complex** in the literature. A **Flag Complex** $$\mathcal{X}(H)$$ of a graph $$H$$  is then a clique lifting of $$H$$.  Conversely, we say that a **Flag Complex** a **Clique Complex** and the **Vietoris-Rips Complex** are homeomorphic.


A **Random Flag Complex**  $$\mathcal{X}(n, p)$$ is the **Flag Complex** of a *random graph* $$G(n,p)$$.  Since a *random graph* consists of sampling the space of all possible graphs that can be formed by $$n$$ vertices with each edge having probability $p$, then the clique lifting of that graph is denoted $$\mathcal{X}(n, p)$$. 


In  <d-cite key="kahle2014topology"> </d-cite> the author shows how the $$k$$-th homology group varies with $$p$$ in relation to $$k$$. This technique then provides a way to generate simplicial complexes from point clouds with desired homological properties given the setting of the parameter $p$ which in this implementation can also be regulated with a constant $$\alpha$$ such that $$p=n^{-\alpha}$$
