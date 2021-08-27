# Getting the data

Most of the data used in this book will be sourced from [OpenStreetMaps](https://www.openstreetmap.org). For any other datasets that are not OSM-related, you can download the data in whatever format it is available in, and import it into `python` using the appropriate methods. Open Data websites hosted by various government bodies are a great source of data related to infrastructure, population metrics, and land use. See the [Datasets](../Datasets/index.md) section in this book for more details. 
<br><br>
For OpenStreetMaps, there are two primary ways of retrieving the data:
1. Download the data as-is from OpenStreetMaps' website and use tools like `osmfilter` to tune it as needed. This is not recommended as it is more difficult and not very efficient.
2. Use OpenStreetMaps' API (Overpass API) to query for data. This filters the data on the fly and you only retrieve what you need. The API is accessible in both Java and Python.

:::{admonition} Data Completeness
:class: tip
The data from OSM is not always "complete". This doesn't mean that there are major uncharted regions, but rather that neighbouring nodes are not always grouped correctly. For some nodes where there are feasible connections between them in real life, OSM still represents them as having no [way](https://wiki.openstreetmap.org/wiki/Way) or [relation](https://wiki.openstreetmap.org/wiki/Relation) connecting them. This means that using the `osmnx` parser will result in the nodes being placed in separate graph components, which is not accurate to real-world conditions. We can use `osrm` to find routes between these kinds of nodes and thus "complete" the graphs.

You can read more about the completeness of OpenStreetMaps data here:
1. [Completeness](https://wiki.openstreetmap.org/wiki/Completeness)
2. [Completeness Metrics](https://wiki.openstreetmap.org/wiki/ONS_Completeness_Metrics)
:::


The data model of OpenStreetMaps is surprisingly simple and consists only of three [elements](https://wiki.openstreetmap.org/wiki/Elements): </br>

1. `Node` represents a specific point on the earth's surface defined by its latitude and longitude
2. `Way` is an ordered list of between 2 and 2,000 nodes that define a polyline. Ways are used to represent linear features such as rivers and roads
3. `Relation` is a multi-purpose data structure that documents a relationship between two or more data elements (nodes, ways, and/or other relations). Examples include:
    * A route relation, which lists the ways that form a major (numbered) highway, a cycle route, or a bus route.
    * A turn restriction that describes if a turn can be made from one way onto another.
    * A multipolygon that describes an area (whose boundary is the 'outer way') with holes (the 'inner ways').


All of the above can be found easily on the linked elements page, but there are two things you should be aware of: 
1. All ID's of the same element type are unique globally, but they are not unique across element types (you can find a `Way` with the same ID as a `Node`).
2. `Ways` and `Relations` are made by listing and referring to the ID's of the `Nodes` that constitute them. 