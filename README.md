# Coastal Commons

## Basic requirements:

- Be a member of `yj27` project on NCI Gadi for data access. If you aren't a member yet then please [request membership](https://my.nci.org.au/mancini/project/yj27); 

- Write permissions to this repository. If you don't have write permissions then please [raise an issue](https://github.com/ACCESS-Community-Hub/coastal-commons/issues/new). Include a description of the file you want to upload.

## Start the virtual environment
This will load required system libraries and automatically activate the `coastal-commons-recipes` python environment.

````
module use /g/data/yj27/public/modules 
module load pyvenv/coastal-commons-recipes
````

## Uploading an existing file from another repository

These next steps will need to be repeated for each file in order to preserve the associated git history.  

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
git filter-repo --path README.md --path-rename README.md:README.md
```
#### Import the preexisting coastal commons file and push back to GitHub
```
git remote add repo-b https://github.com/ACCESS-Community-Hub/coastal-commons.git
git pull --rebase https://github.com/ACCESS-Community-Hub/coastal-commons.git
git checkout -b import-new-file
git push repo-b import-new-file
```
You will need to navigate to the import-new-file branch on githib and create a pull request into main – describing the new files and its usage
