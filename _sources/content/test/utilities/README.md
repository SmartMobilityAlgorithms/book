# Utilities

This is behind the scenes for all the repositories and code in the book.

---

Here is the general structure and where to look at if you want to see what is happening

```
utils
|
|
|
└─── solvers.py ==> This module is meant to be just off-the-shelf solvers for combinatorial problems
|                   that you can use directly after bundling your problem configuration as object
|                   per the interface that is provided in ``problem.py``. We will walk through the design
|                   and the thought process for writing every solver by solving a simple problem with it
|                   after that you can just invoke the solver directly from this module.
|
|
│       
└─── common.py ==> This module is here for providing a nice interface to unnecessary complexity,
|                  like handling graphs produced from osmnx and other utilities associated with
│                  graphs.
│ 
|
|
│
└─── problem.py ==> This module is for defining a number of classes for recurring combinatorial problems
|                   that could be consumed by methods in ``solvers.py``
│ 
│
│
└─── jupyter.py ==> This module is for handling the quirks of jupyter notebook without 
│                   polluting the notebook with distracting commands and functions
│ 
│ 
│ 
│  
└─── viz.py ==> Wrapper around `folium` and `ipyleaflet` to ease visualization and choose the appropriate 
|               library for visulaization based on the size of the graph and the environment the notebook
|               running at.
|
|
|
|
└─── poi.py ==> This module would be used to download data of point of interests and construct a graph based
                on the actual roads between the POIs based on [`osrm`](http://project-osrm.org/) with a lot
                of customization. It would be primarily used on case studies and hopefully it would be of some 
                help in your projects at the end of the semester. 
```

# Usage

If you are on a local machine you don't have to worry about anything at all, just make sure you installed everything on [Getting Started](https://github.com/SmartMobilityAlgorithms/GettingStarted).

If you are on google colab, just upload the `.zip` file that is present in every repository to the default directory and everything would supposedly be fine.

**If not**, don't hesitate for a second to open an issue here and we would go through the steps with you, you are here to learn search algorithms, not how to use package managers :computer: :computer:.
