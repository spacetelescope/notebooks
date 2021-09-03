# DrizzlePac Jupyter Notebook Tutorials


Improved drizzling tutorials are now available as Jupyter Notebooks and compatible with the latest STScI distributed software as part of AstroConda. Prior drizzling examples were written for the DrizzlePac Handbook in 2012, just after MultiDrizzle was replaced, and supplemental examples were posted to the DrizzlePac Webpage in 2015 to support enhanced features in DrizzlePac 2.0. The new interactive notebooks consolidate information from these prior examples to form a more cohesive set, and any references to outdated software, such as PyRAF, have been removed and replaced with python functionality.

The notebooks contain live code and visualizations, along with the usual narrative text, making them an ideal training exercise for new users. Each tutorial includes blocks of code demonstrating how to download the calibrated data from the MAST archive, how to align frames and update the image world coordinate system, and how to enhance the scientific value of the drizzled data products using advanced reprocessing techniques.

The eleven notebooks available in this repository include the following topics:

* Initializing DrizzlePac
* Aligning observations obtained in multiple HST visits
* Aligning HST images to an absolute reference catalog (e.g. GAIA, SDSS)
* Aligning sparse fields
* Improving alignment with DS9 exclusion regions
* Masking satellite trails in DQ arrays prior to drizzling
* Optimizing the image sampling for dithered datasets
* Drizzling WFPC2 data to use a single zeropoint
* Sky matching features for HST mosaics
* Aligning HST mosaics observed with multiple detectors
* Using the updated astrometry solutions based on _Gaia_ positions

Additional tutorials will be added to the repository as new software functionality becomes available, especially for advanced use cases. For additional assistance with DrizzlePac tools, users may submit a ticket to the [STScI Help Desk](https://stsci.service-now.com/hst?id=hst_index) or send an email to help@stsci.edu.


Special thanks to the authors of these notebooks: J. Mack, S. Hoffmann, R. Avila, V. Bajaj, M. Cara, T. Desjardins, C. Martlin, C. Shanahan
