#!/bin/bash

apt-get update
apt-get install build-essential gcc-4.8 -y
conda info --envs
conda env update --file=environment.yml
source activate notebooks_env
conda info --envs
