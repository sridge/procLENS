#!/usr/bin/env python

import subprocess

varname = 'J_DIC'
dates_i = '192001-200512'
dates_f = dates_i
filepath = '/glade/scratch/sridge/'
nMonth = 1032

fileprefix ='b.e11.B20TRC5CNBDRD.f09_g16.'

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

    year = 1920 + x//12
    year_str = '{:0>2}'.format(year)

    #send command
    subprocess.check_call('nces -d time,{},{} -v {} {}{}.nc'
        .format(x-11,x,varname,filenames,year_str),shell=True)


subprocess.check_call('ncrcat {}.ensmean.????.nc {}ensmean.pop.h.{}.{}.nc'.format(
    varname,
    fileprefix,
    varname,
    dates_f))   

