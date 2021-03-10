#!/bin/bash
echo "A Temporary copy of all notebooks will be kept in ~/Desktop/.temp.nosync/clear"
for bn in $(cat ./nb_list.txt); do
    mkdir -p ~/Desktop/.temp.nosync
    mkdir -p ~/Desktop/.temp.nosync/clear
    mkdir -p ~/Desktop/.temp.nosync/render
    echo Running RENDER for ../$bn/$bn.ipynb
    cp ../$bn/$bn.ipynb ~/Desktop/.temp.nosync/clear
    jupyter-nbconvert --to html ../$bn/$bn.ipynb --output-dir=~/Projects/temp_renders
done