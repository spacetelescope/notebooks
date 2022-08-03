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
from astropy.io import fits
# %%
datadir = Path('./data/')
mast_download_dir = datadir / "mastDownload"
lp6_1exp_datadir = datadir / "lp6_1exp_datadir"
lp6_1exp_datadir.mkdir(exist_ok=True)
outputdir = Path('./output/')
plotsdir =  Path('./output/plots/')
# %%
# Copy all of the relevant LP6 data files into the lp6_1exp_datadir
splitwave_rawtags = [
    shutil.copy(rt, lp6_1exp_datadir / rt.name) \
        for rt in mast_download_dir.glob("**/*rawtag*fits") \
            # Only grab the necessary files
            if fits.getval(rt, "ROOTNAME").upper() in ['LETC01M6Q','LETC01MTQ','LETC01MVQ']
]
# Copy the LP6 single exposure asn file we made into the directory where we moved all of the relevant exposures' data
lp6_1exp_asn = shutil.copy('data/letc01mtq_only_asn.fits', lp6_1exp_datadir)
# %%
######### Setting the lref environment variable:
### YOU LIKELY NEED TO CHANGE THIS LOCATION !
where_i_keep_my_ref_files = "/grp/hst/cdbs/lref/"
os.environ['lref'] = where_i_keep_my_ref_files
assert Path(os.environ['lref']).exists(), "Make sure to set the 'lref' environment variable to a valid path with all of your reference files."
# %%
# Run the CalCOS pipeline on our SPLIT wavecal asn file
calcos.calcos(lp6_1exp_asn, verbosity=0, outdir=str(outputdir/"calcos_processed_lp6_1exp/"))
# %%
# Read in the processed data
processed_data_tab = Table.read(str(outputdir/'calcos_processed_lp6_1exp/')+'/letc01mtq_only_x1dsum.fits')

# Plot the processed data
for segment in processed_data_tab:
    wvln, flux = segment["WAVELENGTH", "FLUX"]
    plt.plot(wvln, flux)
    
plt.xlabel('Wavelength [$\AA$]')
plt.ylabel('Flux [ergs/s/$cm^2$/$\AA$]')

plt.title("If this plot looks reasonable, your ASN file seems to have worked\n")
plt.tight_layout()
plot_path = str(plotsdir/"LP6_1exposure_AsnFile_test.png")
plt.savefig(plot_path, bbox_inches = 'tight', dpi = 200)
print(f"Saved plot to: {plot_path}")
# %%
