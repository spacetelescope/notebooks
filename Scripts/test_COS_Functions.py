#!/usr/bin/env python
#%%
import Useful_COS_Functions
from astropy.table import Table
# %%
fuvDat = Table.read('/Users/nkerman/Projects/Walkthroughs/ViewData/data/mastDownload/HST/lcxv13050/lcxv13050_x1dsum.fits')
# %%

wvln , flux = fuvDat[0]["WAVELENGTH", "FLUX"]
# %%
Useful_COS_Functions.downsample_1d(wvln, 6, weighted = False)

# %%
