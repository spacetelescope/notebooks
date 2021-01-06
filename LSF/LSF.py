#!/usr/bin/env python
#%%
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
import scipy as sp
import seaborn as sb
import scipy.signal as signal
from astropy.io import fits
from astropy import units as u
from astropy.io import ascii
# %%
t = ascii.read('./aa_LSFTable_G130M_1291_LP3_cn.dat', data_start = 1, header_start = 0)
# %%
type(t)
# %%
t.columns
# %%
plt.plot(t['1134'])
# %%
