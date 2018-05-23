from subprocess import check_call as cmd


def filelist(varname,memberlist,filepath='',freq='monthly',model='pop',realm='ecosys'):

    if freq != 'monthly' and freq != 'annual':
        raise  ValueError('Frequency given: {}.\n  Frequency must be \'monthly\' or \'annual\'.'.format(freq))

    prefix_BRCP = 'b.e11.BRCP85C5CNBDRD.f09_g16.'
    prefix_B20 = 'b.e11.B20TRC5CNBDRD.f09_g16.'

    if freq == 'annual':

        suffix_BRCP_a = '.{}.h.{}.nyear1.{}.2006-2080.nc'.format(model, realm, varname)
        suffix_BRCP_b = '.{}.h.{}.nyear1.{}.2081-2100.nc'.format(model, realm, varname)
        suffix_BRCP_c = '.{}.h.{}.nyear1.{}.2006-2100.nc'.format(model, realm, varname)
        suffix_B20_a = '.{}.h.{}.nyear1.{}.1850-2005.nc'.format(model, realm, varname)
        suffix_B20_b = '.{}.h.{}.nyear1.{}.1920-2005.nc'.format(model, realm, varname)

    if freq == 'monthly':

        suffix_BRCP_a = '.{}.h.{}.200601-208012.nc'.format(model, varname)
        suffix_BRCP_b = '.{}.h.{}.208101-210012.nc'.format(model, varname)
        suffix_BRCP_c = '.{}.h.{}.200601-210012.nc'.format(model, varname)
        suffix_B20_a = '.{}.h.{}.185001-200512.nc'.format(model, varname)
        suffix_B20_b = '.{}.h.{}.192001-200512.nc'.format(model, varname)

    filelist_BRCP_a = []
    filelist_BRCP_b = []
    filelist_BRCP_c = []
    filelist_B20_a = []
    filelist_B20_b = []

    for member in memberList:

        if member < 100:

            filelist_BRCP_a =  filelist_BRCP_a + [filepath + prefix_BRCP + '{:0>3}'.format(member) + suffix_BRCP_a]

            print(filepath + prefix_BRCP + '{:0>3}'.format(member) + suffix_BRCP_a)

            filelist_BRCP_b =  filelist_BRCP_b + [filepath + prefix_BRCP + '{:0>3}'.format(member) + suffix_BRCP_b]

            print(filepath + prefix_BRCP + '{:0>3}'.format(member) + suffix_BRCP_b)

        elif member > 100:

            filelist_BRCP_c =  filelist_BRCP_c + [filepath + prefix_BRCP + '{:0>3}'.format(member) + suffix_BRCP_c]

            print(filepath + prefix_BRCP + '{:0>3}'.format(member) + suffix_BRCP_c)

        if member == 1:
        
            filelist_B20_a =  [filepath + prefix_B20 + '{:0>3}'.format(1) + suffix_B20_a]

        if member > 1:

            filelist_B20_b =  filelist_B20_b + [filepath + prefix_B20 + '{:0>3}'.format(member) + suffix_B20_b]

            print(filepath + prefix_B20 + '{:0>3}'.format(member) + suffix_B20_b)

    return filelist_BRCP_a,filelist_BRCP_b,filelist_BRCP_c,filelist_B20_a,filelist_B20_b


def hpss_download(varname, filelist, localdir):
    
    # This function downloads CESM-LENS variables off of hpss 

    cmd('mkdir -p {}{}'.format(localdir,varname))
    cmd('cd {}{}'.format(localdir,varname))

    for hpss_file in filelist:

        cmd('nohup hsi {} > {}.out 2>&1'.format(hpss_file,varname),shell=True)
