# Getting Started

## Contents

1.  [Setting up the python environment](#setting-up-the-python-environment) 
    - [Using `pip3`](#using-pip3)
    - [Using `conda`](#using-conda)
    - [Installing Jupyter Notebook](#installing-jupyter-notebook)

2.  [Getting the data](#getting-data)

---

## Setting up the Python environment

Python has been chosen as the main language of this book, for several reasons.
It doesn't have too much jargon, and the signal-to-noise ratio in code is very high (it's almost pseudocode). 
While Python is not the optimal language for scientific computing, it is familiar to most people with basic knowledge of programming, and the learning curve for Python is not as steep as C++, Java, or Julia. 
<br><br>
One of the drawbacks associated with using Python is that it doesn't handle large graphs or datasets very well. C++ and Java both deal with larger structures more efficiently, and many authors of seminal papers in the field of GIS provide C++ and Java implementations alongside their papers. 
<br><br>
Julia, on the other hand, is a perfect midpoint between python and C++/Java. It maintains the readability of Python but was developed specifically for scientific computing applications. 
<br><br>
For the sake of accessibility, the examples and exercises in this book will be based entirely in Python. Implementations in other languages are welcome as pull requests. Simply make a PR of this repo and we'll include any submissions that look promising.
<br><br>
From this point forward, the book will assume that you already have Python 3.6 or newer installed on your system. For installation instructions specific to your operating system, see this [Beginner's Guide](https://wiki.python.org/moin/BeginnersGuide/Download).
<br><br>
There are two primary ways to install the required packages you'll need: `pip` or `conda`. It is recommended to use `pip` as `conda` may have some adverse effects on system dependencies when used improperly in Linux.

:::{note}
If you intend on developing in Windows, it is also recommended that you leverage the convenience of the Windows Subsystem for Linux (WSL). This allows you to use the full capabilities of Linux from within Windows. You can read more about setting up WSL [here](https://docs.microsoft.com/en-us/windows/wsl/install-win10). After enabling WSL, you can proceed with the rest of this book as if you were operating in Linux.
:::

### Using `pip3`

````{tab} Linux

In the terminal, execute the following commands:

```
$ sudo apt update
$ sudo apt install python3-pip

```

Install `venv` and create a python virtual environment:

```
$ sudo apt install python3.8-venv
$ mkdir <new directory for venv>
$ python3 -m venv <path to venv directory>
```
Make sure that you replace `python3.8` with the version of Python you are using.<br>

You can now access your virtual environment using the following command:

```
$ source <path to venv>/bin/activate
```

````


````{tab} MacOS
Using the MacOS terminal:

```
$ python3 -m ensurepip --upgrade
```

`venv` is included with `python 3.8+`. You can run the following command to create a virtual environment:

```
$ mkdir <new directory>
$ python3 -m venv <path to venv directory>
```
You can now access your virtual environment using the following command:
```
$ source <path to venv>/bin/activate
```

````
````{tab} Windows
`pip` should come preinstalled with Windows installations of `python` for versions newer than 3.4.

Make sure to check the "Add Python to PATH" option when using the Python installer. If you don't, you'll need to add `python`, `pip`, and various other programs to the system path manually.

After installing Python, you may need to restart your computer in order for the changes to take effect.

To create a virtual environment, execute the following either in command prompt, or Windows Powershell:

```
C:> py -m venv <new directory>
```

To activate the virtual environment:

```
C:> cd <your venv directory>
C:> .\Scripts\activate
```


:::{note}
There are several things to note when using python in Windows.
1. Using the `py` or `python` command may open the Windows Store app in newer releases of Windows. This can be disabled by going to "Apps and Features", selecting "Application Execution Aliases", and disabling the sliders for any application related to `python` (i.e. `python3.8.exe`, `py.exe`).
2. `pip3` is not sometimes not added to the system PATH by default. You may choose to add it manually, or simply use `pip`, as it should link to the same program.
3. You can use Python by calling the `py` command. If you prefer using `python` or `python3`, you may need to add these to the system PATH manually.
:::
````

### Using `conda`

Install `conda` for your OS using the guide found [here](https://conda.io/projects/conda/en/latest/user-guide/install/index.html). 

You can create a `conda` environment with this command:
```bash
$ conda create --name <name of env> python=<your version of python>
```

To access the newly-created environment:
```bash
$ conda activate <your env name>
```

### Installing Jupyter Notebook

All of the code in this book is stored in Jupyter Notebooks (`.ipynb` files). To access these files directly, you have two options:

1. Open **Binder** or **Google Colab** using the <i class="fas fa-rocket"></i> icon on the top right of a page containing Python code.
2. Install Jupyter Notebook locally.

Jupyter Notebook can be installed as follows:

````{tab} pip3
```bash
$ pip3 install jupyterlab
$ pip3 install notebook
```
````
````{tab} conda
```bash
$ conda install -c conda-forge jupyterlab
$ conda install -c conda-forge notebook
```
````

---
## Getting the data

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