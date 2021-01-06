#! /usr/bin/env python

'''
NAME: plot_lsf.py
DATE: 02/18/2014
AUTHOR: JO TAYLOR, RIA
DESCRIPTION:
This is a program designed to plot LSFs and CDSFs that I produced against
the ones Erin produced and the ones found online. 
'''

# Import necessary packages.
import numpy as np
import matplotlib
from matplotlib import pyplot as pl
import argparse


# Find the wavelength of greatest discrepancy.
def file_diffs(data1,data2,names_to_use,label1,label2):
    final_max = 0.0
    final_name = names_to_use[0]
    all_diffs = []
    for item in names_to_use:
        diff = abs(data1[item] - data2[item])
        all_diffs.append(diff)
        current_max = max(diff)
        if current_max > final_max:
            final_max = current_max
            final_name = item
    print final_name
    plot_lsf(data1,data2,final_name,label1,label2)

# Plot LSF with greatest discrepancy.
def plot_lsf(data1,data2,final_name,label1,label2):
   fig,ax = pl.subplots()
   ax.plot(data1[final_name],"ro-",data2[final_name],"ko-")
   ax.set_yscale("symlog")
   ax.legend((label1,label2),"best")
   pl.show()
   pause = raw_input("Press enter to continue")
   pl.close() 

# Define input parameters.
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Plot LSFs")
    parser.add_argument("-f1", "-file1", dest="table1", action="store",
                        default="/grp/hst/cos3/new_erin_docs/G140L_Data/Data_1Ang_LP2/PSFData_G140L_1105/aa_LSFTable_G140L_1105.dat",
                        help="Path to 1st LSF data table to plot")
    parser.add_argument("-f2", "-file2", dest="table2", action="store",
                        default="/grp/hst/cos3/new_erin_docs/G140L_Data/Data_1Ang_LP2/PSFData_G140L_1105/aa_LSFTable_G140L_1105.dat",
                        help="Path to 2nd LSF data table to plot")
    args = parser.parse_args()
    file1 = args.table1
    file2 = args.table2
    label1 = file1.split("/")[-1]
    label2 = file2.split("/")[-1]
    data1 = np.genfromtxt(file1,names=True) 
    data2 = np.genfromtxt(file2,names=True)
    names1 = data1.dtype.names
    names2 = data2.dtype.names
    if len(names1) != len(names2):
        if len(names1) < len(names2):
            smaller_file = file1
            names_to_use = names1
        else:
            smaller_file = file2
            names_to_use = names2
        print "WARNING: Length of data tables do not match"
        print "         Using length of smaller table "+smaller_file
    else:
        names_to_use = names1

    file_diffs(data1,data2,names_to_use,label1,label2)
