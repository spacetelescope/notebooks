#!/usr/bin/env python3

from astropy.io import fits
import sys
import os
from datetime import datetime

cwd = os.getcwd()

filename = (sys.argv[1:])[0]

filepath = cwd+'/'+filename

print(filepath)


fileheader0 = fits.getheader(filepath)
fileheader1 = fits.getheader(filepath, ext = 1) 
#print(fileheader0,"\n\n\n\n##############\n\n\n", fileheader1)

print(cwd+'/'+filename[:-5]+'_headers.txt')

time = datetime.now().microsecond

fileheader0.totextfile(f'tempDELETE_{time}_0.txt')
fileheader1.totextfile(f'tempDELETE_{time}_1.txt')

with open(filepath[:-5]+'_headers.txt', 'w') as outfile:
   outfile.write("\n\n\n##########HEADER0############\n\n\n")
   with open(f'tempDELETE_{time}_0.txt') as infile:
      for line in infile:
         outfile.write(line)
   outfile.write("\n\n\n##########HEADER1############\n\n\n")
   with open(f'tempDELETE_{time}_1.txt') as infile:
      for line in infile:
         outfile.write(line)

os.remove(f'tempDELETE_{time}_0.txt')
os.remove(f'tempDELETE_{time}_1.txt')

os.system(f"open {filepath[:-5]+'_headers.txt'}")
