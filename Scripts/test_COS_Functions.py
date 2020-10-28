#!/usr/bin/env python
#%%
import pytest as pt

import Useful_COS_Functions as U
from astropy.table import Table
import matplotlib.pyplot as plt
# %%
fuvDat = Table.read('/Users/nkerman/Projects/Walkthroughs/ViewData/data/mastDownload/HST/lcxv13050/lcxv13050_x1dsum.fits')
nuvDat = Table.read('/Users/nkerman/Projects/Walkthroughs/ViewData/data/mastDownload/HST/lbbd01020/lbbd01020_x1dsum.fits')
# %%
# Define the Test Functions:
def test_withinPercent():
    ### test 1
    bool, out = U.withinPercent(1,2,5)
    assert bool == False

    try:
        assert round(out - 100., ndigits=5) == 0
    except: 
        print(f"failed inputs: {1,2,5} . with out", out)
    
    ### test 2
    bool, out = U.withinPercent(9.1E-15 , 8.15E-13 , 8857)
    assert bool == True

    try:
        assert round(out - 8856, ndigits=1) == 0
    except: 
        print("failed with out", out)

    ### test 3
    bool, out = U.withinPercent(110 , 100 , 11)
    assert bool == True

    try:
        assert round((out - 10), ndigits=5) == 0
    except: 
        print("failed with out", out)
    
    ### test 4
    bool, out = U.withinPercent(110 , -100 , 10)
    assert bool == False

    try:
        assert round(out - 210 , ndigits=5 ) == 0
    except: 
        print("failed with outs", out)

# %%
# Run the test functions
test_withinPercent()

# %%

# %%










# %%

wvln , flux = fuvDat[0]["WAVELENGTH", "FLUX"]
# %%
U.downsample_1d(wvln, 6, weighted = False)

# %%
U.binByResel(fuvDat)
# %%
nuv_range_overlap = [2200,2300]
a, b = U.estimate_SNR(nuvDat, snr_range=nuv_range_overlap)
# %%
a
# %%
b[2]
# %%
plt.plot(b[2][0], b[2][1])
plt.plot(b[0][0], b[0][1])
# %%

# %%
