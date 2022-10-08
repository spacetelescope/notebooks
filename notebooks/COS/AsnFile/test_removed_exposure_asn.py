#!/usr/bin/env python3
#%%[markdown]
### From here, you can run the `CalCOS` pipeline on your association file where we've removed the empty exposure file.
##### Running `CalCOS` is explained in *much* more detail in our [Notebook on running the pipeline](https://github.com/spacetelescope/notebooks/blob/master/notebooks/COS/CalCOS/CalCOS.ipynb)

##### In short, to run the `CalCOS` pipeline, you will need the relavent reference files. These will need be hosted in the directory assigned the environmetn variable `lref`. 
##### No matter *where* you place these files, you *must* create the lref environment variable.
# %%
import os, shutil
import calcos
from astropy.table import Table
import matplotlib.pyplot as plt
from pathlib import Path
from astropy.io import fits
# %%
datadir = Path('./data/')
mast_download_dir = datadir / "mastDownload"
outputdir = Path('./output/')
plotsdir =  Path('./output/plots/')
# %%
######### Setting the lref environment variable:
### YOU LIKELY NEED TO CHANGE THIS LOCATION !
where_i_keep_my_ref_files = "/grp/hst/cdbs/lref/"
os.environ['lref'] = where_i_keep_my_ref_files
assert Path(os.environ['lref']).exists(), "Make sure to set the 'lref' environment variable to a valid path with all of your reference files."
# %%
remove_badfile_asn = "data/removed_badfile_asn.fits"
# Run the CalCOS pipeline on our asn file
calcos.calcos(remove_badfile_asn, verbosity=0, outdir=str(outputdir/"calcos_processed_remove_badfile/"))
# %%
# Read in the processed data
processed_data_tab = Table.read(str(outputdir/'calcos_processed_remove_badfile/')+'/ldif01010_x1dsum.fits')

# Plot the processed data
for segment in processed_data_tab:
    wvln, flux = segment["WAVELENGTH", "FLUX"]
    plt.plot(wvln, flux)
    
plt.xlabel('Wavelength [$\AA$]')
plt.ylabel('Flux [ergs/s/$cm^2$/$\AA$]')

plt.title("If this plot looks reasonable, your ASN file seems to have worked\n")
plt.tight_layout()
plot_path = str(plotsdir/"remove_badfile_AsnFile_test.png")
plt.savefig(plot_path, bbox_inches = 'tight', dpi = 200)
print(f"Saved plot to: {plot_path}")
# %%
