#!/bin/bash -l
#SBATCH -J hvd_test
#SBATCH -o hvd_test_out.txt
#SBATCH -e hvd_test_err.txt

#SBATCH -t 0:10:00

#SBATCH --partition gpu

#SBATCH --nodes 2
#SBATCH --ntasks-per-node=2

# module load Python/2.7.14-foss-2017b
# pip install --user h5py matplotlib numpy keras tensorflow
# conda activate py37tfgpu

# time mpirun -np 2 python mnist_hvd_2.py > output.txt

time horovodrun -np 2 -H localhost:2  python mnist_hvd_2.py
