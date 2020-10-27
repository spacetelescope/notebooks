#!/usr/bin/env python
#%%
import Useful_COS_Functions
from astropy.table import Table
import matplotlib.pyplot as plt
# %%
fuvDat = Table.read('/Users/nkerman/Projects/Walkthroughs/ViewData/data/mastDownload/HST/lcxv13050/lcxv13050_x1dsum.fits')
nuvDat = Table.read('/Users/nkerman/Projects/Walkthroughs/ViewData/data/mastDownload/HST/lbbd01020/lbbd01020_x1dsum.fits')
# %%

wvln , flux = fuvDat[0]["WAVELENGTH", "FLUX"]
# %%
Useful_COS_Functions.downsample_1d(wvln, 6, weighted = False)

# %%
Useful_COS_Functions.binByResel(fuvDat)
# %%
nuv_range_overlap = [2200,2300]
a, b = Useful_COS_Functions.estimate_SNR(nuvDat, snr_range=nuv_range_overlap)
# %%
a
# %%
b[2]
# %%
plt.plot(b[2][0], b[2][1])
plt.plot(b[0][0], b[0][1])
# %%
