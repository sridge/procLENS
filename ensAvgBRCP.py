#!/usr/bin/env python

import subprocess

i = 0
varname = 'J_DIC'
dates_i = '200601-210012'
dates_f = dates_i
filepath = '/glade/scratch/sridge/'
nMonth = 1140  

fileprefix = 'b.e11.BRCP85C5CNBDRD.f09_g16.'

filenames = '{}{}/{}???.pop.h.{}.{}.nc {}{}/{}.ensmean.'.format(
    filepath,
    varname,
    fileprefix,
    varname,
    dates_i,
    filepath,
    varname,
    varname)

for x in range(11,nMonth,12):

    year = 2006 + x//12
    year_str = '{:0>3}'.format(year)

    #send command
    subprocess.check_call('ncra -d time,{},{} -v {} {}{}.nc'
        .format(x-11,x,varname,filenames,year_str),shell=True)

subprocess.check_call('ncrcat {}.ensmean.????.nc {}ensmean.pop.h.{}.{}.nc'.format(
    varname,
    fileprefix,
    varname,
    dates_f))   

