Advanced Python Course
----------------------

This seminar was held at the university of Greifswald. The course materials can be used for independent self-study.

## Requirements

The participants of this course should be comfortable using Python for simple scripts and should know the procedural or functional programming style. In particular, they should be familiar with handling of built-in datatypes, variables, control flow structures, defining and structuring code in functions and creating and loading modules. 

## Preparations

The course materials consist of Jupyter Notebooks. A Jupyter notebook is an interactive Python environment allowing to combine interactive execution of code along with formatted description texts, like an enriched, interactive lecture manuscript.

### Option 1: Install Anaconda on your machine

**In case you prefer to use Jupyter Hub (in case you have university login credentials), you can skip this setup section.** If you'd like to write and test your code independently from the university infrastructure and start from scratch, install the Jupyter environment locally on your machine, following the instructions below:

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

### Option 2: Use JupyterHub from within the university intranet

**If you're already connected via Wifi to eduroam or via LAN in the university,** you can access the JupyterHub, a Jupyter Notebook server runnning in the university cloud. As a student or employee of the university, you can use your default login credentials to login here
    
[https://apphub.wolke.uni-greifswald.de/](https://apphub.wolke.uni-greifswald.de/)

**then login with your credentials and choose "Datascience" as server type.**
    
### Option 3: Use JupterHub remotely from home or anywhere else
    
**If you are not connected to eduroam - or - if you're working from home**, you have to install and setup a VPN client. Follow [these](https://rz.uni-greifswald.de/en/services/technical-infrastructure/vpn/) instructions to install and setup the VPN client for the university of Greifswald  before you can use the JupyterHub in the university cloud. **In any case you need the university login credentials to have VPN access to the university intranet.**
    
### Download the course materials
    
**If you're using the JupyterHub**, either open a new Python 3 notebook and copy the lines
    
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

In order to follow the github crash course being part of this seminar, you should have your own github account. If you don't have one, signup beforehand.
