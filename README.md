# Coastal Commons

## Setting Up a Python Virtual Environment

#### 1) Clone the Repository
```bash
module load git/2.39.2
cd <directory-of-choice>
git clone git@github.com:UNSW-oceanography/ACCESS-NRI-SEACOFS.git
```

#### 2) Create the Environment
```bash
module load python3/3.12.1
python3 -m venv "<path-to-venv-dir>/seacofs"
```

#### 3) Activate the Environment
```bash
source "<path-to-venv-dir>/seacofs/bin/activate"
```

#### 4) Install Library Requirements
```bash
pip install --upgrade pip
pip install -r "<path-to-cloned-repository>/requirements.txt" --no-cache-dir
```
