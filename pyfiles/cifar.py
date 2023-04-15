from tensorflow import keras
import numpy as np
import os

os.chdir('..')
cwd = os.getcwd()

# import the dataset
(x_train, y_train), (x_val, y_val) = keras.datasets.cifar100.load_data()

# save the dataset to the current directory
np.savez(f'{cwd}/content/cifar100.npz', x_train=x_train, y_train=y_train, x_val=x_val, y_val=y_val)
