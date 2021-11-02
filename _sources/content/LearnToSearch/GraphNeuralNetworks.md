# Graph Neural Networks (GNN)

As mentioned previously, a graph is a structured data type that consists of 3 sets, namely, vertices/ nodes (entities that hold information), edges (connections between nodes that can also hold information) and a set representing relations between vertices and edges. Graph deep learning (GDL) is a subfield of machine learning that combines both graph theory and deep learning. Graph Neural Network is a type of Neural Network which directly operates on the Graph structure. Graph Neural Networks seek to adapt existing machine learning technologies to directly process non-Euclidean structured data as input, so that this (possibly useful) information is not lost in transforming the data into a Euclidean input as required by existing techniques {cite}`gnn_stanford`. 

The following table shows the difference between Euclidean and Non-Euclidean data:

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


## Resources:
- Deep Graph Library ([DGL](https://github.com/dmlc/dgl))
- Graph Nets Library ([Graph Nets](https://github.com/deepmind/graph_nets))
- PyTorch Geometric Library ([PyTorch Geometric](https://pytorch-geometric.readthedocs.io/en/latest/))
- Stanford Network Analysis Platform ([SNAP](https://github.com/snap-stanford/snap-python))