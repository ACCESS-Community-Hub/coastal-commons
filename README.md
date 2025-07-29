# Coastal Commons

## TODO (by 01 August)
- [x] License - HM
- [x] Load first notebooks - HM
- [x] Share workflow for uploading exisiting notebook / preserve history - HM
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
## Uploading a file

You will need access to xp65 on gadi and write permissions to this repository. If you don't have write permissions then please [raise an issue](https://github.com/ACCESS-Community-Hub/coastal-commons/issues/new). Include a description of the file you want to upload 
### Getting the scripts
The first time you upload your file you will need to download a git filter repo script:
```
mkdir -p ~/code
cd ~/code
git clone https://github.com/newren/git-filter-repo.git
```

### Upload your file 
These next steps will need to be repeated for each file
#### Download the repository from which your file is coming from. 
For this example we are using ACCESS-NRI-SEACOFS but you can swap the url and repository name to any GitHub repository.
```
cd ~/code
git clone https://github.com/UNSW-oceanography/ACCESS-NRI-SEACOFS.git
cd ACCESS-NRI-SEACOFS/
```
#### Run script to isolate only your file. 
Note that for this example, the file here is called “README.md”. You will need to change this to the relative path (references from the top directory) and name of the file you want to upload

```
module use /g/data/xp65/public/modules; 
module load conda/analysis3
python3 ../git-filter-repo/git-filter-repo --path README.md --path-rename README.md:README.md
```
#### Import the preexisting coastal commons file and push back to GitHub
```
git remote add repo-b https://github.com/ACCESS-Community-Hub/coastal-commons.git
git pull --rebase https://github.com/ACCESS-Community-Hub/coastal-commons.git
git checkout -b import-new-file
git push repo-b import-new-file
```
You will need to navigate to the import-new-file branch on githib and create a pull request into main – describing the new files and its usage
