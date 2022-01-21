# COS Notebooks 
*[Click here](https://spacetelescope.github.io/COS-Notebooks/) for the COS Notebooks website*

## Jupyter Notebook Walkthroughs of Cosmic Origins Spectrograph (COS) Data Processing
The [Cosmic Origins Spectrograph](https://www.stsci.edu/hst/instrumentation/cos) (COS) is an instrument on the [Hubble Space Telescope](https://www.stsci.edu/hst/about) (HST).
This is a repository of interactive walkthrough guides to common COS data procedures. It is intended for any and all COS data users: from undergraduates, to professional astronomers, to the general public.

#### 1. [Currently Operational Notebooks](#ch1)
#### 2. [Basic Requirements](#ch2)
#### 3. [Notes for those new to `Python`/`Jupyter`/Coding](#ch3)
#### 4. [Getting Help](#ch4)

---
<a id=ch1></a>
## Currently Operational Notebooks

If you don't want to run the Notebooks for yourself but just want to see rendered html versions of the Notebooks, *(with outputs,)* you may use the rendered `html` file.

|Name|Topic|Notebook file (`ipynb`)|Rendered file (`html`)|
|-|-|-|-|
|Setup|Setting up an environment to work with COS data|[Setup.ipynb](https://github.com/spacetelescope/notebooks/blob/master/notebooks/COS/Setup/Setup.ipynb)|[Setup.html](https://spacetelescope.github.io/COS-Notebooks/Setup.html)|
|DataDl|Downloading COS Data from the archive|[DataDl.ipynb](https://github.com/spacetelescope/notebooks/blob/master/notebooks/COS/DataDl/DataDl.ipynb)|[DataDl.html](https://spacetelescope.github.io/COS-Notebooks/DataDl.html)|
|ViewData|Beginning to work with COS data in Python: *plotting, binning, calculating SNR, & evaluating* a spectrum|[ViewData.ipynb](https://github.com/spacetelescope/notebooks/blob/master/notebooks/COS/ViewData/ViewData.ipynb)|[ViewData.html](https://spacetelescope.github.io/COS-Notebooks/ViewData.html)|
|AsnFile|Modifying or creating an association file|[AsnFile.ipynb](https://github.com/spacetelescope/notebooks/blob/master/notebooks/COS/AsnFile/AsnFile.ipynb)|[AsnFile.html](https://spacetelescope.github.io/COS-Notebooks/AsnFile.html)|
|CalCOS|Running the COS pipeline ([CalCOS](https://hst-docs.stsci.edu/cosdhb/chapter-3-cos-calibration))|[CalCOS.ipynb](https://github.com/spacetelescope/notebooks/blob/master/notebooks/COS/CalCOS/CalCOS.ipynb)|[CalCOS.html](https://spacetelescope.github.io/COS-Notebooks/CalCOS.html)|
|DayNight|Filtering out COS data taken during the day or night|[DayNight.ipynb](https://github.com/spacetelescope/notebooks/blob/master/notebooks/COS/DayNight/DayNight.ipynb)|[DayNight.html](https://spacetelescope.github.io/COS-Notebooks/DayNight.html)|
|SplitTag|Breaking COS TIME-TAG data into multiple sub-exposures|[SplitTag.ipynb](https://github.com/spacetelescope/notebooks/blob/master/notebooks/COS/SplitTag/SplitTag.ipynb)|[SplitTag.html](https://spacetelescope.github.io/COS-Notebooks/SplitTag.html)|
|LSF|Working with the COS Line Spread Function (LSF)|[LSF.ipynb](https://github.com/spacetelescope/notebooks/blob/master/notebooks/COS/LSF/LSF.ipynb)|[LSF.html](https://spacetelescope.github.io/COS-Notebooks/LSF.html)|
|Extract|Editing the extraction boxes in a BOXCAR-method spectral extraction file (XTRACTAB)|[Extract.ipynb](https://github.com/spacetelescope/notebooks/blob/master/notebooks/COS/Extract/Extract.ipynb)|[Extract.html](https://spacetelescope.github.io/COS-Notebooks/Extract.html)|

##### For Notebooks with exercises, you can find worked solutions at the end of the Notebook.


<a id = ch2></a>
## Basic Requirements

### Computer requirements
We have built these Notebooks to be cross-platform compatible; however they have been tested primarily on `Unix` and `Unix`-`like` systems, (i.e. **MacOS** and **Linux**). As such **Users may encounter issues when run on Windows computers**. If you are unable to run a particular Notebook from a Windows device, please reach out to us (see [Getting Help](#ch4)) and we will work to fix the problem. The first solution to try if the Notebooks are failing because of a Windows incompatibility is using the [Windows Sub-System for Linux](https://docs.microsoft.com/en-us/windows/wsl/) (WSL), which will allow you to run a Linux computer environment from your Windows device.


### Downloading the Notebooks

While you *can* run most of the Notebooks with only the `ipynb` file downloaded, it is **highly recommended that you clone this entire repository**. Specifically, `ViewData.ipynb` cannot run at present without both the file `cos_functions.py` and `ViewData` installed side-by-side in the same directory. To clone (which means download, in the language of `git`,) the repository with all the COS Notebooks, run the following command from a terminal in the directory where you would like to download the Notebook repository. 

```bash
git clone https://github.com/spacetelescope/notebooks
```

The git cloning process is also shown in [this video walkthrough](https://vimeo.com/548158095).

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

From a new terminal (*make sure that the current working directory encompasses your Notebook directory*), simply run either:

`jupyter notebook` to begin a Notebook kernel (*recommended for new users*)

*OR*

`jupyter lab` to begin a lab kernel (*more versatile for advanced users*)

Either of the previous commands should open up a new window in your default web browser (with an address like `localhost:8888/`). From there you can navigate to a Notebook and open it.

If you don't have experience installing packages, you should begin with our **introductory Notebook** [Setup.ipynb](https://github.com/spacetelescope/notebooks/blob/master/notebooks/COS/Setup/Setup.ipynb) on setting up an environment for running astronomical Python code. If you do not yet have Jupyter up-and-running, you can read the pre-rendered (`.html`) version [here](https://spacetelescope.github.io/COS-Notebooks/Setup.html).

<a id=ch3></a>
## Notes for those new to `Python`/`Jupyter`/Coding:

- You will frequently see exclamation points (**\!**) or dollar signs (**\$**) at the beginning of a line of code. These are not part of the actual commands. The exclamation points tell a Jupyter Notebook to pass the following line to the command line, and the dollar sign merely indicates the start of a terminal prompt. 
- Similarly, when a variable or argument in a line of code is surrounded by sharp brackets, like \<these words are\>, this is an indication that the variable or argument is something which you should change to suit your data.

- If you install the full Anaconda distribution with the [*Anaconda Navigator* tool](https://docs.anaconda.com/anaconda/navigator/), (see Section 1 of the `Setup.ipynb` Notebook) you will also have access to a graphical interface (AKA a way to use windows and a point-and-click interface instead of the terminal for installing packages and managing environments).
  
<a id = ch4></a>
## Getting Help

If you have an issue using these Notebooks which you cannot fix, or if believe you have discovered an error in a Notebook, please reach out to the [HST Help Desk](https://stsci.service-now.com/hst) or to the Notebook's primary author: <nkerman@stsci.edu>.

---
