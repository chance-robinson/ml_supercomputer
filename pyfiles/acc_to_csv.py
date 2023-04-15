import os
import pandas as pd

os.chdir('..')
cwd = os.getcwd()

directory = f'{cwd}/results/'  # Replace with the path to your directory

df = pd.DataFrame(columns=['BATCH_SIZE','EPOCHS','LEARNING_RATE','L1NF','FDROPOUT','ACCURACY'])

for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        filestring = filename.replace('accuracy_', '').replace('.txt', '')
        file_arr = filestring.split('_')
        BATCH_SIZE = file_arr[0]
        EPOCHS = file_arr[1]
        LEARNING_RATE = file_arr[2]
        L1NF = file_arr[3]
        FDROPOUT = file_arr[4]
        ACCURACY = None
        with open(os.path.join(directory, filename), 'r') as file:
            ACCURACY = float(file.read())
        df.loc[len(df)] = [BATCH_SIZE, EPOCHS, LEARNING_RATE, L1NF, FDROPOUT, ACCURACY]

df.to_csv(f'{cwd}/content/parameter_sweep.csv', index=False)