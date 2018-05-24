#!/usr/bin/env python

import subprocess
varname = 'J_DIC'

with open('submit.sh', 'r') as file:
    submit_file = file.readlines()

with open('catcesm.py', 'r') as file:
    catcesm_file = file.readlines()

memberList = [1, 2, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
    20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]

for member in memberList:

    submit_file[1] = '#SBATCH -J catcesm_{}.{:0>3}\n'.format(varname, member)
    submit_file[3] = '#SBATCH -t 25:00\n'
    submit_file[6] = '#SBATCH --mem 40G\n'
    submit_file[7] = '#SBATCH -e catcesm_{}.{:0>3}.err.%J\n'.format(varname, member)
    submit_file[8] = '#SBATCH -o catcesm_{}.{:0>3}.out.%J\n'.format(varname, member)
    submit_file[-1] = 'ipython catcesm_{}.{:0>3}.py'.format(varname, member)


    catcesm_file[2] = 'x = {}\n'.format(member)
    catcesm_file[3] = 'varname = \'{}\'\n'.format(varname)

    
    with open('submit_{:0>3}.sh'.format(member), 'w') as file:
        file.writelines(submit_file)

    with open('catcesm_{}.{:0>3}.py'.format(varname, member), 'w') as file:
        file.writelines(catcesm_file)

    subprocess.check_call('sbatch submit_{:0>3}.sh'.format(member),shell=True)
    subprocess.check_call('rm submit_{:0>3}.sh'.format(member),shell=True)
