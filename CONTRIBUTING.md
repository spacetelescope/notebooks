# How to contribute spacetelescope notebooks

Contributions are welcome from both inside and outside the institute.

1. Read over the [spacetelescope notebook style guide](https://github.com/spacetelescope/style-guides/blob/master/guides/jupyter-notebooks.md). The style parts are guidelines and it is not always necessary to follow them to the letter, but contributions are expected to generally follow this guide.  However the layout and data rules in general should be followed to ensure this repository stays consistent.
2. Fork this repository. See the preferred method of doing this on the [workflow page](https://github.com/spacetelescope/style-guides/blob/master/guides/git-workflow.md).
3. Create a feature branch to add or modify content (`git checkout -b my-new-feature`).  You should aim to do one branch (and therefore one Pull Request) per notebook, as that will make review faster and easier. 
4. Create your notebook. It can be anywhere within the `notebooks` directory or any level of sub-directory, but each notebook should be in its *own* directory with no other notebooks or other files. See [the Jupyter Notebook template](https://github.com/spacetelescope/notebooks/tree/master/notebooks/MAST/templates/jupyter_template/jupyter_template.ipynb) for an idea of how to get started.
5. Develop your notebook by adding and committing it (`git add path/to/my/notebook/notebook.ipynb`,  `git commit -m 'Added some feature'`), as many times as necessary to capture your development history.  Note that you should *never* commit a notebook with executed cells or commit large data files (see the guide).  Always "Clear Ouputs" on cells before adding/committing.
6.  Add a ``requirements.txt`` file next to your notebook.  Each line should be a separate package following `pip` [requirements file conventions](https://pip.pypa.io/en/stable/reference/pip_install/#requirement-specifiers), listing all the required packages for your notebook, including a "known good version" (e.g., if you wrote the notebook on numpy v1.14.0, the line should be ``numpy>=1.14.0``).
    - **A note on supplemental files:** 
        - Including supplemental files with your notebook is discouraged, and should only occur if the files are not accessible online (e.g. via MAST).
        - See the [style guide](https://github.com/spacetelescope/style-guides/blob/master/guides/where-to-put-your-data.md) for more detailed guidance on how to handle supplemental data.
        - If you do need to add additional files, however, be sure to add that file name to the "Exceptions committed to repo" list within ``notebooks/notebooks/.gitignore``. For example, if you need to add ``diagram.jpg`` to your notebook ``DrizzlePac/sky_matching``, then add ``!DrizzlePac/sky_matching/diagram.jpg`` to the ``.gitignore`` list (don't forget the ``!``). Otherwise, git won't recognize your file. 
7. Push to your github fork's branch (`git push origin my-new-feature`)
8. Create a new Pull Request from your fork into `spacetelescope` using the GitHub web site.  Be sure to include a description that's sufficient for someone *not in your team* to understand the context of the notebook (not all reviewers will be from your team.)

Once you've created a Pull Request, the CI tests will run on your changes.  These ensure that the notebook actually runs, and enforce some of the important elements of "notebook hygine" referenced in the style guide (e.g., not committing notebooks that have been executed).

# Squashing (or: what to do if you accidentally committed data)

As the [style guide](https://github.com/spacetelescope/style-guides/blob/master/guides/jupyter-notebooks.md) outlines (and the tests check for), it is not desirable to include large data files or executed cells with the notebooks because it can sometimes cause the repository to grow quickly to an unmanagable size. However, because git tracks such changes, simply deleting them and making a commit is not sufficient - the data files are "hidden" and not deleted (they therefore continue to bloat the repository). To truly remove accidentally-committed data requires "rewriting history".  There are two ways to do this - an easy (but information-destroying) version, and a harder (but more "correct") version.

## The Better Way

Git allows re-writing history using the `git rebase` command, and this is generally the best way to address the above problem. In particular, it has the advantage that it maintains the development history of a notebook.  If your committed data is a file (as opposed to part of the notebook itself) this step is relatively easy:

1. Start from your working branch (i.e., where you are developing the notebook)
2. Create a commit that deletes the data (`git rm <filetobedeleted>`, `git commit -m "deleted file"`).  Record that SHA.
3. Determine the commit where you introduced the data in the first place, and record/remember the SHA of the commit (usually most easily found via `git log`).
4. Start an interactive rebase up to the commit just *before* the one you just determined.  This is best done using the `^` trick in git (which basically means "the commit before that one").  For example, if the SHA you introduced the file in is abc123, you would do `git rebase -i abc123^`
5. This will pop up a text editor.  Identify the commit where you deleted the file, and move that line to right *after* the commit where you introduced the file.  Also change the word "pick" next to the deleting commit to "squash".
6. Git will think for a minute then show you a new commit message.  Edit as you feel appropriate (Usually you can just delete the "deleted file" part), then save/exit to complete the rebasing.  
7. You now have a cleaned up commit with the file expunged from your history.  You will now need to `git push origin my-new-feature -f` (or whatever the name of your branch is), and your GitHub PR will be updated with the new history.

If you have executed a *cell* in a notebook, the steps are related, but somewhat different, because those changes might conflict with *later* changes in your notebook. So while the above might work, if you run into trouble, the alternate approach might be better
1. Do steps 1, 3, and 4 above
2. Change the "pick" text next to the offending commit (should be the top-most one) to "edit".  When you save and close your editor git will run for a bit and then stop on the commit in question asking you to make changes.
3. Open up the notebook in Jupyter (be sure to refresh if your browser window is open from previous edits), and do a "Clear All Cells". Don't forget to save!
4. "Amend" the commit with the change you just made: `git add <yournotebook.ipynb>`, `git commit --amend` (it will automatically include the earlier changelog text which you can modify if you wish).
5. `git rebase --continue`
6. If you have commits that conflict, you'll need to fix those.  You may find it easier to use a text editor rather thean Jupyter itself, as the conflicts can make Jupyter not correctly read the file. When you hit a conflict you'll need to  `git add <yournotebook.ipynb>` and `git rebase --continue`.
7. Once git says it has successfully completed the rebase, you can finish off with step 7 above.


## The Easy Way

If you (the contributor) are not confident in your ability to execute the steps above (or cannot find someone to help guide you through them), there is a simpler approach available.  You will still need to include a commit that deletes the data, as described in the above. However, instead of needing to rewrite your own history, GitHub allows a merge to automatically "squash" all the commits of a branch (i.e., a Pull Request) into a single commit.  This has the disadvantage of erasing the development history completely (i.e., there is only one commit for the whole branch), but is easy to implement: when the Pull Request is ready, all the maintainer needs to do is click the downward-pointing arrow next to "Merge pull request", choose "Squash and merge", and then merge.

Note that it is important that you double-check that the *other* tests in a Pull Request have passed.  That is, this technique only addresses the "accidentally committed data" problem, and the other tests still must pass for the notebook site to correctly build after the merge.
