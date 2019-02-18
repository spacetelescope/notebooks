#!/bin/bash

if [[ ! -d /home/circleci/miniconda ]]; then
    wget https://repo.continuum.io/miniconda/Miniconda3-latest-OSX-x86_64.sh -O miniconda.sh &&
    bash miniconda.sh -b -f -p /home/circleci/miniconda;
else
    echo "Using cached miniconda";
fi
source ~/miniconda/bin/activate root
conda config --set always_yes yes
conda update -q conda
conda config --add channels astropy-ci-extras
conda config --add channels astropy
conda config --add channels http://ssb.stsci.edu/astroconda
conda install -n root conda-build
pip install ./requirements.txt
pip install --pre astroquery
