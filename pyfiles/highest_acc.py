import os

os.chdir('..')
cwd = os.getcwd()

directory = f'{cwd}/results2/'  # Replace with the path to your directory

max_value = None
max_file = None

for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        with open(os.path.join(directory, filename), 'r') as file:
            value = float(file.read())
            if max_value is None or value > max_value:
                max_value = value
                max_file = filename

print(f"The highest val_accuracy is {max_value}, found in file: {max_file}")

