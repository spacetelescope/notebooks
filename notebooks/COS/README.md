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

    1.  These notebooks will interactively teach the user to view a COS spectrum, re-bin COS data, combine COS FUV and NUV spectra into a master UV spectrum, etc.
    2.  They will also aim to *teach* the user how to determine the best parameters for a given procedure - i.e. choosing which binning they should apply to their data. This will primarily be done with optional exercises throughout the notebooks.
---
<a id = ch2></a>
## Basic Requirements

If you have never used Jupyter/IPython Notebooks before, please see the [Jupyter/IPython Notebook Quick Start Guide](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/).

While you *can* run most of the notebooks at present on their own, it is **highly recommended that you clone this entire repository**. Specifically, *ViewData.ipynb* cannot run at present without both the *Scripts* and *ViewData* subdirectories installed side-by-side.

You need to be able to run Jupyter Notebooks and install python packages. If you don't have Jupyter installed, continue reading, or see the [Jupyter Docs](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html) for much more detailed installation instructions.

If you have `pip` or `conda` installed:


|`pip`|`conda` (**strongly preferred**)|
|-----|--------------------------------|
|`pip install jupyterlab`|`conda install -c conda-forge jupyterlab`|


If you don't have the `conda` tool: 

We recommend installing either the Anaconda or Minicoda distributions. See [this page](https://astroconda.readthedocs.io/en/latest/getting_started.html#getting-started-jump) for instructions, and install either of the following: 

|Conda Distribution (with link to download)|Short Description|Size|
|-|-|-|
|[`anaconda` Distribution](https://docs.anaconda.com/anaconda/install/) | More beginner friendly, with lots of extras you likely won't use| \~ 3 GB|
|[`miniconda` Distribution](https://docs.conda.io/en/latest/miniconda.html)| Bare-bones conda distribution, which allows you to download only what you need|\~ 400 MB|

These will install the conda command line tool, allowing you to run `conda install -c conda-forge jupyterlab`. 

Next, if you don't have experience installing packages, you should begin with our notebook [Setup.ipynb](https://github.com/spacetelescope/COS-Notebooks/blob/master/Setup/Setup.ipynb) on setting up an [environment for running astronomical code](https://github.com/spacetelescope/COS-Notebooks/blob/master/Setup/Setup.ipynb), or read the pre-rendered version [here](https://spacetelescope.github.io/COS-Notebooks/Setup.html).

---
<a id = ch3></a>
## Currently Operational Notebooks

If you don't want to run the notebooks for yourself but just want to see rendered html versions of the notebooks *(with outputs)* check out the html render.

|Name|Topic|Notebook file (`ipynb`)|Rendered file (`html`)|
|-|-|-|-|
|Setup|Setting up an environment to work with COS data|[Setup.ipynb](https://github.com/spacetelescope/COS-Notebooks/blob/master/Setup/Setup.ipynb)|[Setup.html](https://spacetelescope.github.io/COS-Notebooks/Setup.html)|
|DataDl|Downloading COS Data from the archive|[DataDl.ipynb](https://github.com/spacetelescope/COS-Notebooks/blob/master/DataDl/DataDl.ipynb)|[DataDl.html](https://spacetelescope.github.io/COS-Notebooks/DataDl.html)|
|ViewData|Beginning to work with COS data in Python|[ViewData.ipynb](https://github.com/spacetelescope/COS-Notebooks/blob/master/ViewData/ViewData.ipynb)|[ViewData.html](https://spacetelescope.github.io/COS-Notebooks/ViewData.html)|
|AsnFile|Modifying or creating an association file|[AsnFile.ipynb](https://github.com/spacetelescope/COS-Notebooks/blob/master/AsnFile/AsnFile.ipynb)|[AsnFile.html](https://spacetelescope.github.io/COS-Notebooks/AsnFile.html)|
|CalCOS|Running the COS pipeline ([CalCOS](https://hst-docs.stsci.edu/cosdhb/chapter-3-cos-calibration))|[CalCOS.ipynb](https://github.com/spacetelescope/COS-Notebooks/blob/master/CalCOS/CalCOS.ipynb)|[CalCOS.html](https://spacetelescope.github.io/COS-Notebooks/CalCOS.html)|
|DayNight|Filtering out COS data taken during the day or night|[DayNight.ipynb](https://github.com/spacetelescope/COS-Notebooks/blob/master/DayNight/DayNight.ipynb)|[DayNight.html](https://spacetelescope.github.io/COS-Notebooks/DayNight.html)|
|LSF|Working with the COS Line Spread Function (LSF)|[LSF.ipynb](https://github.com/spacetelescope/COS-Notebooks/blob/master/LSF/LSF.ipynb)|[LSF.html](https://spacetelescope.github.io/COS-Notebooks/LSF.html)|
|Extract|Editing the extraction boxes in a spectral extraction file (XTRACTAB)|[Extract.ipynb](https://github.com/spacetelescope/COS-Notebooks/blob/master/Extract/Extract.ipynb)|[Extract.html](https://spacetelescope.github.io/COS-Notebooks/Extract.html)|

##### For notebooks with exercises, you can find worked solutions at the end of the notebook.
