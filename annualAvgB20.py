import subprocess

i = 0
varname = 'J_DIC'
dates_i = '192001-200512'
dates_f = '1920-2005'
filepath = '/glade/scratch/sridge/'
nMonth = 1032

fileprefix ='b.e11.B20TRC5CNBDRD.f09_g16.'

filenames = '{}{}/{}{:0>3}.pop.h.{}.{}.nc {}{}/{}.{:0>3}.mean.'.format(
    filepath,
    varname,
    fileprefix,
    i,
    varname,
    dates_i,
    filepath,
    varname,
    varname,
    i)

for x in range(11,nMonth,12):

    year = 1920 + x//12
    year_str = '{:0>2}'.format(year)

    #send command
    subprocess.check_call('ncra -d time,{},{} -v {} {}{}.nc'
        .format(x-11,x,varname,filenames,year_str),shell=True)


subprocess.check_call('ncrcat -n 86,4,1 {}{}/{}.{:0>3}.mean.????.nc {}{}/{}{:0>3}.pop.h.ecosys.nyear1.{}.{}.nc'.format(
    filepath,
    varname,
    varname,
    i,
    filepath,
    varname,
    fileprefix,
    i,
    varname,
    dates_f),shell=True)

subprocess.check_call('rm {}{}/{}.{:0>3}.mean.????.nc'.format(filepath,varname,varname,i),shell=True)  
subprocess.check_call('rm avgB20_{}.{:0>3}.*'.format(varname,i),shell=True)
