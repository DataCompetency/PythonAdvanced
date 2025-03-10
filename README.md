Advanced Python Course
----------------------

Is sometimes held on-site at the university of Greifswald. The course materials can also be used for independent self-study.

## Requirements

The participants of this course should be comfortable using Python for simple scripts and should know the procedural or functional programming style. In particular, they should be familiar with handling of built-in datatypes, variables, control flow structures, defining and structuring code in functions and creating and loading modules. 

## Contents

Session 1: Functions (incl. F-strings, Namespace, Call-by-sharing), Code style (incl. PEP8, Docstrings), Type Hinting, Exceptions, Decorators, Generators

Session 2: Object oriented programming paradigm (incl. classes, objects, attributes;  Inheritance & Method prototyping, overriding and overloading;  Useful built-in attributes and methods; Getter and setter methods; Multiple Inheritance and Method Resolution Order (MRO)), Importing Modules and Namespaces, Parallelism

Session 3: NumPy, Matplotlib, Pandas

## Preparations

The course materials consist of Jupyter Notebooks. A Jupyter notebook is an interactive Python environment allowing to combine interactive execution of code along with formatted description texts, like an enriched, interactive lecture manuscript.

### Option 1: Use AppHub from within the university intranet

**If you're already connected via Wifi to eduroam or via LAN in the university,** you can access the AppHub, a Jupyter Notebook server runnning in the university cloud. As a student or employee of the university, you can use your default login credentials to login here
    
[https://apphub.wolke.uni-greifswald.de/](https://apphub.wolke.uni-greifswald.de/)

**then login with your credentials and choose "Datascience" as server type.**
    
### Option 2: Use AppHub remotely from home or anywhere else
    
**If you are not connected to eduroam - or - if you're working from home**, you have to install and setup a VPN client. Follow [these](https://rz.uni-greifswald.de/en/services/technical-infrastructure/vpn/) instructions to install and setup the VPN client for the university of Greifswald  before you can use the AppHub in the university cloud. **In any case you need the university login credentials to have VPN access to the university intranet.**

### Option 3: Install Anaconda on your machine (e.g. to use materials later outside of UG)

**In case you prefer to use AppHub (in case you have university login credentials), you can skip this setup section.** If you'd like to write and test your code independently from the university infrastructure and start from scratch, install the Jupyter environment locally on your machine, following the instructions below:

**Linux**

[Anaconda for Linux](https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh)

**Mac OS X**

[Anaconda for Mac OS X](https://repo.anaconda.com/archive/Anaconda3-2020.07-MacOSX-x86_64.pkg)

**Windows**

[Anaconda for Windows](https://repo.anaconda.com/archive/Anaconda3-2020.07-Windows-x86_64.exe)
    
or checkout [this link](https://anaconda.com) to download the newest version.

**Optional: Jupyter Notebook Extensions and Widgets**

In order to use useful notebook extensions like e.g code completion, autoformatting to comply with PEP8 etc. install the extensions using conda
with

```
conda install -c conda-forge jupyter_contrib_nbextensions
conda install -c conda-forge jupyter_nbextensions_configurator
conda install -c conda-forge ipywidgets
jupyter contrib nbextension install --user
```

A new tab named "NbExtensions" should appear now where you can manage all Jupyter notebook extensions.

A very useful extensions is "Hinterland" offering autocompletion like in the popular Python IDEs e.g. PyCharm.

IPython widgets allow interactive GUI elements to be used in Jupyter notebooks which can be very useful for interactive data visualizations.
    
### Download the course materials
    
**If you're using the AppHub**, either open a new Python 3 notebook and copy the lines
    
```
%%bash
git clone https://github.com/DataCompetency/PythonAdvanced
```

into a cell of a new notebook and then execute the cell with **CTRL + Enter**.
      
**If you're using a locally installed version of Anaconda**, simply go to an arbitrary directory and clone the github repository with the course materials using the following command in a terminal:    
   
```
git clone https://github.com/DataCompetency/PythonAdvanced
```
    
Then simply open one of the Jupyter notebooks. **Have fun !**

### Create a Github account

In order to follow the course on GitHub, consider to create your own GitHub account.
