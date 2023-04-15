# Initialize project
chmod a+x run_all.sh
chmod a+x train_hyperparams.sh
chmod a+x pyfiles/training.py

python pyfiles/cifar.py
python pyfiles/hyper.py

# Run project
bash run_all.sh content/hyperparameters.txt

# Check accuracies after running project
python all_acc.py
OR
python highest_acc.py