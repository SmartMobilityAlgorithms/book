# Getting Started

## Contents

1.  [Introduction and Quick Overview](#introduction-and-quick-overview) 

2.  [General structure of the repositories](#general-structure-of-the-repositories)

3.  [Libraries used](#libraries-used)
    * [osmnx](#osmnx)
    * [networkx](#networkx)
    * [osrm](#osrm)
    * [geopandas](#geopandas)
    * [shapely](#shapely)
    * [nominatim](#nominatim)
    * [visualization libraries](#visualization-libraries)
    * [tqdm](#tqdm)
    
4.  [Quick tutorials](#quick-tutorials)
    
5. [Setting up your environment](#setting-up-your-environment)
    * [Linux](#linux)
    * [MacOS](#macos)
    * [Windows 10](#windows)
    * [Jupyter Notebooks](#jupyter-notebook)

6. [OpenStreetMaps data model](#openstreetmaps-data-model)

7. [Getting the data](#getting-the-data)

8. [Relevant Tools](#relevant-tools)

---

## Introduction and Quick Overview

This Jupyter Book is meant to accompany the "AI Search Algorithms for Smart Mobility" book by Dr. Alaa Khamis and Yinan Wang. The book provides a comprehensive introduction to bio-inspired search algorithms and highlights the power of these computational techniques in solving ill-structured problems in the context of smart mobility.

The code in all of the notebooks a is step-by-step guide for the implementation of the algorithms in the book using actual maps from OpenStreetMaps. 


### Language Choice

We have choosen `python` as the main language for the course, as it doesn't have too much jargon and the signal-to-noise ratio in code is very high; it is almost like pseudocode. `python` is not the optimal language for scientific computing, especially with large graphs that we extract from maps. All the major routing and navigation engines usually use `C++` or `Java`, and most of the authors of the seminal papers in the field usually provide `C++` implementations accompanying their papers. What would be the perfect trade-off between `python` and `C++`? `Julia`; it was made with scientific computing in mind and it gives a comparable performance with `C++` and with almost the readability  of `python`.

We may decide to provide a `Julia` version of the notebooks for this book in the future. In the meantime, we would love to have `Julia` implementations for the algorithms submitted by readers. If you want to do so, don't hesitate to open a PR with your `Julia` code and just change the code line by line from `Python` to `Julia`. For programming language benchmarking, see [Benchmarks Game](https://benchmarksgame-team.pages.debian.net/benchmarksgame/fastest/julia-python3.html).

---

## General structure of the repositories


Each repository contains three sections:

### 1. Algorithms Notebooks

Here we introduce the algorithms and how to implement them on a real world `.osm` dataset. We also provide the pseudocode to tune down the noise of programming language quirks, so be aware of language-specific limitations and conventions. These notebooks are complementary to the materials provided in the lectures.

### 2. Toy Problems Notebooks

These are more or less like the algorithm notebooks but with more focus on solving toy problems, such as the Travelling Salesman Problem (TSP), or finding how to optimally pave a muddy city using minimum spanning trees (MST).

### 3. Case Studies Notebooks

These are real world problems found in the literature, and can be potential course projects. We usually need to exert some efforts to get the data and think about how to solve these problem.


---

## Libraries Used

### osmnx

This library was developed by [Geoff Boeing](https://geoffboeing.com/) from the University of Southern California to ease the process of retrieving and manipulating the data from OpenStreetMap, and to make it easier to be interpolated into Python applications. It offers the ability to download the data (filtered) from OSM and returns the network as `networkx` graph data structure. The library is too complicated to be explained fully in a README file, but you can check the [official website](https://osmnx.readthedocs.io/en/stable/#) and follow Professor Boeing's website as he posts regularly on recent updates and trends about osmnx and the field in general.

### networkx

This is one of the pillars of Python programming and scientific computing, besides `numpy` and `scipy`. Its main and only goal is supporting graph data structures and the associated algorithms like shortest path and networks flow and optimization. `osmnx` returns the map as `networkx` network so it is possible to use all the library's functions on the maps obtained from OSM. `networkx` has books written explaining its API's and we wholeheartedly recommend [Complex Network Analysis in Python: Recognize - Construct - Visualize - Analyze - Interpret](https://www.amazon.com/Complex-Network-Analysis-Python-Recognize/dp/1680502697) if you want to dive into it. Information about `networkx` is also available [here](https://networkx.github.io/). 

`networkx` has a monopoly over the field of network analysis for many years now, but the scalability of `networkx` may be an issue. If your network has tens of millions of nodes, it can get really ugly because `networkx` is still just a `python` library, and `python` can't handle these millions of nodes and will run out of memory, and give you a segmentation fault.

You can optimize `python` by using `__slots__` instead of `__dict__`, something which is discussed [here](https://stackoverflow.com/questions/472000/usage-of-slots#:~:text=The%20proper%20use%20of%20__,one%20dict%20for%20every%20object.%5D). You can also use arrays or something similar, but then other problems would arise.

Are there any alternatives? In `C++`, you can use [graph-tool](https://graph-tool.skewed.de/), which was built over the [boost-graph](https://www.boost.org/doc/libs/1_64_0/libs/graph/doc/index.html) libraries, or you can use [igraph](https://github.com/igraph) which is written in C. But for these you will need to write your own parser for OpenStreetMaps data and understand its file format. Fortunately, this is not too complicated.

### osrm

For some problems, determining the route between multiple points is not the main focus, and it is acceptable to use a pre-generated route. [OSRM](http://project-osrm.org/) does exactly that; it is a routing engine with an API that you feed with coordinates, and in return it gives you the fastest route between them. It has other useful capabilities like doing Travelling Salesman and solving all pairs shortest path.

### geopandas

It is an extension to pandas that handles geospatial data by extending the datatypes of pandas, and the ability to query and manipulate spatial data. Alternatively, you would need to deal with [spatial databases](https://en.wikipedia.org/wiki/Spatial_database) for these operations, like how to properly and efficiently represent polygons and curved lines and query them without too much overhead (for database folks, the indexing of spatial data is different than normal data).

### shapely

It provides us with datatypes to represent geometric objects that geopandas exploits to represent spatial data.

### nominatim

It is used to look up a location from a textual description (the official website description). This is called geocoding and decoding, which is translating address of a location to its coordinates (and vice-versa).

### visualization libraries

There are <b>many</b> libraries for visualization, but we are mainly using [folium](https://python-visualization.github.io/folium/) and [ipyleaflet](https://ipyleaflet.readthedocs.io/en/latest/). Both of them are just wrappers around [leaflet.js](https://github.com/Leaflet/Leaflet), which is the go-to library for any kind of map visualization in almost all web and mobile applications.

Both of `ipyleaflet` and `folium` were created to serve the same purpose, and you don't need to dwell so much on how to use them if you don't want to, as we have provided wrappers around them in  `utilities/utils/viz.py`. This contains two functions: one for drawing a map with our graph overlaid on it, and and the other function is for drawing a route between two places/nodes with markers marking the source and destination. At the very least, you should be able to recognize the differences between the two wrappers. `folium` is much more lightweight than `ipyleaflet`, but on the other hand `ipyleaflet` has more options and very niche capabitilies. `ipyleaflet` doesn't work on Google Colab, unlike `folium`; see [googlecolab/colabtools#60](https://github.com/googlecolab/colabtools/issues/60) for more details. 

There are other visualization libraries that you should be aware of: 

* [hvplot](https://hvplot.holoviz.org/user_guide/Geographic_Data.html), if you want to get going through your analysis with geopandas and dataframes and all that. You should be aware of the significance of working with vanilla [GeoPandas](https://geopandas.org/), and that `osmnx` [supports that](https://osmnx.readthedocs.io/en/stable/osmnx.html#module-osmnx.projection) and yields two dataframes: one for all your nodes and one for all the edges.

* [mplleaflet](https://github.com/jwass/mplleaflet), which is another `leaflet`-based library, but it plays really nicely with `matplotlib`.

### tqdm

[This library](https://github.com/tqdm/tqdm) helps us to see the progress of our algorithm while it is running. We use it in all of the other repositories to track the speed of the algorithm in traversing the given map, and how many nodes are expanded per second. It works on any python iterable structure.

#### Note

Most of these libraries use coordinates as input and/or output, but please take into account that some of them accept the coordinates as (longtitude, latitude) and others as (latitude, longtitude). 

---

## Quick Tutorials

1. **Snapshots 1**</br>
A very dense tutorial over almost all the tools we will be using in the repositories

2. **Utilities**</br>
Goes over how to properly use the graphs returned from `osmnx` and some useful methods on them

3. **Snapshots 2**</br>
We will skim over the capabilities of `osmnx` and `networkx` and how to do visualization with our utilities

4. **Networkx**</br>
This is a very short introduction about the capabilities of `networkx`

5. **Osmnx/Geopandas/Shapely**</br>
How to download data from `osmnx` and see all the graph properties

6. **Generation of Initial Population**</br>
How to generate initial population for P-metaheruristics in continous and combinatorial problems. In the generation of the initial population, the main criterion to deal with is diversification. If the initial population is not well diversified, a premature convergence can occur. For instance, this may happen if the initial population is generated using a greedy heuristic or a S-metaheuristic (e.g., local search, simulated annealing) for each solution of the population.

Use binder, its icon is at the top, to launch the repository and run the notebooks remotely. 

---

## Setting up your environment

We assume that you have Python 3.6+ installed in your system and we will go through how to install ```osmnx``` and ```networkx``` and ```jupyter```

---

### Linux

You have two ways (either to use `conda` or `pip`) to get everything working, but `conda` usually messes up the system dependencies on Linux and complicates easy things, so we recommend using `pip`.

</br>

If you still want to use ```conda```, you can just execute the following command:

```$ conda install -c conda-forge osmnx```

and that is it.

</br>

Otherwise, you will need to get ```pip``` package manager installed to use it to fetch the other libraries.

```$ sudo apt install python3-pip```

Unfortunately we just can't "pip" our way through the dependencies because ```osmnx``` depends on a library called ```Rtree```, which needs to be *made* using this command

```$ apt-get install libspatialindex-c4v5```

and then after that we can use ```pip``` to get osmnx

```$ pip3 install osmnx```

To test that everything is working, issue the following command

```$ python3 -c "import osmnx"```

We do some animations every now and then with `matplotlib`, which needs `ffmpeg` to construct the video. Install it using:

```$ sudo apt install ffmpeg```

If there is any error in installation, the terminal will complain about missing modules and whatnot. If so, open an issue and we will walk through the problem together.

---

### MacOS

Follow the exact same steps as above, but instead of using ```apt```, you are going to use ```brew``` (if you want to uses the ```pip``` method). If you want to use ```conda```, it would be the exact same command as above,

**EXCEPT** when installing `libspatialindex-c4v5`, you will need to issue the following command instead:

```$ brew install spatialindex```


---

### Windows

Create a conda environment:
```\> conda create -n uoft python=3.7```

Activate the environment:
```\> conda activate uoft```

Install the following packages:

```\> conda install -c conda-forge rtree```

```\> conda install -c conda-forge osmnx```

```\> conda install -c conda-forge ipyleaflet```

```\> conda install -c conda-forge folium```

```\> conda install -c conda-forge tqdm```

and don't forget to install ffmpeg from [here](https://www.gyan.dev/ffmpeg/builds/)

---

### Jupyter Notebook

All the code in the repositories are in Jupyter Notebooks , so we need to install that to launch the environment.</br>
For ```conda``` users:
</br>

```conda install -c conda-forge jupyterlab```

```conda install -c conda-forge notebook```

</br>

For ```pip``` users:
</br>

```pip install jupyterlab```

```pip install notebook```

---

#### Note

Things can go wrong very easily when you install the libraries because of building `Rtree`, and you can mess up your whole `python` environment if you played with `pip` and `conda` at the same time.

Don't hesitate to open an issue if any issues arise during the installation phase.

---

## OpenStreetMaps Data Model

The data model of OpenStreetMaps is surprisingly simple and consists only of three [elements](https://wiki.openstreetmap.org/wiki/Elements): </br>

1. `Node` represents a specific point on the earth's surface defined by its latitude and longitude
2. `Way` is an ordered list of between 2 and 2,000 nodes that define a polyline. Ways are used to represent linear features such as rivers and roads
3. `Relation` is a multi-purpose data structure that documents a relationship between two or more data elements (nodes, ways, and/or other relations). Examples include:
    * A route relation, which lists the ways that form a major (numbered) highway, a cycle route, or a bus route.
    * A turn restriction that describes if a turn can be made from one way onto another.
    * A multipolygon that describes an area (whose boundary is the 'outer way') with holes (the 'inner ways').

#

All of the above can be found easily on the linked elements page, but there are two things you should be aware of: 
1. All ID's of the same element type are unique globally, but they are not unique across element types (you can find a `Way` with the same ID as a `Node`).
2. `Ways` and `Relations` are made by listing and referring to the ID's of the `Nodes` that constitute them. 

---

## Getting the data

There are many ways to get the data, including using `osmnx` directly to get your data in a very clean way, but in some situations you may need to have more control over the data, tuning it and altering it in ways that `osmnx` does not support. For this we need to get the data from the original source of OpenStreetMaps and download the data directly, and let `osmnx` parse it afterwards.</br>

Generally there are two ways of getting the data from OpenStreetMaps:

1. Download the data in its vanilla form and structure straight out of OpenStreetMaps' website and use tools like [osmfilter](https://wiki.openstreetmap.org/wiki/Osmfilter) (hard way and not widely used in practice) to tune it as you want and pass it to `osmnx` in `python` code.
2. Use OpenStreetMaps API (`Overpass API`) and get your data and filter it on the fly. This can be used from `Python` and `Javascript`.

#

Take a look at [Datasets](https://github.com/SmartMobilityAlgorithms/Datasets), in which we discuss in detail how to use Overpass API.

#

### Completeness of the data

The data from OpenStreetMaps is not "complete", not in the sense that there are major uncharted areas of the earth, but that the nodes of the same area are usually not grouped correctly. You can have two places with obvious and feasible routes between them but the two nodes are not related in any way in the `.osm` file and there is no [way](https://wiki.openstreetmap.org/wiki/Way)/[relation](https://wiki.openstreetmap.org/wiki/Relation) between these nodes, so `osmnx` parser will place them in different graph components. For these instances, we can use `osrm` to find the route between these nodes and make the graph complete. 

You can read more about that completness of OpenStreetMaps data here:
1. [Completeness](https://wiki.openstreetmap.org/wiki/Completeness)
2. [Completeness Metrics](https://wiki.openstreetmap.org/wiki/ONS_Completeness_Metrics)

---

## Relevant Tools

1. If you are developing a web/mobile application and you want to get really fancy with your maps, you have [Open layers](https://openlayers.org/) which is the industry standard for webmaps.

2. Do you want traffic data beyond just max speed and duration? Check out [traffic per edge](https://github.com/Project-OSRM/osrm-backend/wiki/Traffic) or [Open traffic](https://github.com/opentraffic).

3. [JupyterLab Extensions for Geospatial Data science](https://towardsdatascience.com/4-must-have-jupyterlab-extensions-for-geospatial-data-science-f3cf7822de4b).
4. [OSMPythonTools](https://github.com/mocnik-science/osm-python-tools) is a well-written package to query OSM services.
5. [deck.gl](https://deck.gl/)
6. [kepler.gl](https://kepler.gl/)
7. [Google Data Studio](https://datastudio.google.com/)
8. [QGIS](https://qgis.org/en/site/)
9. [ParaView](https://www.paraview.org/)

## License

The project is licensed under the [Apache license](https://github.com/SmartMobilityAlgorithms/GettingStarted/blob/master/LICENSE).
