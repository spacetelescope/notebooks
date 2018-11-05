# Notebooks

NOTE: this is a work-in-progress re-write of the layout of this repo.  If you are seeing this message and aren't sure whhy probably you are on the wrong branch - try master...

This repository contains a curated set of Jupyter notebooks related to the work that we do at STScI. These notebooks follow a consistent<sup>\*</sup> [style guide]( https://github.com/spacetelescope/style-guides/issues/2) in terms of layout/structure, coding conventions etc.

These notebooks are also under continuous integration<sup>\*</sup> to ensure that astronomers using these notebooks have a high level of confidence that they will work.

## Contents

- [MAST](https://archive.stsci.edu/)
  - [API Functionality Demo](MAST/astroquery_functionality_demo.ipynb)
  - Kepler/K2
    - [Kepler Lightcurves](MAST/Kepler/Kepler_Lightcurve/kepler_lightcurve.ipynb)
    - [Kepler Target Pixel Files (TPF)](MAST/Kepler/Kepler_TPF/kepler_tpf.ipynb)
    - [Kepler Full Frame Images (FFI)](MAST/Kepler/Kepler_FFI/kepler_ffi.ipynb)
  - TESS
    - [TESS API Demo](MAST/TESS/tess_api_demo.ipynb)
    - [TESS TIC API Demo (no astroquery)](MAST/TESS/tess_tic_api_demo.ipynb)
    - [TESS TIC Search for Dwarf Stars Around HD 209458](MAST/TESS/tess_tic_search_for_dwarf_stars_around_hd_209458.ipynb)
- HST
  - ACS
  - COS
  - STIS
  - WFC3
- JWST
  - NIRCam
  - NIRSpec
  - MIRI
  - NIRISS

## TODO

<sup>\*</sup> Make sure what is said above is true. This project follows the principle of [README driven development](http://tom.preston-werner.com/2010/08/23/readme-driven-development.html), i.e. we have written the README describing the future we would like to see for this project.


## Contributing

If you want to suggest changes to this content do the following:

1. Take a look at the contributing guide
2. Fork it
3. Create your feature branch (`git checkout -b my-new-feature`)
4. Commit your changes (`git commit -am 'Added some feature'`)
5. Push to the branch (`git push origin my-new-feature`)
6. Create new Pull Request
