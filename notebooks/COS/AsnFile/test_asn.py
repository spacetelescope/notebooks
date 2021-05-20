#!/usr/bin/env python
#%%[markdown]
### From here, you can run the `calcos` pipeline on your new association file.
##### Running `calcos` is explained in *much* more detail in our [notebook on running the pipeline](https://github.com/spacetelescope/COS-Notebooks/blob/master/Calcos/Calcos.ipynb)

##### In short, to run the `calcos` pipeline, you will need the relavent reference files. These will need be hosted in the directory assigned the environmetn variable `lref`. 
##### No matter *where* you place these files, you *must* create the lref environment variable.
# %%
import os, shutil
import calcos
from astropy.table import Table
import matplotlib.pyplot as plt
from pathlib import Path
# %%
datadir = Path('./data/')
outputdir = Path('./output/')
plotsdir =  Path('./output/plots/')
# %%
######### SETTING THE lref VARIABLE:
### YOU LIKELY NEED TO CHANGE THIS LOCATION!!!
where_i_keep_my_ref_files = "/grp/hst/cdbs/lref/"
os.environ['lref'] = where_i_keep_my_ref_files

# %%
# shutil.copy("./output/ldifcombo_2_asn.fits", "./data/ldifcombo_2_asn.fits")
# calcos.calcos('./data/ldifcombo_2_asn.fits', verbosity=0, outdir=str(outputdir/"./calcos_processed_1"))
# %%
processed_data_tab = Table.read(str(outputdir/'calcos_processed_1/')+'/ldifcombo_x1dsum.fits')
for segment in processed_data_tab:
    wvln, flux = segment["WAVELENGTH", "FLUX"]
    plt.plot(wvln, flux)
    
plt.xlabel('Wavelength [$\AA$]')
plt.ylabel('Flux [ergs/s/$cm^2$/$\AA$]')

plt.title("If this graph looks reasonable, your ASN file seems to have worked!\n")
plt.tight_layout()
plt.savefig(str(plotsdir/"AsnFile_test.png"), bbox_inches = 'tight', dpi = 200)
# %%
