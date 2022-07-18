"""
AUTHOR: Nathaniel Kerman <nkerman@stsci.edu>
DATE of last modification: Feb 2022
DESCRIPTION: 
    Several functions useful for the COS ViewData.ipynb Notebook, such as:
    * downsampling
    * binning to a resolution element (resel)
    * estimating SNR
    * Checking how close two values are
    
    The reason this file is defined separate of the Notebook is to prevent the Notebook from including large and confusing code chunks. In the future, these functions may be incorporated into a Python package, such as `COSTools`.
"""
#%%
import numpy as np
from astropy.table import Table


def downsample_sum(myarr, factor):
    """Downsamples a 1D array by summing over *factor* pixels; Crops right side if the shape is not a multiple of factor.

    Args:
        myarr (numpy array): numpy array to be downsampled/binned.
        factor (int) : how much you want to rebin the array by.
    """
    xs = myarr.shape[0]
    crop_arr = myarr[: xs - (xs % int(factor))]
    dsarr = np.sum(
        np.concatenate([[crop_arr[i::factor] for i in range(factor)]]), axis=0
    )
    return dsarr


# %%
def downsample_1d(myarr, factor, weightsarr=[-1], weighted=True, in_quad=False):
    """
    Downsamples a 1D array by averaging over *factor* pixels; Crops right side if the shape is not a multiple of factor; Can do in quadrature, and weighted.

    Parameters:
    myarr (numpy array): numpy array to be downsampled/binned.
    factor (int) : how much you want to rebin the array by.
    weightsarr (numpy array) : numpy array by which to weight the average; Unnecessary if weighted == False.
    weighted (bool) : Default True. Is this an unweighted mean or a weighted average
    in_quad (bool) : Default False. Do you want to average/sum in quadrature?

    Returns:
    (numpy array) downsampled myarr binned by factor, cropped to an integer multiple of factor.

    Citation:
    Credit to Rachel Plesha for the initial inspiration on this. Rachel cited "Adam Ginsburg's python codes".
    """
    if in_quad:
        myarr = np.power(myarr, 2)

    xs = myarr.shape[0]
    crop_arr = myarr[: xs - (xs % int(factor))]
    crop_weights = weightsarr[: xs - (xs % int(factor))]

    if weighted == True:
        if np.mean(weightsarr) == -1:
            print("CAUTION!!!! You didn't specify what to weight by!")
            dsarr = -1
        else:
            dsarr = np.average(
                np.concatenate([[crop_arr[i::factor] for i in range(factor)]]),
                weights=np.concatenate(
                    [[crop_weights[i::factor] for i in range(factor)]]
                ),
                axis=0,
            )

    else:  # when weighted == False:
        dsarr = np.mean(
            np.concatenate([[crop_arr[i::factor] for i in range(factor)]]), axis=0
        )
    if in_quad:
        dsarr = np.sqrt(dsarr)
    return dsarr


# %%
def bin_by_resel(data_table, binsize=6, weighted=True, verbose=True):
    """
    Bins an entire COS dataset (in astropy Table form)
        * Wavelength and flux are combined by taking an exposure-time weighted mean of all the pixels in a bin.
        * Errors are combined as above and divided by the square root of the number of pixels in a bin
        * Counts and count rate are summed over all the pixels in a bin.

    Parameters:
    data_table (Table) : Astropy Table of COS spectral data.
    binsize (int) : What to bin by.
    weighted (bool) : Whether to weight the averages by exposure time of a pixel; Default is True.
    verbose (bool) : Whether to print major steps the function is taking; Default is True.

    Returns:
    Table : New binned table of values
    """
    assert binsize != 0, "Impossible binsize of 0."
    assert binsize != 1, "Binning by 1 means doing nothing."
    assert (
        binsize > 1 and type(binsize) == int
    ), "Binsize must be an integer greater than 1."
    exptimes_ = []
    wvlns_, fluxs_, fluxErrs_, fluxErr_lowers_, gross_s_, gcount_s_ = (
        [],
        [],
        [],
        [],
        [],
        [],
    )

    print(f"function `bin_by_resel` is binning by {binsize}")
    for i in range(len(data_table)):
        exptimes_.append(data_table[i]["EXPTIME"])
        wvln_, flux_, fluxErr_, fluxErr_lower_, gross_, gcount_ = data_table[i][
            "WAVELENGTH", "FLUX", "ERROR", "ERROR_LOWER", "GROSS", "GCOUNTS"
        ]
        if weighted == True:
            np.seterr(
                invalid="ignore"
            )  # We want to silence warnings from  dividing 0/0
            weightsarr_ = np.nan_to_num(
                gcount_ / gross_, nan=1e-30
            )  # Exposure time can be calculated by gross counts divided by gross counts/second
            # Dividing this way results in NaNs which are messy. replace nans with a value << exptime
            # This way, weight is ~0 unless all values in a chunk are NaN
            np.seterr(invalid="warn")  # Turn the warnings back on
            wvln_ = downsample_1d(myarr=wvln_, weightsarr=weightsarr_, factor=binsize)
            flux_ = downsample_1d(myarr=flux_, weightsarr=weightsarr_, factor=binsize)
            fluxErr_ = np.divide(
                downsample_1d(
                    myarr=fluxErr_, weighted=False, factor=binsize, in_quad=False
                ),
                np.sqrt(binsize),
            )  # Errors are divided by the square root of the number of (identical) observations they represent - this is idealized and simplified. It is good for an estimation.
            fluxErr_lower_ = np.divide(
                downsample_1d(
                    myarr=fluxErr_lower_, weighted=False, factor=binsize, in_quad=False
                ),
                np.sqrt(binsize),
            )
            gross_ = downsample_sum(myarr=gross_, factor=binsize)
            gcount_ = downsample_sum(myarr=gcount_, factor=binsize)

        elif weighted == False:
            weightsarr_ = -1

            wvln_ = downsample_1d(myarr=wvln_, weighted=False, factor=binsize)
            flux_ = downsample_1d(myarr=flux_, weighted=False, factor=binsize)
            fluxErr_ = np.divide(
                downsample_1d(
                    myarr=fluxErr_, weighted=False, factor=binsize, in_quad=False
                ),
                np.sqrt(binsize),
            )
            fluxErr_lower_ = np.divide(
                downsample_1d(
                    myarr=fluxErr_lower_, weighted=False, factor=binsize, in_quad=False
                ),
                np.sqrt(binsize),
            )
            gross_ = downsample_sum(myarr=gross_, factor=binsize)
            gcount_ = downsample_sum(myarr=gcount_, factor=binsize)

        wvlns_.append(wvln_)
        fluxs_.append(flux_)
        fluxErrs_.append(fluxErr_)
        fluxErr_lowers_.append(fluxErr_lower_)
        gross_s_.append(gross_)
        gcount_s_.append(gcount_)

    return Table(
        [exptimes_, wvlns_, fluxs_, fluxErrs_, fluxErr_lowers_, gross_s_, gcount_s_],
        names=[
            "EXPTIME",
            "WAVELENGTH",
            "FLUX",
            "ERROR",
            "ERROR_LOWER",
            "GROSS",
            "GCOUNTS",
        ],
    )


# %%
def estimate_snr(
    data_table,
    snr_range=[-1, -1],
    bin_data_first=False,
    binsize_=6,
    weighted=False,
    verbose=True,
):
    """
    Gets an estimate of the Signal to Noise Ratio (SNR), either over wvln-range or whole spectrum, using Poisson noise assumption SNR ~sqrt(N_Counts).
    Weights the SNR

    Parameters:
    data_table (Astropy Table) : astropy table of COS data.
    snr_range (list) : list of two values - [wvln_range_start , wvln_range_end]; Default is [-1,-1], indicating that we will take over all values.
    bin_data_first (bool) : Should we begin by binning the data by the binsize_? Default is False.
    binsize_ (int) : If bin_data_first == True, what to bin by; Default is 6 for fuv resel.
    weighted (bool) : Do you want the average to be an exposure time weighted average rather than the default unweighted mean; Default is False.
    verbose (bool) : Whether to give a few print statements; default is True.

    Returns:
    float : A single value for the exptime-weighted average or mean SNR over the specified snr_range; -1 if no specified range.
    nested list : 1st level of list corresponds to the segments/rows of the input data_table, 2nd level holds wvln, snr, segmentnumber over snr_range -\n\t\t ie [[-1,-1,-1],[wvln over range array, wvln over range array, row in input data_table int][-1,-1,-1]].
    """
    snr_array = []  # Initialize to empty array
    weight_avg_snr = -1  # Will return -1 UNLESS changed
    segsFound = 0

    # STEP ONE - BINNING
    if bin_data_first == True:  # Should we bin first?
        if verbose:
            print("First, Binning the data by ", binsize_)
        data_table = bin_by_resel(data_table, binsize=binsize_)

    # STEP TWO - ESTIMATE SNR
    for i in range(len(data_table)):
        wvln_, gross_, gcount_ = data_table[i]["WAVELENGTH", "GROSS", "GCOUNTS"]

        if snr_range == [-1, -1]:  # No range specified - estimates over the whole range
            snr_array.append([wvln_, np.sqrt(gcount_), i])
            if verbose:
                print("No range specified.")

        else:
            if (min(snr_range) > min(wvln_)) & (max(snr_range) < max(wvln_)):
                segsFound += 1
                wvln_range_mask = (wvln_ > snr_range[0]) & (wvln_ < snr_range[1])

                wvln_range, gcount_range, gross_range = (
                    wvln_[wvln_range_mask],
                    gcount_[wvln_range_mask],
                    gross_[wvln_range_mask],
                )

                snr_array.append([wvln_range, np.sqrt(gcount_range), i])

                if weighted == False:
                    weight_avg_snr = np.mean(np.sqrt(gcount_range))
                    if verbose:
                        print(
                            f"In range on {i}-th segment with limits:",
                            min(wvln_),
                            max(wvln_),
                            f"\nUnweighted mean SNR over the range {snr_range} is: {weight_avg_snr}",
                        )

                if weighted == True:
                    weight_avg_snr = np.average(
                        np.sqrt(gcount_range),
                        weights=np.nan_to_num(gcount_range / gross_range, nan=1e-30),
                    )
                    if verbose:
                        print(
                            f"In range on {i}-th segment with limits:",
                            min(wvln_),
                            max(wvln_),
                            f"\nEXPTIME weighted average SNR over the range {snr_range} is: {weight_avg_snr}",
                        )
            else:
                snr_array.append([-1, -1, -1])
                if verbose:
                    print(
                        f"Out of range on {i}-th segment with limits:",
                        min(wvln_),
                        max(wvln_),
                    )
    if (  # Check whether the code has found any specified wavelength ranges
        all([elem == -1 for elem in (snr_array[0][2], snr_array[1][2])])
    ) & (  # Check that the user specified wavelength ranges
        snr_range != [-1, -1]
    ):
        if verbose:  # Then print to the user that the ranges weren't found
            print("\nThe input range was not found in any segment!\n")
    if segsFound > 1:
        if verbose:
            print(
                "\nThis range was found on multiple segments, (grating = G230L?) ,which at present is not fully supported. The returned array should be accurate, but the mean may be incorrect."
            )
    return weight_avg_snr, snr_array


# %%
def withinPercent(val1, val2, percent=1.0):
    """
    Primarily created for testing, this function evaluates whether two values are 'close-enough' to one another, i.e. within a percent value, that they could only differ by slight pipeline changes; This one is defined such that at close values, the percent difference is accurate.

    Parameters:
    val1, val2 (numerical) : Values to compare.
    percent (float) : Returns value of true if the values are within this percent.

    Returns:
    bool : Whether or not values are within the specified percent.
    float : Percent they are off by.
    """
    if (val1 == np.nan) | (val2 == np.nan):
        print("One of your values is NOT A NUMBER")
    lowval = np.min(np.array([val1, val2]))
    meanval = np.mean(np.array([val1, val2]))
    absDif = np.abs(np.subtract(val1, val2))
    percentDif = np.abs(100 * (absDif / lowval))
    within_percent_bool = percentDif <= percent
    return within_percent_bool, percentDif


# %%
"""
This section is for testing and validating our S/N Calculations.
"""
if __name__ == "__main__":
    print("Running test on S/N estimate function.")
    test_SNR_calculations = True
    if test_SNR_calculations:
        # You will need to set this filepath to a fitsfile.
        # I used the publicly available ldxt08010_x1dsum.fits from program 15646 (https://archive.stsci.edu/cgi-bin/mastpreview?mission=hst&dataid=LDXT08010). It was chosen at random, and is not particularly high quality data.
        filepath = "./ldxt08010_x1dsum.fits.gz"

        from astropy.io import fits
        import matplotlib.pyplot as plt

        unbin_tab = Table.read(filepath)
        X = [1]
        snr_counts_approach = [
            estimate_snr(
                unbin_tab,
                snr_range=[1565, 1575],
                bin_data_first=False,
            )[0]
        ]

        snr_flux_approach = [
            np.nanmean(
                unbin_tab["FLUX"][
                    (unbin_tab["WAVELENGTH"] > 1565) & (unbin_tab["WAVELENGTH"] < 1575)
                ]
                / unbin_tab["ERROR"][
                    (unbin_tab["WAVELENGTH"] > 1565) & (unbin_tab["WAVELENGTH"] < 1575)
                ]
            )
        ]
        snr_flux_approach_low = [
            np.nanmean(
                unbin_tab["FLUX"][
                    (unbin_tab["WAVELENGTH"] > 1565) & (unbin_tab["WAVELENGTH"] < 1575)
                ]
                / unbin_tab["ERROR_LOWER"][
                    (unbin_tab["WAVELENGTH"] > 1565) & (unbin_tab["WAVELENGTH"] < 1575)
                ]
            )
        ]
        for bs_ in range(1, 100):
            try:
                a, b = estimate_snr(
                    unbin_tab,
                    snr_range=[1565, 1575],
                    bin_data_first=True,
                    binsize_=bs_,
                    weighted=True,
                    verbose=False,
                )
                X.append(bs_)
                snr_counts_approach.append(a)
                # flux/error approach:
                bin_tab = bin_by_resel(unbin_tab, binsize=bs_)
                x1d_error_range = (
                    bin_tab["FLUX"][
                        (bin_tab["WAVELENGTH"] > 1565) & (bin_tab["WAVELENGTH"] < 1575)
                    ]
                    / bin_tab["ERROR"][
                        (bin_tab["WAVELENGTH"] > 1565) & (bin_tab["WAVELENGTH"] < 1575)
                    ]
                )
                x1d_error_range_low = (
                    bin_tab["FLUX"][
                        (bin_tab["WAVELENGTH"] > 1565) & (bin_tab["WAVELENGTH"] < 1575)
                    ]
                    / bin_tab["ERROR_LOWER"][
                        (bin_tab["WAVELENGTH"] > 1565) & (bin_tab["WAVELENGTH"] < 1575)
                    ]
                )
                snr_flux_approach_val = np.nanmean(x1d_error_range)
                snr_flux_approach_val_low = np.nanmean(x1d_error_range_low)
                snr_flux_approach.append(snr_flux_approach_val)
                snr_flux_approach_low.append(snr_flux_approach_val_low)

            except Exception as ex:
                print("failed for", bs_)
                print(ex)
        plt.figure(figsize=(8, 6), dpi=200)
        # plt.scatter(X[1:],limfluxerrs, label = "From my binning algorithm")
        plt.scatter(X, snr_counts_approach, label="From my binning algorithm")
        plt.scatter(
            x=X,
            y=snr_flux_approach,
            label="From the X1DSUM's $\dfrac{FLUX}{ERROR}$",
            marker="x",
            c="r",
        )
        plt.scatter(
            x=X,
            y=snr_flux_approach_low,
            label="From the X1DSUM's $\dfrac{FLUX}{ERROR\_LOWER}$",
            marker="x",
            c="g",
        )
        plt.xlabel("Binsize [pixels]")
        plt.ylabel("$\dfrac{Signal}{Noise}$")
        # plt.xlim(0,30)
        plt.legend()
        plt.savefig("./test_estimate_snr_function.png")

        plt.figure(figsize=(8, 6), dpi=200)
        plt.title("Comparing our S/N calculation to CalCOS'")
        plt.scatter(
            x=X,
            y=100 * (np.divide(snr_counts_approach, snr_flux_approach) - 1),
            label="Comparing against S/N from ERROR",
            marker="x",
            c="k",
        )
        plt.scatter(
            x=X,
            y=100 * (np.divide(snr_counts_approach, snr_flux_approach_low) - 1),
            label="Comparing against S/N from ERROR_LOWER",
            marker=".",
            c="b",
        )
        plt.xlabel("Binsize [pixels]")
        plt.ylabel("Exceeds the X1DSum file's binned S/N by this %")
        plt.legend()
        plt.savefig("./test_estimate_snr_function_percent_overestimation.png")
