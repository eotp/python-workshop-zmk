# Materials for a Python workshop series at Charité - Universitätsmedizin Berlin, Department of Restorative and Preventive Dentistry 

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/eotp/workshop-data-science-CODE/master)


Preliminary dates
* Part 1: October 18<sup>th</sup> and 19<sup>th</sup>, 2018
* Part 2: _tba_
* Part 3: _tba_


This repository contains materials for a series of workshops on __Python and Python for Data Science__ hosted at [Charité - Universitätsmedizin Berlin](https://zahnerhaltung.charite.de/en/), Germany.

In order to re-run the workshop materials we encourage you to use the [conda](https://conda.io/docs/) package manager. Once installed, create an environment and install all required dependencies on your machine by typing 

`conda env create -f environment.yml`

into your console. You activate your new environment by typing 

`source activate python-charite` (on LINUX and Mac) or

`activate python-charite` (on WINDOWS). 

Then you are ready to go (if you are stuck check out the [conda documentation site](https://conda.io/docs/user-guide/tasks/manage-environments.html#)). Alternatively, you may launch [binder](https://mybinder.org/) to get a reproducible executable environment immediately in your browser. Simply click the _launch binder_ icon in the upper left corner, or go [here](https://mybinder.org/v2/gh/eotp/workshop-data-science-CODE/master).


***

## Content

The workshops focus on Python and its usage for scientific applications. 

### Part 1

* Getting started with Python
  * Introduction to scientific computing with Python
  * Python and Python´s scientific stack
  * IDE´s and the Jupyter ecosystem

* Python 101
  * Objects
  * Operations
  * Functions
  * Methods
  * Indexing and Slicing
  * Collections
  * Loops
  * Control Flow
  * I/O
  * User-defined functions
  * Code refactoring


### Part 2

* Data science, statistics and predictive modeling
  * Processing of tabular data
  * Exploratory Data Analysis 
  * Plotting with Python
  * Statistics
    * Univariate statistics
    * Multivariate statistics
    * Confidence intervals and bootstrapping
    * Hypotheses tests    
  * Predictive modeling
    * Regression
    * Classification
    * Model tuning
  
  
### Part 3

* Applied scientific computing and problem solving. 
_The specific content for part 3 is yet to be determined. We aim to help the participants to tackle their particular research questions using Python._

***

All data sets, all code snippets, all [Jupyter](http://jupyter.org/) notebooks and the `environment.yml` file for reproducibility are available through this self contained repository.

The structure of this repository is outlined below:

    python-charite
    │.git                  # git internals
    │.gitignore            # specify files/folders to be ignored by git
    └───datasets
    │   │...               # find all the raw data files
    └───figures
    │   │...               # saved figures go here
    └───notebooks
    │   └───_img
    │   │   │...           # rendered images are placed here
    │   │...               # find all Jupyter notebooks here
    │
    │README.md
    │LICENSE   
    │environment.yml       # conda environment specifications for reproducibility
    └───src
        │...               # here go the code snippets and scripts
        └───_solutions
            │...           # solutions for coding challenges (don't cheat yourself ;-))


 ***
 
 




