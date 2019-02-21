# Notebooks

[![Build Status](https://travis-ci.com/spacetelescope/notebooks.svg?branch=master)](https://travis-ci.com/spacetelescope/notebooks)

This repository contains a curated set of Jupyter notebooks related to the work that we do at STScI. These notebooks follow a consistent [style guide](https://github.com/spacetelescope/style-guides/blob/master/guides/jupyter-notebooks.md) in terms of layout/structure, coding conventions etc.

These notebooks are also under continuous integration to ensure that astronomers using these notebooks have a high level of confidence that they will work.

## Contents

This repository holds the notebooks themselves, but in a harder-to-read unexecuted form. If you want to view the notebooks online, you should view [the rendered versions](https://spacetelescope.github.io/notebooks).  At present this includes:
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
    * [Kepler Lightcurve](https://spacetelescope.github.io/notebooks/notebooks/MAST/Kepler/Kepler_Lightcurve/kepler_lightcurve.html)
    * [Kepler TPF](https://spacetelescope.github.io/notebooks/notebooks/MAST/Kepler/Kepler_TPF/kepler_tpf.html)
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


### Building Locally

Alternatively, if you would like to execute the notebooks and view them locally, you can clone this repo and do ``python convert.py``. This requires the [nbpages](https://github.com/eteq/nbpages) python package, which you can most easily install by doing ``pip install -e git+https://github.com/eteq/nbpages.git#egg=nbpages``.

## Contributing

If you want to suggest changes to this content (or new content!), check out the [contributing guide](CONTRIBUTING.md).
