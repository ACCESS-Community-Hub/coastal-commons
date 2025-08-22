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

To facilitate the process which involve many steps, we have created a bash script to automate most of it. To start off, you need to be in the same folder where coastal-commons repo is. It is recommended to avoid any problem, that you create a new folder which will contain coastal-commons and source bare repository and the bash script "automate_github_recipes.sh". After cloning "coastal-commons" repo, copy the bash script to recentlty created folder as below:

```
mkdir temporary
cd temporary
git clone https://github.com/ACCESS-Community-Hub/coastal-commons.git
cp coastal-commons/automate_github_recipes.sh ../
```

To use the automate script you need to also inform the path to the file you want to copy (skipping the name of the source repo since it assumes by default it is "ACCESS-NRI-SEACOFS.git") and the commit comment as string:

```
bash automate_github_recipes.sh Recipes/OHC_calculation.ipynb "Copying OHC recipe"
```

After that you just need to monitor the terminal and press ENTER when it is requested and you don't run into any error.

When the copy is pushed to the remote repo, you will need to visit coastal-commons on Github. Click on the link printed on the terminal with a message like:

```
remote: Create a pull request for 'import-recipe' on GitHub by visiting:
remote:      https://github.com/ACCESS-Community-Hub/coastal-commons/pull/new/import-recipe
```

Do the pull request and if you have permissions merge into main. After you have done that, go back to your terminal and press ENTER. This will remove the branch created, clean, and pull your coastal-commons with the new changes to keep it updated.



<!-- #### Download the repository from which your file is coming from.  -->
<!-- For this example we are using ACCESS-NRI-SEACOFS but you can swap the url and repository name to any GitHub repository. Make sure you clone it as "bare", so you have only the metadata which contains the history. You won't have the tree structure as a normal repo.

```
cd ~/code
git clone --bare https://github.com/UNSW-oceanography/ACCESS-NRI-SEACOFS.git
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
You will need to navigate to the import-new-file branch on githib and create a pull request into main – describing the new files and its usage -->
