# COS-Notebooks

## Jupyter Notebooks of COS Data Processing Walkthroughs
Interactive walkthrough guides to common COS data procedures for PIs and other COS data users.

#### 1. [Abstract](#abs)
#### 2. [Basic Requirements](#ch2)
#### 3. [Currently Operational Notebooks](#ch3)
---
<a id = abs></a>
***Abstract***

1.  The **goal** of this project is to produce *Jupyter Notebooks* presenting walkthroughs of common data analysis procedures for data from the Cosmic Origins Spectrograph (COS).

2.  The **users/beneficiaries** of these notebooks will be users of COS data - PIs, graduate students, undergraduates, the public - who want to work with existing COS data.

    1.  These notebooks will intertactively teach the user to view a COS spectrum, re-bin COS data, combine COS FUV and NUV spectra into a master UV spectrum, etc.
    2.  They will also aim to *teach* the user how to determine the best parameters for a given procedure - i.e. choosing which binning they should apply to their data. This will primarily be done with optional exercises throughout the notebooks.
---
<a id = ch2></a>
## Basic Requirements
You need to be able to run Jupyter Notebooks and install python packages. If you don't have Jupyter installed, continue reading, or see the [Jupyter Docs](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html) for much more detailed installation instructions.

If you have `pip` or `conda` installed:
|`pip`|`conda` (**strongly preferred**)|
|-|-|
|`pip install jupyterlab`|`conda install -c conda-forge jupyterlab`|

If you don't have the `conda` tool: 

We recommend installing either the Anaconda or Minicoda distributions. See [this page](https://astroconda.readthedocs.io/en/latest/getting_started.html#getting-started-jump) for instructions, and install either of the following: 
- [`anaconda` - more beginner friendly, \~ 3 GB, lots of extras you likely won't use](https://docs.anaconda.com/anaconda/install/) 
- [`miniconda` - \~ 400 MB, only what you need](https://docs.conda.io/en/latest/miniconda.html).

These will install the conda command line tool, allowing you to run `conda install -c conda-forge jupyterlab`. 

Next, if you don't have experience installing packages, you should begin with our notebook on setting up an [environment for running astronomical code](https://github.com/spacetelescope/COS-Notebooks/blob/master/Setup/Setup.ipynb).

---
<a id = ch3></a>
## Currently Operational Notebooks
- [Setup.ipynb](https://github.com/spacetelescope/COS-Notebooks/blob/master/Setup/Setup.ipynb)
- [DataDL.ipynb](https://github.com/spacetelescope/COS-Notebooks/blob/master/DataDL/DataDl.ipynb)
- [ViewData.ipynb](https://github.com/spacetelescope/COS-Notebooks/blob/master/ViewData/ViewData.ipynb)
- [Calcos.ipynb](https://github.com/spacetelescope/COS-Notebooks/blob/master/Calcos/Calcos.ipynb)
