import numpy as np
import itertools
import os

os.chdir('..')
cwd = os.getcwd()
# create a list of all possible combinations of hyperparameters
BATCH_SIZE = [25,50,75,100]
EPOCHS = [10, 50, 100]
LEARNING_RATE = [1e-1, 3e-1, 1e-2, 3e-2, 1e-3, 3e-3]
L1NF = [2,4,8,16]
FDROPOUT = [.25, 0.5, .75]

hyperparameter_combinations = list(itertools.product(BATCH_SIZE, EPOCHS, LEARNING_RATE, L1NF, FDROPOUT))
 
with open(f'{cwd}/content/hyperparameters.txt', 'w') as f:
    for params in hyperparameter_combinations:
        f.write(','.join(map(str, params)) + '\n')
