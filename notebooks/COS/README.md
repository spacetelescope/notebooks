# COS Notebooks

## Jupyter Notebook Walkthroughs of Cosmic Origins Spectrograph (COS) Data Processing
The [Cosmic Origins Spectrograph](https://www.stsci.edu/hst/instrumentation/cos) (COS) is an instrument on the [Hubble Space Telescope](https://www.stsci.edu/hst/about) (HST).
This is a repository of interactive walkthrough guides to common COS data procedures. It is intended for any and all COS data users: from undergraduates, to professional astronomers, to the general public.

#### 1. [Currently Operational Notebooks](#ch1)
#### 2. [Basic Requirements](#ch2)
#### 3. [Getting Help](#ch3)

---
<a id=ch1></a>
## Currently Operational Notebooks

If you don't want to run the notebooks for yourself but just want to see rendered html versions of the notebooks, *(with outputs,)* you may use the rendered `html` file.

|Name|Topic|Notebook file (`ipynb`)|Rendered file (`html`)|
|-|-|-|-|
|Setup|Setting up an environment to work with COS data|[Setup.ipynb](https://github.com/nkerman/notebooks/blob/main/notebooks/COS/Setup/Setup.ipynb)|[Setup.html](https://spacetelescope.github.io/COS-Notebooks/Setup.html)|
|DataDl|Downloading COS Data from the archive|[DataDl.ipynb](https://github.com/nkerman/notebooks/blob/main/notebooks/COS/DataDl/DataDl.ipynb)|[DataDl.html](https://spacetelescope.github.io/COS-Notebooks/DataDl.html)|
|ViewData|Beginning to work with COS data in Python: *plotting, binning, calculating SNR, & evaluating* a spectrum|[ViewData.ipynb](https://github.com/nkerman/notebooks/blob/main/notebooks/COS/ViewData/ViewData.ipynb)|[ViewData.html](https://spacetelescope.github.io/COS-Notebooks/ViewData.html)|
|AsnFile|Modifying or creating an association file|[AsnFile.ipynb](https://github.com/nkerman/notebooks/blob/main/notebooks/COS/AsnFile/AsnFile.ipynb)|[AsnFile.html](https://spacetelescope.github.io/COS-Notebooks/AsnFile.html)|
|CalCOS|Running the COS pipeline ([CalCOS](https://hst-docs.stsci.edu/cosdhb/chapter-3-cos-calibration))|[CalCOS.ipynb](https://github.com/nkerman/notebooks/blob/main/notebooks/COS/CalCOS/CalCOS.ipynb)|[CalCOS.html](https://spacetelescope.github.io/COS-Notebooks/CalCOS.html)|
|DayNight|Filtering out COS data taken during the day or night|[DayNight.ipynb](https://github.com/nkerman/notebooks/blob/main/notebooks/COS/DayNight/DayNight.ipynb)|[DayNight.html](https://spacetelescope.github.io/COS-Notebooks/DayNight.html)|
|LSF|Working with the COS Line Spread Function (LSF)|[LSF.ipynb](https://github.com/nkerman/notebooks/blob/main/notebooks/COS/LSF/LSF.ipynb)|[LSF.html](https://spacetelescope.github.io/COS-Notebooks/LSF.html)|
|Extract|Editing the extraction boxes in a BOXCAR-method spectral extraction file (XTRACTAB)|[Extract.ipynb](https://github.com/nkerman/notebooks/blob/main/notebooks/COS/Extract/Extract.ipynb)|[Extract.html](https://spacetelescope.github.io/COS-Notebooks/Extract.html)|

##### For notebooks with exercises, you can find worked solutions at the end of the notebook.


<a id = ch2></a>
## Basic Requirements



### Downloading the notebooks

While you *can* run most of the notebooks with only the `ipynb` file downloaded, it is **highly recommended that you clone this entire repository**. Specifically, `ViewData.ipynb` cannot run at present without both the `Scripts` and `ViewData` subdirectories installed side-by-side. To clone (which means download in the language of `git`) the repository with all the COS notebooks, run the following command from a terminal as shown in this [video walkthrough](https://vimeo.com/548158095):

```bash
git clone https://github.com/spacetelescope/notebooks
```

### Using Jupyter Notebooks
If you have never used Jupyter/IPython Notebooks before, please see the [Jupyter/IPython Notebook Quick Start Guide](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/).

#### Installing Jupyter

You need to be able to run Jupyter Notebooks and install python packages. If you don't have Jupyter installed, continue reading, or see the [Jupyter Docs](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html) for much more detailed installation instructions.

If you have `pip` or `conda` installed:


|`pip`|`conda` (**preferred**)|
|-----|--------------------------------|
|`pip install jupyterlab`|`conda install -c conda-forge jupyterlab`|


If you don't have the `conda` tool: 

We recommend installing either the Anaconda or Minicoda distributions. See [this page](https://astroconda.readthedocs.io/en/latest/getting_started.html#getting-started-jump) for instructions, and install either of the following: 

|Conda Distribution (with link to download)|Short Description|Size|
|-|-|-|
|[`anaconda` Distribution](https://docs.anaconda.com/anaconda/install/) | More beginner friendly, with lots of extras you likely won't use| \~ 3 GB|
|[`miniconda` Distribution](https://docs.conda.io/en/latest/miniconda.html)| Bare-bones conda distribution, which allows you to download only what you need|\~ 400 MB|

These will install the conda command line tool, allowing you to run: 

```bash
conda install -c conda-forge jupyterlab
``` 

#### Running Jupyter

From a new terminal (*make sure that the current working directory encompasses your notebook directory*), simply run either:

`jupyter notebook` to begin a notebook kernel (*recommended for new users*)

*OR*

`jupyter lab` to begin a lab kernel (*more versatile for advanced users*)

Either of the previous commands should open up a new window in your default web browser (with an address like `localhost:8888/`). From there you can navigate to a notebook and open it.

If you don't have experience installing packages, you should begin with our **introductory notebook** [Setup.ipynb](https://github.com/nkerman/notebooks/blob/main/notebooks/COS/Setup/Setup.ipynb) on setting up an environment for running astronomical Python code. If you do not yet have Jupyter up-and-running, you can read the pre-rendered (`.html`) version [here](https://spacetelescope.github.io/COS-Notebooks/Setup.html).

<a id = ch3></a>
## Getting Help

If you have an issue using these notebooks which you cannot fix, or if believe you have discovered an error in a notebook, please reach out to the [HST Help Desk](https://stsci.service-now.com/hst) or to the notebook's primary author: <nkerman@stsci.edu>.

---

