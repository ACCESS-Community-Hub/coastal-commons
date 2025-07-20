# Coastal Commons

## TODO (by 01 August)
- [x] License - HM
- [x] Load first notebooks - HM
- [ ] Share workflow for uploading exisiting notebook / preserve history - HM
- [ ] Create python environment (conda or venv) - PC
- [ ] Create module file for loading py env above - PC
- [ ] Create directory to store sample files required by the model recipes - PC
- [ ] Upload scripts for downloading sattelite data (OSTIA, AVISO) - PC
- [ ] Rendered pictures / prints on notebooks or not? - HM, PC, FS
- [ ] Add `contributors` file - HM
- [ ] Nominate other scripts that can be uploaded - HM, FS
- [ ] Document relevant info / changes in this README file

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
