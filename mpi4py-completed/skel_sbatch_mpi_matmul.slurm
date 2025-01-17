#!/bin/bash
#SBATCH --ntasks=64
#SBATCH --ntasks-per-node=16
#SBATCH --partition=preempt
#SBATCH --exclusive
#SBATCH --nodes=4
#SBATCH -o t_mpi_dgmm_job.%N.%j.out  # STDOUT
#SBATCH -e t_mpi_dgmm_job.%N.%j.err  # STDERR
#SBATCH --threads-per-core=1
#SBATCH --time=00:30:00

#****************************************************#
# Author:
# Thomas Cullison, Stanford University, 2023
#



##*****************************************##
## size of N for N*N matrix
MATSIZE=4


##*****************************************##
## Header Info
echo;
echo "Starting sbatch script";
echo "DATE: $(date), NTASKS: $SLURM_NTASKS, NNODES: $SLURM_NNODES";
echo;


##*****************************************##
## SPACK setup (like modules)
echo ". /home/spack/spack/share/spack/setup-env.sh";
. /home/spack/spack/share/spack/setup-env.sh;
echo;
echo "spack load intel-oneapi-mpi";
spack load intel-oneapi-mpi;
echo "which mpiexec";
which mpiexec;
echo "spack load python@3.10.8";
spack load python@3.10.8;
echo "python --version";
python --version 2>&1;


##*****************************************##
## MPI
MY_MPI_MATMUL="parallel_matmul.py"
echo;
echo "Running MatMul";
echo;
echo "mpiexec -n $SLURM_NTASKS python $MY_MPI_MATMUL $MATSIZE";
mpiexec -n $SLURM_NTASKS python $MY_MPI_MATMUL;
echo;


##*****************************************##
## Footer Info
echo;
echo "Done...";
echo "DATE: $(date), NTASKS: $SLURM_NTASKS, NNODES: $SLURM_NNODES";
