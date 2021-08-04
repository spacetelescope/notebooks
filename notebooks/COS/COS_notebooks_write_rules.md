# Rules for writing to the [spacetelescope/notebooks GitHub repository](https://github.com/spacetelescope/notebooks/)

**Contributors:** Nat Kerman @nkerman, Marc Rafelski @mrafelski, Erik Tollerud @etollerud

**Updated:** August 03, 2021

---

## Motivation

For Notebooks under active development, as well as those simply being maintained, INS needs to be able to make changes and corrections in a timely fashion. This is especially important for minor user-facing changes: edits to markdown explanations, comments on the code, typo fixes, etc., which add clarity or formality without altering the message or code. It was determined that this level of changes may be made without a full DMD review, and that a member of the COS Notebooks development team, (in this case Nat Kerman,) would be given write access to the notebooks repo to merge their own edits on a limited basis. However, it is extremely important that this workflow of merging one's own edits only be used for minor changes. It is considered bad version control "hygiene" to merge one's own commits for good reason: it is dangerous to publish changes that no one else has looked over. To establish good precedent for this procedure, this document of **ground rules** was established.

*At present these rules apply only to the COS team altering the spacetelescope/notebooks repo.*

---

## We define 3 levels/categories of edits

1. **Very minor edits** require no oversight. Self merging is allowed for very minor edits.
2. **Medium edits** are the gray area which we attempt to define below. They generally require at least one additional person's formal or informal review.
3. **Major edits** are anything from writing or seriously re-working a major function, to publishing a new Notebook. These require a full DMD review.

### Defining **"very minor"**

If it's the type of change that is *"obviously not going to be a debated"*, then no review is necessary. These include the following categories:

* fixing obvious typos - i.e. `teh Cosmic Origins Spactro Graph;    (COsS)` → `the Cosmic Origins Spectrograph (COS)`
* fixing spacing and other minor formatting issues
* rewriting a sentence for clarity in either markdown or code comments
* changing a variable name
  * i.e. `NCosExps` → `num_cos_exps`
* PEP changes (exercise more caution here)
  * i.e. `dict_of_numbers = {'a':1,...,'n':14}` →

```python
dict_of_numbers = {
    'a': 1,
    ...,
    'n': 14
}
```

When possible use and cite the Instrument and Data Handbooks, referring interested users to more information there. In-depth changes to markdown sections explaining the science should be checked by someone with the requisite scientific knowledge. This may be the same person as the author, but if you're ever unsure about something, and it is not clearly explained in the Instrument or Data Handbook, get an expert to review!

### Defining **"major"**

Broadly speaking, a change is major if it...

* ...**adds new functionality** to a Notebook or the repo as a whole, such as:
  * A new Notebook
  * A new section in an existing Notebook
  * A new major function of an existing Notebook
* ...or makes a **fundamental change** to how a Notebook accomplishes a task.
  * What is a fundamental change?:
    * This category is subjective, but our best definition is: *A change is fundamental if it changes not only exactly how a task is accomplished in small details, but also exactly what that task is.*
    * Examples/counter-examples:
      * Changing the way a Notebook handles filepaths from strings to `pathlib.Path` objects *is not* a fundamental change (see notes on medium changes below)
      * Changing the algorithm which a function uses to determine outliers *is* a fundamental change.

**Never** merge a pull request (PR) that contains new content and has not been reviewed from a scientific standpoint and a technical one!

### Defining **"medium"**

These are changes which alter the code in a **notable**, but **non-fundamental** way.

* *Notable* means they are go beyond [minor changes](#defining-very-minor).
* *Non-fundamental* means that they may change the details of *how* a task is accomplished in the program but not *what* is happening.

#### Guiding principle for medium changes

*There should be at least one more "set of eyes" on a change before a merge*: at least one more person aside from the author should examine the change to determine if it is useful, necessary, and correctly implemented.

* In cases of changing code, the additional "eyes" will generally take the form of a **technical expert** like the DATB project scientist. As of August, 2021, this would be Larry Bradley, with backup Erik Tollerud.
* In cases of changing scientific content, a **scientific expert** of the appropriate topic should be asked to review the commit.
* When opening the pull request, @mention the reviewer's GitHub username, referring them to the commit and specific change, and kindly asking them to review the change. They may also need to be contacted via email or Slack. Ask nicely, and know that they are under no obligation to help you!
  * They should give some sort of written approval (preferably through the GitHub Approval method, but email is acceptable).

* If the change is minor, and has been specifically requested by users, it is sometimes acceptable to consider a user as the "second pair of eyes".
  * This only applies to user-focused changes, such as increasing or decreasing the verbosity of code, adding a warning, etc.

If, for some reason, no reviewer can provide approval before a hard deadline, medium changes may be PRed by their author. However, **extreme caution** should be taken to check one's work in these situations. Write access is a privilege which comes with serious responsibility. Merging one's own PRs without approval should be a rare exception, not a rule. Additionally, all such PRs should be considered probationary, awaiting approval once a reviewer is available. As such, the PR should be especially well documented, to ease the reviewer's job once they are available.

#### Examples of medium changes

* Implementing a different sorting algorithm
* Adding minor functionality to a class or function
* Increasing verbosity of output to the user, as in notebooks issue [#171](https://github.com/spacetelescope/notebooks/issues/171). This is also an example where a user could count as the second set of eyes.

## Additional guidelines for contributing to the [spacetelescope/notebooks](https://github.com/spacetelescope/notebooks/) repository

Aim for *smaller commits in larger, detailed PRs*:

* **Commits** should be restricted to specific, small changes to the files.
  * Commit often, always after clearing all Notebook cells.
  * Commit messages should be concise, but mention all types of changes made and relevant files.
    * i.e. "Fixed spelling errors in Markdown - Notebook1.ipynb"; "Draft function for convolving LSFs-Notebook2.ipynb".
  * If a commit fixes an issue, add the text "Issue Fix #NNN" to close the issue when merging the PR.

* **PRs** should be relatively rare and contain as many commits as possible while still remaining readable.
  * PRs must describe not only what has been changed, but *why* these changes were determined to be necessary.
  * Keep related commits to the same PR.
  * PRs should be very well documented and PR messages should describe every type of change included.
  * PRs should flag commits with medium changes to the relevant expert for review, using an @username mention.
