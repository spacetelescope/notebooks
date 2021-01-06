## Translating IDL LSFs into python so I can edit and use them

from astropy.table import Table
import numpy as np
from astropy.io import fits
from scipy.interpolate import interp1d

from astropy.convolution import convolve

from matplotlib import pyplot as plt

#-------------------------------------------------------------------------------
def read_lsf(filename):
    # this is assuming you got the lsf from the COS webpage and the first column
    #   is a list of the wavelengths corresponding to the gaussian
    lsf = Table.read(filename, format='ascii', header_start=0)

    # I don't know why this is called pix, but this is the same result as IDL version
    # middle pixel of the lsf is zero ; center is relative zero
    pix = np.arange(len(lsf)) - len(lsf) // 2 # integer division to have whole pixels I assume

    # the column names returned as integers. Called w for some reason
    w = np.array([int(k) for k in lsf.keys()])

    return lsf, pix, w

#-------------------------------------------------------------------------------

def get_disp_params(disptab, cenwave, segment, x=[]):
    with fits.open(disptab) as d:
        wh_disp= np.where((d[1].data['cenwave'] == cenwave) &
                          (d[1].data['segment'] == segment) &
                          (d[1].data['aperture'] == 'PSA'))[0]
        disp_coeff = d[1].data[wh_disp]['COEFF'][0] # for some reason this returns [[arr]]
        d_tv03 = d[1].data[wh_disp]['D_TV03']
        d_orbit = d[1].data[wh_disp]['D']

    delta_d = d_tv03 - d_orbit

    if len(x):
        wavelength = np.zeros(len(x))
        for power, coeff in enumerate(disp_coeff):
            # calculating the wavelength from xfull by adding to the same array
            #   but going up in powers each time
            wavelength = wavelength + coeff*(x+delta_d)**power

        return disp_coeff, wavelength
    else:
        return disp_coeff
#-------------------------------------------------------------------------------

def redefine_lsf(lsf_file, cenwave, disptab, detector='FUV'):
    if detector == 'FUV':
        # FUV detector!!
        xfull = np.arange(16384)
        # segments = ['FUVA', 'FUVB']
    elif detector == 'NUV':
        raise NotImplementedError()
        xfull = np.arange(1024)

    ## this block wont work for NUV
    # read the here for the segments and pass that in
    if cenwave != 1105:
        disp_coeff_b, wavelength_b = get_disp_params(disptab, cenwave, 'FUVB', x=xfull)
    else:
        # 1105 doesn't have an FUVB so set it to something arbitrary
        wavelength_b = [-99., 0.]

    disp_coeff_a, wavelength_a = get_disp_params(disptab, cenwave, 'FUVA', x=xfull)

    step = disp_coeff_a[1] # a and b seem to be the same dispersion coeff....I'm not sure this is true after we redid the wavecal solutions

    ## read in the lsf file
    lsf, pix, w = read_lsf(lsf_file)

    # There might be a better way to do this. IDL shift function can be devious
    # interpolate instead if not linearly spaced ; most people do this though (unfortunately)
    deltaw = np.median(w-np.roll(w, 1)) # getting the median difference between the column headers

    lsf_array = [np.array(lsf[key]) for key in lsf.keys()]
    if deltaw > len(pix)*step*2: #this seems super arbitary
        raise ValueError('deltaw too large:\ndeltaw:{}\nthreshold:{}'.format(detaw, len(pix)*step*2))

    # this is all a set up of the bins we want to use I think
    new_deltaw = round(len(pix)*step*2.)
    new_nw = int(round((max(w)-min(w))/new_deltaw))+1 # nw = number of wavelengths
    new_w = min(w) + np.arange(new_nw)*new_deltaw
    # new_w = np.linspace(min(w), max(w), new_nw) # code review replacement. Test this. Might need to add to max to get the last value

    # populating the lsf with the proper bins
    # changed new_nw to be an int on round line

    # might be a much simpler way to do this
    # new_lsf = lsf[0::new_deltaw] # make sure you know where you're starting

    new_lsf = np.zeros((len(pix), new_nw)) #empty 2-D array to populate
    for i, current_w in enumerate(new_w):
        dist = abs(current_w - w)

        lsf_index = np.argmin(dist)
        temp_key = lsf.keys()[lsf_index]
        new_lsf[:, i] = np.array(lsf[temp_key])

    return new_lsf, new_w, step

#-------------------------------------------------------------------------------

def convolve_lsf(wavelength, spec, cenwave, lsf_file, disptab):

    new_lsf, new_w, step = redefine_lsf(lsf_file, cenwave, disptab)

    ## wavelength of the COS lsf
    # new wavelength scale ; is this different than new_w?
    nstep = round(( max(wavelength)-min(wavelength))/step)-1
    wave_cos = min(wavelength) + np.arange(nstep)*step

    # resampling onto the spectrum wavelength scale
    interp_func = interp1d(wavelength, spec)
    spec_cos = interp_func(wave_cos)
    final_spec = interp_func(wave_cos)

    ## new stuff
    for i, w in enumerate(new_w):
        # The first and last elements need to be treated separately
        if i == 0:
            diff_wave_left = 500
            diff_wave_right = (new_w[i+1]-w)/2.
        elif i == len(new_w)-1:
            diff_wave_right = 500
            diff_wave_left = (w-new_w[i-1])/2.
        else:
            diff_wave_left = (w-new_w[i-1])/2.
            diff_wave_right = (new_w[i+1]-w)/2.

        # splitting up the spectrum into slices
        chunk = np.where( (wave_cos < w+diff_wave_right) &
                        (wave_cos >= w-diff_wave_left))[0]
        if len(chunk) == 0:
            # off the edge
            # in idl, "where" returns -1 if it doesn't find anything
            continue

        current_lsf = new_lsf[:, i]

        if len(chunk) >= len(current_lsf):
            final_spec[chunk] = convolve(spec_cos[chunk], current_lsf, boundary="extend", normalize_kernel=True)

    return wave_cos, final_spec

#-------------------------------------------------------------------------------

if __name__ == "__main__":

    lsf_file = '/user/rplesha/1222_av75/aa_LSFTable_G130M_1222_LP4_norm.dat'
    disptab = '/grp/hst/cdbs/lref/05i1639ml_disp.fits'

    data = Table.read('/user/rplesha/1222_av75/C1096bin3-stis-modelA.dat', format='ascii', names=['wave', 'flux'])
    #data = fits.getdata('/user/rplesha/1222_av75/fuse_data/AV75/all/P1150404999_combined.fit')
    wave = data['wave']
    flux = data['flux']

    conv_wave, final_spec = convolve_lsf(wave, flux, 1222, lsf_file, disptab)

    new_data = Table([conv_wave, final_spec], names=['wave', 'flux'])
    new_data.write("/user/rplesha/1222_av75/fuse_data/AV75/all/convolved_AV75.dat", format='ascii')

    plt.plot(wave, flux, color='black')
    plt.plot(conv_wave, final_spec, color='red')
    plt.show()
