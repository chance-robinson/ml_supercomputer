import os

os.chdir('..')
cwd = os.getcwd()

directory = f'{cwd}/results/'  # Replace with the path to your directory

max_value = None
max_file = None
accuracies = {}

for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        with open(os.path.join(directory, filename), 'r') as file:
            value = float(file.read())
            if max_value is None or value > max_value:
                max_value = value
                max_file = filename
            accuracies[value] = filename

sorted_accuracies = sorted(accuracies.keys(), reverse=True)

print(f"\nThe highest accuracy is {max_value}, found in file: {max_file}")

print("Accuracies from highest to lowest:")
for acc in sorted_accuracies:
    print(f"{accuracies[acc]}: {acc}")
