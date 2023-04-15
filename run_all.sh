#!/bin/bash

# Get the path to the file from the first argument
hyperparam_file=$1

while read item; do
  sbatch ./train_hyperparams.sh "$item"
done < "$hyperparam_file"
