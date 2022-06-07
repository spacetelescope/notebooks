#!/usr/bin/env python3
#%%[markdown]
### From here, you can run the `CalCOS` pipeline on your new association SPLIT wavecal file.
##### Running `CalCOS` is explained in *much* more detail in our [Notebook on running the pipeline](https://github.com/spacetelescope/notebooks/blob/master/notebooks/COS/CalCOS/CalCOS.ipynb)

##### In short, to run the `CalCOS` pipeline, you will need the relavent reference files. These will need be hosted in the directory assigned the environmetn variable `lref`. 
##### No matter *where* you place these files, you *must* create the lref environment variable.
# %%
import os, shutil
import calcos
from astropy.table import Table
import matplotlib.pyplot as plt
from pathlib import Path
# %%
datadir = Path('./data/')
mast_download_dir = datadir / "mastDownload"
splitwave_datadir = datadir / "splitwave"
splitwave_datadir.mkdir(exist_ok=True)
outputdir = Path('./output/')
plotsdir =  Path('./output/plots/')
# %%
# Move all of the split wavecal data files into the splitwave_datadir
splitwave_rawtags = [
    rt.rename(splitwave_datadir / rt.name) \
    for rt in mast_download_dir.glob("**/*rawtag*fits")
]
# Get rid of now_empty MAST download directory
shutil.rmtree(mast_download_dir)
# %%
######### Setting the lref environment variable:
### YOU LIKELY NEED TO CHANGE THIS LOCATION !
where_i_keep_my_ref_files = "/grp/hst/cdbs/lref/"
os.environ['lref'] = where_i_keep_my_ref_files
assert Path(os.environ['lref']).exists(), "Make sure to set the 'lref' environment variable to a valid path with all of your reference files."

# Copy the asn file we made into the directory where we moved all of our SPLIT wavecal exposures' data
shutil.copy(outputdir / "splitwave_asn.fits", splitwave_datadir / "splitwave_asn.fits")

# Run the CalCOS pipeline on our SPLIT wavecal asn file
calcos.calcos(str(splitwave_datadir / "splitwave_asn.fits"), verbosity=0, outdir=str(outputdir/"calcos_processed_splitwave"))

# %%
# Read in the processed data
processed_data_tab = Table.read(str(outputdir/'calcos_processed_splitwave/')+'/splitwave_x1dsum.fits')

# Plot the processed data
for segment in processed_data_tab:
    wvln, flux = segment["WAVELENGTH", "FLUX"]
    plt.plot(wvln, flux)
    
plt.xlabel('Wavelength [$\AA$]')
plt.ylabel('Flux [ergs/s/$cm^2$/$\AA$]')

plt.title("If this graph looks at all reasonable, your ASN file seems to have worked\n")
plt.tight_layout()
plot_path = str(plotsdir/"Splitwave_AsnFile_test.png")
plt.savefig(plot_path, bbox_inches = 'tight', dpi = 200)
print(f"Saved plot to: {plot_path}")
# %%
