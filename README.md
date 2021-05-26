# Notebooks

[![CircleCI](https://circleci.com/gh/spacetelescope/notebooks/tree/master.svg?style=svg)](https://circleci.com/gh/spacetelescope/notebooks/tree/master)

This repository contains a curated set of Jupyter notebooks related to the work that we do at STScI. These notebooks follow a consistent [style guide](https://github.com/spacetelescope/style-guides/blob/master/guides/jupyter-notebooks.md) in terms of layout/structure, coding conventions etc.

These notebooks are also under continuous integration to ensure that astronomers using these notebooks have a high level of confidence that they will work.

## Contents

This repository holds the notebooks themselves, but in a harder-to-read unexecuted form. If you want to view the notebooks online, you should view [the rendered versions](https://spacetelescope.github.io/notebooks).  At present this includes:
* COS
  * [Setting up your computer environment to work with COS data](https://spacetelescope.github.io/COS-Notebooks/Setup.html)
  * [Downloading COS Data from the archive](https://spacetelescope.github.io/COS-Notebooks/DataDl.html)
  * [Beginning to work with COS data in Python: *plotting, binning, calculating SNR, & evaluating* a spectrum](https://spacetelescope.github.io/COS-Notebooks/ViewData.html)
  * [Modifying or creating an association file](https://spacetelescope.github.io/COS-Notebooks/AsnFile.html)
  * [Running the COS pipeline (CalCOS)](https://spacetelescope.github.io/COS-Notebooks/CalCOS.html)
  * [Filtering out COS data taken during the day or night](https://spacetelescope.github.io/COS-Notebooks/DayNight.html)
  * [Working with the COS Line Spread Function (LSF)](https://spacetelescope.github.io/COS-Notebooks/LSF.html)
  * [Editing the extraction boxes in a BOXCAR-method spectral extraction file (XTRACTAB)](https://spacetelescope.github.io/COS-Notebooks/Extract.html)
* DrizzlePac
  * [Initialization](https://spacetelescope.github.io/notebooks/notebooks/DrizzlePac/Initialization/Initialization.html)
  * [Aligning HST images to an absolute reference catalog](https://spacetelescope.github.io/notebooks/notebooks/DrizzlePac/align_to_catalogs/align_to_catalogs.html)
  * [Aligning HST Mosaics](https://spacetelescope.github.io/notebooks/notebooks/DrizzlePac/align_mosaics/align_mosaics.html)
  * [Optimizing Image Alignment for Multiple HST Visits](https://spacetelescope.github.io/notebooks/notebooks/DrizzlePac/align_multiple_visits/align_multiple_visits.html)
  * [Aligning Deep Exposures of Sparse Fields](https://spacetelescope.github.io/notebooks/notebooks/DrizzlePac/align_sparse_fields/align_sparse_fields.html)
  * [Drizzling WFPC2 Images to use a Single Zeropoint](https://spacetelescope.github.io/notebooks/notebooks/DrizzlePac/drizzle_wfpc2/drizzle_wfpc2.html)
  * [Satellite Trail Masking Techniques](https://spacetelescope.github.io/notebooks/notebooks/DrizzlePac/mask_satellite/mask_satellite.html)
  * [Optimizing the Image Sampling](https://spacetelescope.github.io/notebooks/notebooks/DrizzlePac/optimize_image_sampling/optimize_image_sampling.html)
  * [Sky Matching](https://spacetelescope.github.io/notebooks/notebooks/DrizzlePac/sky_matching/sky_matching.html)
  * [Using DS9 Regions to Include and Exclude Sources in HST Image Alignment with TWEAKREG](https://spacetelescope.github.io/notebooks/notebooks/DrizzlePac/use_ds9_regions_in_tweakreg/use_ds9_regions_in_tweakreg.html)
* MAST
  * Hubble Source Catalog
    * [MAST Table Access Protocol Hubble Source Catalog Demo](https://spacetelescope.github.io/notebooks/notebooks/MAST/HSC/HSC_TAP/HSC_TAP.html)
  * Kepler
    * See [notebooks/MAST/Kepler/README.md](https://github.com/spacetelescope/notebooks/blob/master/notebooks/MAST/Kepler/README.md)
  * PanSTARRS
    * [PanSTARRS1 DR2 TAP Demo](https://spacetelescope.github.io/notebooks/notebooks/MAST/PanSTARRS/PS1_DR2_TAP/PS1_DR2_TAP.html)
  * TESS
    * [Beginner: Read and Plot A TESS Data Validation Timeseries File](https://spacetelescope.github.io/notebooks/notebooks/MAST/TESS/beginner_how_to_use_dvt/beginner_how_to_use_dvt.html)
    * [Beginner: Read and Display a TESS Full Frame Image](https://spacetelescope.github.io/notebooks/notebooks/MAST/TESS/beginner_how_to_use_ffi/beginner_how_to_use_ffi.html)
    * [Beginner: Read and Plot A TESS Light Curve File](https://spacetelescope.github.io/notebooks/notebooks/MAST/TESS/beginner_how_to_use_lc/beginner_how_to_use_lc.html)
    * [Beginner: Read and Display A TESS Target Pixel File](https://spacetelescope.github.io/notebooks/notebooks/MAST/TESS/beginner_how_to_use_tp/beginner_how_to_use_tp.html)
    * [Beginner: Search The TESS Input Catalog Centered On HD 209458](https://spacetelescope.github.io/notebooks/notebooks/MAST/TESS/beginner_tic_search_hd209458/beginner_tic_search_hd209458.html)
    * [Beginner: A Tour of the Contents of the TESS 2-minute Cadence Data](https://spacetelescope.github.io/notebooks/notebooks/MAST/TESS/beginner_tour_lc_tp/beginner_tour_lc_tp.html)
    * [Beginner: Cutout of the TESS FFIs using Astrocut and Astroquery](https://spacetelescope.github.io/notebooks/notebooks/MAST/TESS/interm_tesscut_astroquery/interm_tesscut_astroquery.html)
    * [Intermediate: Search and Download GI Program Light Curves](https://spacetelescope.github.io/notebooks/notebooks/MAST/TESS/interm_gi_query/interm_gi_query.html)
    * [Intermediate: Create TESS FFI Cutout using Python Requests](https://spacetelescope.github.io/notebooks/notebooks/MAST/TESS/interm_tesscut_requests/interm_tesscut_requests.html)


## Building Locally

Python 3 is required for use of these notebooks.

To quickly create an environment with everything needed to run and convert, please first install Conda or Miniconda to your machine using [Conda Installation Instructions](https://conda.io/projects/conda/en/latest/user-guide/install/index.html).

Once you have Conda installed, complete the following from a command line:

```bash
git clone https://github.com/spacetelescope/notebooks
cd notebooks
conda env create -f environment.yml
conda activate notebooks_env
python convert.py
```

Doing so will clone this repo, create and activate a conda environment with all needed dependencies, and convert the notebooks to html. For all current notebooks, this can take around 30 minutes.

After converting, you can access the converted HTML of the notebooks in each notebook directory. These can be opened in any web browser. You can also open the index.html file in the root of the repo after converting that links to all converted notebooks.

If you would like to view the notebooks in Jupyter, from the command line in the notebooks directory use:

```bash
jupyter notebook
```

Your web browser will open a new page and you can navigate the notebook directories and click the a notebook file (ends in .ipynb) to open.

## Contributing

If you want to suggest changes to this content (or new content!), check out the [contributing guide](CONTRIBUTING.md).
