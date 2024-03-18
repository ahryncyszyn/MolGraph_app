# MolGraph - Molecular Insight & Graph Conversion Tool

MolGraph is an app that can convert .xyz file(s) into a database containing each molecule as a graph. Further, it provides functionalities like calculating the molecular weight or plotting a selected molecule.

## Features

**Support for any .xyz format**: Distinguishes between multiple molecules stored within one .xyz file. \
**Graph Conversion**: Calculates locations of bonds based on atom coordinates and saves the molecule as a graph. \
**Molecular Weight Calculation**: Calculates the molecular weight of a selected molecule. \
**Visualization**: Plots the molecular structure of a selected molecule. 

## Installation

The code can be cloned locally to your device using:

```
git clone https://github.com/ahryncyszyn/MolGraph.git
```

All of the required libraries can be installed from the requirements.txt file located in .config directory. It can be achieved by executing this line in your command window:

```
pip install -r /path/to/.config/requirements.txt
```

Alternatively, you can create a virtual enviroment and install the libraries there, for example using:

```
python -m venv <venv_name>

source <venv_name>/bin/activate               #for Mac/Linux systems
source <venv_name>/Scripts/activate           #for Windows

pip install -r requirements.txt
```

## Usage

1. Clone the repository to your local machine.
2. Make sure you have the required libraries or install them using the command above
3. Run the main.py file using Python
4. Follow the on-screen instructions to select .xyz files, calculate molecular weights, or plot molecules.
