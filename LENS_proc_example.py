#!/usr/bin/env python

freq = 'annual'

varname = 'DIC_ALT_CO2'

localdir = '/glade/scratch/sridge/'

memberlist = [1, 2, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
    20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 101, 102, 103, 104, 105]


# transport_comp = ['UE_','VN_','WT_','HDIFE_','HDIFN_','HDIFB_','DIA_IMPVF_','KPP_SRC_']
transport_comp = ['HDIFB_','DIA_IMPVF_','KPP_SRC_']

for comp in transport_comp:

    filepath = '/CCSM/csm/CESM-CAM5-BGC-LE/ocn/proc/tseries/{}/{}{}/'.format(freq,comp,varname)

    filelist_BRCP_a,filelist_BRCP_b,filelist_BRCP_c,filelist_B20_a,filelist_B20_b = filelist(
        (comp + varname),memberlist,filepath=filepath,freq=freq)

    comp_filelist = sum([filelist_BRCP_a,filelist_BRCP_b,filelist_BRCP_c,filelist_B20_a,filelist_B20_b],[])

    hpss_transfer((comp + varname), comp_filelist, localdir)


