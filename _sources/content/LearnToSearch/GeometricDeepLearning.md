# Geometric Deep Learning

As mentioned previously, a graph is a structured data type that consists of 3 sets, namely, vertices/ nodes (entities that hold information), edges (connections between nodes that can also hold information) and a set representing relations between vertices and edges. Graph deep learning (GDL) is a subfield of machine learning that combines both graph theory and deep learning. 

**GDL = Graph Theory + Deep Learning**

The objective of GDL is to build neural networks that can learn from non-Euclidean data or graphs. The following table summarizes the differences between Euclidean and Non-Euclidean data:

| Aspects                                                  | Euclidean Data                                           | Non-Euclidean Graph Data                  |
|----------------------------------------------------------|----------------------------------------------------------|-------------------------------------------|
| Dimensionality                                           | 1d data: numbers, text, speech 2d data: images or videos | large dimensionality                      |
| Data modality                                            | Unimodal                                                 | Multimodal                                |
| Structure                                                | Structured data                                          | Arbitrary structure                       |
| Spatial locality                                         | yes                                                      | no                                        |
| shift-invariance                                         | yes                                                      | no                                        |
| ordinality or hierarchy                                  | yes                                                      | No fixed node ordering or reference point |
| the shortest path between 2 points                       | a straight line                                          | is not necessarily a straight line        |
| Basic operations like dot products, norms & convolution  | Well-defined                                             | Not well defined                          |
| Data storage                                             | Can be stored as a tensor                                | cannot be easily stored as a tensor       |

Convolutional Neural Networks (CNNs) can only operate on regular Euclidean data like image (2D grid) and text (1D sequence) and cannot deal with non-Euclidean data. In order to deal with this problem, graph structure needs to be encoded where nodes are encoded as low-dimensional vectors in latent space. The geometric relations in this latent space correspond to interactions (e.g. edges) in the original graph. Data-driven approaches are used to learn the node embeddings. These representation learning approaches consist of the following three main steps {cite}`zhou_cui_hu_zhang_yang_liu_wang_li_sun_2020`:

1. Collect neighbors
2. Aggregate feature information from neighbors
3. Decode graph context and/or label using aggregated information

[DeepWalk](https://github.com/phanein/deepwalk) and [node2vec](https://snap.stanford.edu/node2vec/) are random walk-based methods for graph embedding based on representation learning. Graph Neural Network (GNN) {cite}`DBLP:journals/corr/abs-1709-05584` is commonly used to adapt existing machine learning technologies to directly process non-Euclidean structured data as input, so that this (possibly useful) information is not lost in transforming the data into a Euclidean input as required by existing techniques {cite}`scarselli_gori_tsoi_hagenbuchner_monfardini_2009`.
