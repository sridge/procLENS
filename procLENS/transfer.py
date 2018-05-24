def hpss(varname, filelist, localdir):
    
    # This function downloads CESM-LENS variables off of hpss 

    Popen(['mkdir','-p','{}{}'.format(localdir,varname)])
    
    os.chdir('{}{}'.format(localdir,varname))

    cmd_list = []

    for hpss_file in filelist:

        cmd_list = cmd_list + ['hsi cget {}'.format(hpss_file)]

    with open('{}_filelist.sh'.format(varname), 'w') as file:
        file.writelines('\n'.join(cmd_list))

    proc = Popen(['nohup','bash','{}_filelist.sh'.format(varname) ],
                 stdout=open(('{}_out.log'.format(varname)), 'w'),
                 stderr=open(('{}_err.log'.format(varname)), 'a'))

    with open('{}_PID.log'.format(varname), 'w') as file:
        file.writelines(str(proc.pid))

