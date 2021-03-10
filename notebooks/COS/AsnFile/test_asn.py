#!/usr/bin/env python
#%%[markdown]
### From here, you can run the `calcos` pipeline on your new association file.
##### Running `calcos` is explained in *much* more detail in our [notebook on running the pipeline](https://github.com/spacetelescope/COS-Notebooks/blob/master/Calcos/Calcos.ipynb)

##### The next two cells are only fully relavent if all of the following is true:
##### 1. You are not on the Space Telescope Science Institute (STScI) internet, or connected to STScI via VPN.
##### 2. You have not yet run the notebooks hosted in this repository on the `Calcos` pipeline *nor* the `DayNight` separation.

##### In short, to run the `calcos` pipeline, you will need the relavent reference files. These will need be hosted in the directory assigned the environmetn variable `lref`. No matter *where* you place these files, you *must* create the lref environment variable.
# %%
import os
import calcos
from astropy.table import Table
import matplotlib.pyplot as plt
# %%
data_dir = './data/'
output_dir = './output/'
plots_dir = output_dir + 'plots/'
# %%
os.environ['lref'] = '../../../calcos_reference/references/hst/cos'
# %%
!echo $lref
# %%
%%capture cap --no-stderr

!cp ./output/ldifcombo_2_asn.fits ./data/
calcos.calcos('./data/ldifcombo_2_asn.fits', verbosity=0, outdir=output_dir+"./calcos_processed_1")
# %%
with open(output_dir+'output_calcos_1.txt', 'w') as f: # This file now contains the output of the last cell
    f.write(cap.stdout)
# %%
processed_data_tab = Table.read(output_dir+'calcos_processed_1/'+'ldifcombo_x1dsum.fits')
for segment in processed_data_tab:
    wvln, flux = segment["WAVELENGTH", "FLUX"]
    plt.plot(wvln, flux)
# %%