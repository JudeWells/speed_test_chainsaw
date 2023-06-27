#!/bin/bash
#$ -l tmem=3.9G
#$ -l h_vmem=3.9G
#$ -l h_rt=08:29:30
#$ -S /bin/bash
#$ -N move_zips
#$ -t 1
#$ -o /SAN/cath/cath_v4_3_0/alphafold/chainsaw_on_alphafold/speed_test_chainsaw/logs/
#$ -wd /SAN/cath/cath_v4_3_0/alphafold/chainsaw_on_alphafold/speed_test_chainsaw
#These are optional flags but you probably want them in all jobs
#$ -j y
hostname
date
cd /SAN/cath/cath_v4_3_0/alphafold/chainsaw_on_alphafold/speed_test_chainsaw
source /share/apps/source_files/python/python-3.8.5.source
export PATH=/share/apps/python-3.8.5-shared/bin:$PATH
export PYTHONPATH=/SAN/cath/cath_v4_3_0/alphafold/chainsaw_on_alphafold/speed_test_chainsaw
python3 speed_test_uniform_sample # $((${SGE_TASK_ID}-1))
echo completed
date
