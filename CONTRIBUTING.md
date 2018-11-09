# How to contribute spacetelescope notebooks

Contributions are welcome from both inside and outside the institute.

1. Read over the [spacetelescope notebook style guide](https://github.com/spacetelescope/style-guides/blob/master/guides/jupyter-notebooks.md). These are guidelines and are it is not always necessary to follow them to the letter, but contributions are expected to generally follow this guide.
2. Fork this repository
3. Create your feature branch to add or modify content (`git checkout -b my-new-feature`)
4. Make your changes, and then add them (`git add path/to/my/notebook.ipynb`,  `git commit -m 'Added some feature'`)
5. Push to the branch (`git push origin my-new-feature`)
6. Create a new Pull Request using the GitHub web site.

Once you've created a Pull Request, the CI tests will run on your changes.  These ensure that the notebook actually runs, and enforce some of the important elements of "notebook hygine" referenced in the style guide (e.g., not committing notebooks that have been executed).