#!/bin/bash --login

#SBATCH --time=06:00:00   # walltime
#SBATCH --ntasks=1   # number of processor cores (i.e. tasks)
#SBATCH --nodes=1   # number of nodes
#SBATCH --gpus=1
#SBATCH --mem-per-cpu=15360M   # memory per CPU core


# Set the max number of threads to use for programs using OpenMP. Should be <= ppn. Does nothing if the program doesn't use OpenMP.
export OMP_NUM_THREADS=$SLURM_CPUS_ON_NODE

module load cuda/10.1
module load cudnn/7.6
conda activate venv

# Get the passed argument
arg1=$1

# Convert the string to an array
IFS=',' read -r BATCH_SIZE EPOCHS LEARNING_RATE L1NF FDROPOUT <<< "$arg1"

python pyfiles/training.py $BATCH_SIZE $EPOCHS $LEARNING_RATE $L1NF $FDROPOUT