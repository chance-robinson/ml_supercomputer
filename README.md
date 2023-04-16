# Initialize Environment (run one by one)
module load miniconda3/latest
module load cuda/10.1
module load cudnn/7.6

conda init
source ~/.bashrc  #you should see the (base) prefix at the front of the line
echo "[[ -f ~/.bashrc ]] && source ~/.bashrc" > ~/.bash_profile


conda create -n venv tensorflow-gpu cudatoolkit=10.1
conda activate venv  #now you should see (venv) at the front of the line
# this is your virtual environment

conda install keras

(additional packages may need to be installed using conda install ...)

# Initialize project
mkdir slurm_out
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
