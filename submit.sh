#!/bin/bash
#SBATCH -J dask
#SBATCH -N 1
#SBATCH -t 02:00:00
#SBATCH -A P93300070
#SBATCH -C geyser
#SBATCH --mem 400G
#SBATCH -e testdask.err.%J
#SBATCH -o testdask.out.%J


### Initialize the Slurm environment
source /glade/u/apps/opt/slurm_init/init.sh
export TMPDIR=/glade/scratch/$USER/temp
mkdir -p $TMPDIR

module load nco
source ~/.bashrc
source activate pangeo

