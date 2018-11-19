# How to contribute spacetelescope notebooks

Contributions are welcome from both inside and outside the institute.

1. Read over the [spacetelescope notebook style guide](https://github.com/spacetelescope/style-guides/blob/master/guides/jupyter-notebooks.md). The style parts are guidelines and it is not always necessary to follow them to the letter, but contributions are expected to generally follow this guide.  However the layout and data rules in general should be followed to ensure this repository stays consistent.
2. Fork this repository
3. Create your feature branch to add or modify content (`git checkout -b my-new-feature`)
4. Create your notebook. It can be anywhere within the `notebooks` directory or any level of sub-directory, but each notebook should be in its *own* directory with no other notebooks or other files.
5. Develop your notebook by adding and committing it (`git add path/to/my/notebook/notebook.ipynb`,  `git commit -m 'Added some feature'`), as many times as necessary to capture your development history.  Note that you should *never* commit a notebook with executed cells or commit large data files (see the guide).  Always "Clear Ouputs" on cells before adding/committing.
6.  Add a ``requirements.txt`` file next to your notebook.  Each line should be a separate package following `pip` [requirements file conventions](https://pip.pypa.io/en/stable/reference/pip_install/#requirement-specifiers), listing all the required packages for your notebook, including a "known good version" (e.g., if you wrote the notebook on numpy v1.14.0, the line should be ``numpy>=1.14.0``).
7. Push to your github fork's branch (`git push origin my-new-feature`)
8. Create a new Pull Request from your fork into `spacetelescope` using the GitHub web site.

Once you've created a Pull Request, the CI tests will run on your changes.  These ensure that the notebook actually runs, and enforce some of the important elements of "notebook hygine" referenced in the style guide (e.g., not committing notebooks that have been executed).
