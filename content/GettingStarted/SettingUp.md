# Setting up the python environment

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

## Using `pip3`

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

## Using `conda`

Install `conda` for your OS using the guide found [here](https://conda.io/projects/conda/en/latest/user-guide/install/index.html). 

You can create a `conda` environment with this command:
```bash
$ conda create --name <name of env> python=<your version of python>
```

To access the newly-created environment:
```bash
$ conda activate <your env name>
```

## Installing Jupyter Notebook

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