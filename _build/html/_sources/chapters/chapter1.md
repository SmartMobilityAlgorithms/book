# GettingStarted

This repository is meant to be the how and the what of everything.

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity) [![GitHub contributors](https://img.shields.io/github/contributors/Naereen/StrapDown.js.svg)](https://github.com/SmartMobilityAlgorithms/GettingStarted/graphs/contributors) 
[![GitHub issues](https://img.shields.io/github/issues/Naereen/StrapDown.js.svg)](https://github.com/SmartMobilityAlgorithms/GettingStarted/issues) 
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/SmartMobilityAlgorithms/GettingStarted/pulls)
[![Gitter](https://badges.gitter.im/SmartMobilityAlgorithms/community.svg)](https://gitter.im/SmartMobilityAlgorithms/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/SmartMobilityAlgorithms/GettingStarted/master)


### Contents

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

This organization is meant to accompany ECE1724H S Bio-inspired Algorithms for Smart Mobility course being offered at University of Toronto. This project-based course provides a comprehensive introduction to bio-inspired search algorithms and highlights the power of these computational techniques in solving ill-structured problems in the context of smart mobility.

The code in all of the notebooks is step-by-step guide for the implementation of the algorithms in the course using actual maps from OpenStreetMaps. 


### Language Choice

We have choosen `python` as the main and only language as it doesn't have much jargon and the signal to noise ratio in code is very high; it is almost like pseudocode. `Python` is not the optimal language for scientific computing and especially with large graphs that we extract from maps. All the major routing and navigation engines usually use `C++` or `Java` and most of the authors of the seminal papers in the field usually provide `C++` implementation accompying their papers. What would be the perfect trade-off between `python` and `C++`? `Julia`; it was made with scientific computing in mind and it gives a comparable performance with `C++` and with almost the readability  of `python`.

Surely, We would love to have `Julia` implementation for the algorithms in so if you want to do so, don't hesitate to open PR with your `Julia` code and just change the code line by line from `Python` to `Julia`. For programming language benchmarking, see [Benchmarks Game](https://benchmarksgame-team.pages.debian.net/benchmarksgame/fastest/julia-python3.html).

---

## General structure of the repositories


Each repository contains three sections:

### 1. Algorithms Notebooks

Here we introduce the algorithms and how to implement them on a real world `.osm` data and we would provide the pseudocode to tune down the noise of programming languages quirks and what to consider and what you should be aware of when implementing these algorithms. These notebooks are complementary for the materials in the lectures.

### 2. Toy Problems Notebooks

These are more or less like the algorithm notebooks but with more focus on solving toy problems such as travelling salesman problem (TSP) or finding how to optimally pave a muddy city using minimum spanning tree (MST).

### 3. Case Studies Notebooks

These are real world problems found in the literature and potential course projects. We usually need to exert some efforts to get the data and think about how to solve the problem.


---

## Libraries Used

### osmnx

This library was developed by [geoff boeing](https://geoffboeing.com/) from University of Southren California to ease the process of retrieving and manipulating the data from OpenStreetMap and make it easier to be interpolated into Python applications. It offeres the ability to download the data (filtered) from OSM and returns the network as networkx graph data structure. The library is really big to be explained entirely in a README file but you can check the official website from [here](https://osmnx.readthedocs.io/en/stable/#) and follow Professor Geoff Boeing website as he posts regularly on the recent updates and trends about osmnx and the field.

### networkx

This is one of the pillars of Python programming and scientific computing besides numpy and scipy. Its main and only goal is supporting graphs data structures and the associated algorithms like shortest path and networks flow and optimization. `osmnx` returns the map as `networkx` network so it is possible to use all the library's functionalities on the maps obtained from OSM. Networkx has books written explaining its API's and we wholeheartedly recommend [Complex Network Analysis in Python: Recognize - Construct - Visualize - Analyze - Interpret](https://www.amazon.com/Complex-Network-Analysis-Python-Recognize/dp/1680502697) if you want to dive into it. Information about `networkx` is also available [here](https://networkx.github.io/). 

`networkx` has monopoly over the field of network analysis for many years now but sometimes scalability of networkx is not the answer to your problem. If your network has tens of millions of nodes, it gets really ugly because `networkx` is still just `python` library and `python` can't handle these millions of nodes and would run out of memory and give you segmentation fault.

You can optimize `python` by using `__slots__` instead of `__dict__`, discussed [here](https://stackoverflow.com/questions/472000/usage-of-slots#:~:text=The%20proper%20use%20of%20__,one%20dict%20for%20every%20object.%5D) and you can use arrays and all of that, but still you would have problems.

What to do now? we do `C++`, you can use [graph-tool](https://graph-tool.skewed.de/) which was built over the [boost-graph](https://www.boost.org/doc/libs/1_64_0/libs/graph/doc/index.html) libraries or you can use [igraph](https://github.com/igraph) which is written in C. But you got to write your own parser for OpenStreetMaps data and understand its file format, fortunately this is not complicated.

### osrm

Sometimes in a lot of problems, you are not concerned about finding the route between two places and want to have the routes as given. [OSRM](http://project-osrm.org/) does exactly that; it is a routing engine with an API that you would feed with coordinates and gives you the fastest route between them. It has other useful capabilities like doing travelling salesman and solving all pairs shortest path.

### geopandas

It is an extension to pandas to handle geospatial data by extending the datatypes of pandas and be able to query and manipulate spatial data otherwise you would need to deal with [spatial databases](https://en.wikipedia.org/wiki/Spatial_database) for these operations, like how to properly and efficiently represent polygons and curved lines and query them without much overhead (for database folks, the indexing of spatial data is different than normal data).

### shapely

It provides us with datatypes to represent geometric objects that geopandas exploit to represent spatial data.

### nominatim

It is used to look up a location from a textual description (the official website description). This is called geocoding and decoding which is translating address of a location to its coordinates.

### visualization libraries

There are <b>many</b> libraries for visualization, but we are mainly using [folium](https://python-visualization.github.io/folium/) and [ipyleaflet](https://ipyleaflet.readthedocs.io/en/latest/) and both of them are just wrapper around [leaflet.js](https://github.com/Leaflet/Leaflet) which is the go-to library for any kind of map visualization in almost all web and mobile applications.

Each of `ipyleaflet` and `folium` were both created to serve the same purpose, and you don't need to dwell so much on how to use them if you don't want to as we have provided wrapper around them on  `utilities/utils/viz.py` that contains two functions: one for drawing a map with our graph overlaied on it and and the other function is for drawing a route between two places/nodes with markers marking the source and destination. But you need to know the difference between them, `folium` is much lightweight than `ipyleaflet` but on the other hand `ipyleaflet` has more options and very niche capabitilies but `ipyleaflet` doesn't work on google colab unlike `folium`; see [googlecolab/colabtools#60](https://github.com/googlecolab/colabtools/issues/60) for more details. 

There are other visualization libraries that you should be aware of: 
* [hvplot](https://hvplot.holoviz.org/user_guide/Geographic_Data.html), if you want to get going through your analysis with geopandas and dataframes and all that. There are no place for that but you need to be aware of the significance of working with vanilla [GeoPandas](https://geopandas.org/), and that `osmnx` [supports that](https://osmnx.readthedocs.io/en/stable/osmnx.html#module-osmnx.projection) and yields two dataframes: one for all your nodes and one for all the edges.

* [mplleaflet](https://github.com/jwass/mplleaflet), which is another `leaflet` based library, but it plays really nice with `matplotlib`.

### tqdm

[This](https://github.com/tqdm/tqdm) library would help us to see the progress of or algorithm on the runtime. We would use it in all of the other repositories to see how much the speed of the algorithm in traversing the given map and how many nodes are expanded per second. It works on any python iterable structure.

#### Note

Most of these libraries uses coordinates of a certain place to do its job, but please take into account that some of them accept the coordinates as (longtitude, latitude) and others as (latitude, longtitude). 

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
How to generate initial population for P-metaheruristics in continous nad combinatorial problems. In the generation of the initial population, the main criterion to deal with is diversification. If the initial population is not well diversified, a premature convergence can occur. For instance, this may happen if the initial population is generated using a greedy heuristic or a S-metaheuristic (e.g., local search, simulated annealing) for each solution of the population.

Use binder, its icon is at the top, to launch the repository and run the notebooks remotely. 

---

## Setting up your environment

We assume that you have Python 3.6+ installed in your system and we will go through how to install ```osmnx``` and ```networkx``` and ```jupyter```

---

### Linux

You have two way either to use ```conda``` or ```pip``` to get everything working, but ```conda``` usually messes up the system dependencies on linux and complicate easy things and it is a bad idea to use it.

</br>

If you still want to use ```conda```, you can just execute the following command.

```
$ conda install -c conda-forge osmnx
```

and that is it.

</br>

If else, you need to get ```pip``` package manager installed to use it to fetch the other libraries.

```
$ sudo apt install python3-pip
```

Unfortunately we just can't "pip" our way through the dependencies because ```osmnx``` depends on library called ```Rtree``` which needs to be *made* using this command

```
$ apt-get install libspatialindex-c4v5
```

and then after that we can use ```pip``` to get osmnx

```
$ pip3 install osmnx
```

To test that everything is working, issue the following command

```
$ python3 -c "import osmnx"
```

We do some animations every now and then with `matplotlib` which needs `ffmpeg` to construct the video, so let's install it

```
$ sudo apt install ffmpeg
```

If there is any error in installation, the terminal will whine about missing module and whatnot. If so, open an issue and we will walk through the problem together.

---

### MacOS

That exact same steps as above but instead of using ```apt```, you are going to use ```brew``` and that if you want to do the ```pip``` way. If you want to use ```conda```, it would be the exact same command.

EXCEPT in installing `libspatialindex-c4v5`, you will need to issue the following command instead

```
$ brew install spatialindex
```


---

### Windows

Create a conda environment
```
\> conda create -n uoft python=3.7
```

Activate the environment
```
\> conda activate uoft
```

Install the following packages

```
\> conda install -c conda-forge rtree
```

```
\> conda install -c conda-forge osmnx
```

```
\> conda install -c conda-forge ipyleaflet
```

```
\> conda install -c conda-forge folium
```

```
\> conda install -c conda-forge tqdm
```

and don't forget to install ffmpeg from [here](https://www.gyan.dev/ffmpeg/builds/)

---

### Jupyter Notebook

All the codes in the repositories are in jupyter notebooks so, we need to install that to launch the environment.</br>
For ```conda``` users and such
</br>

```
conda install -c conda-forge jupyterlab
```

```
conda install -c conda-forge notebook
```

</br>

For ```pip``` people
</br>

```
pip install jupyterlab
```

```
pip install notebook
```

---

#### Note

Things can go wrong very easily when you install the libraries because of building `Rtree` and you can mess up your whole `python` environment if you played with `pip` and `conda` at the same time.

Don't hesitate to open an issue if any thing comes up with you.

---

## OpenStreetMaps Data Model

The data model of OpenStreetMaps is surprisingly simple and consists only of three [elements](https://wiki.openstreetmap.org/wiki/Elements): </br>

1. Node</br>
represents a specific point on the earth's surface defined by its latitude and longitude
2. Way</br>
is an ordered list of between 2 and 2,000 nodes that define a polyline. Ways are used to represent linear features such as rivers and roads
3. Relation</br>
A relation is a multi-purpose data structure that documents a relationship between two or more data elements (nodes, ways, and/or other relations). Examples include:

* A route relation, which lists the ways that form a major (numbered) highway, a cycle route, or a bus route.
* A turn restriction that says you can't turn from one way into another way.
* A multipolygon that describes an area (whose boundary is the 'outer way') with holes (the 'inner ways').

#

All the above can be found easily on the linked elements page, but there are things you should be aware of: All ID's of the same element type are unique globally, but you can find ID of Way the same as the ID of Node and that is allowed.</br>Ways and Relations are made by listing and referring to the ID's of the Nodes that constitute them. 

---

## Getting the data

There are many ways to get the data including using `osmnx` directly and get your data in a very clean way, but in some situations you need to have more control over the data and need to tune it and alter it in ways that `osmnx` can't do. So we need to get down to get the data from the original source of OpenStreetMaps and download the data directly and after that we let `osmnx` parse it.</br>

Generally there are two ways of getting the data from OpenStreetMaps:

1. Download the data in its vanilla form and structure straight out of OpenStreetMaps website and use tools like [osmfilter](https://wiki.openstreetmap.org/wiki/Osmfilter)(hard way and not widely used in practice) to tune it as you want and pass it to `osmnx` in `python` code and that is it.
2. Use OpenStreetMaps API which is called Overpass API and get your data and filter it on the fly and can be used from `Python` and `Javascript`.

#

Check [Datasets](https://github.com/SmartMobilityAlgorithms/Datasets) in which we discuss in enough details how to use Overpass API.

#

### Completness of the data

There are some things that you need to be aware of: the data from OpenStreetMaps are not complete, not in the sense that there are major uncharted areas of the earth but the nodes of the same area usually are not grouped properly so you can have two places with obvious and feasible route between them but the two nodes are not related in any way in the `.osm` file and there is no [way](https://wiki.openstreetmap.org/wiki/Way)/[relation](https://wiki.openstreetmap.org/wiki/Relation) between these nodes, so `osmnx` parser put them in different graph component at this point we would go to use `osrm` to find the route between these nodes and make the graph complete. 

You can read more about that completness of OpenStreetMaps data here:
1. [Completness](https://wiki.openstreetmap.org/wiki/Completeness)
2. [Completness Metrics](https://wiki.openstreetmap.org/wiki/ONS_Completeness_Metrics)

---

## Relevant Tools

1. Developing web/mobile application and you want to get really fancy with your maps, you have [Open layers](https://openlayers.org/) which is the industry standard for that.

2. Traffic beyond just max speed and duration? [traffic per edge](https://github.com/Project-OSRM/osrm-backend/wiki/Traffic) or [Open traffic](https://github.com/opentraffic).

3. [JupyterLab Extensions for Geospatial Data science](https://towardsdatascience.com/4-must-have-jupyterlab-extensions-for-geospatial-data-science-f3cf7822de4b).

4. [OSMPythonTools](https://github.com/mocnik-science/osm-python-tools) is a well-written package to query OSM services.
5. [deck.gl](https://deck.gl/)
6. [kepler.gl](https://kepler.gl/)
7. [Google Data Studio](https://datastudio.google.com/)
8. [QGIS](https://qgis.org/en/site/)
9. [ParaView](https://www.paraview.org/)

## License

The project is licensed under the [Apache license](https://github.com/SmartMobilityAlgorithms/GettingStarted/blob/master/LICENSE).
