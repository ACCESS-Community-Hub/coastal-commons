#!/bin/bash
# Author: Fernando Sobral
# Date: 22 Aug 2025

# Usage: ./export_recipe.sh Recipes/model_MKE_EKE.ipynb "MKE EKE"
# First argument: file path in source repo
# Second argument: description for commit message

if [ $# -lt 2 ]; then
  echo "Usage: $0 <file-path> <description>"
  exit 1
fi


# To be able to use filter-repo
module use /g/data/yj27/public/modules 
module load pyvenv/coastal-commons-recipes

echo "=== Updating you remote repo"
cd coastal-commons
git pull
cd ..

FILE_PATH=$1
DESCRIPTION=$2
SRC_REPO="git@github.com:UNSW-oceanography/ACCESS-NRI-SEACOFS.git"
DEST_REPO_DIR="coastal-commons"
TMP_REPO_DIR="ACCESS-NRI-SEACOFS.git"
BRANCH_NAME="import-recipe"

echo "=== Cloning source repo as bare..."
rm -rf $TMP_REPO_DIR
git clone --bare $SRC_REPO $TMP_REPO_DIR

echo
echo ">>> You created a bare clone from ACCESS-NRI-SEACOFS"
echo ">>> Press ENTER if it looks alright..."
read


echo "=== Filtering file: $FILE_PATH ..."
cd $TMP_REPO_DIR || exit 1
git filter-repo --path "$FILE_PATH" --path-rename "$FILE_PATH:$FILE_PATH"
cd ..

echo
echo ">>> You filtered the recipe you want to copy"
echo ">>> Press ENTER if it looks alright..."
read

echo "=== Adding remote and fetching into destination repo..."
cd $DEST_REPO_DIR || exit 1

echo
echo ">>> You are now on the remote repo"
echo ">>> Press ENTER if it looks alright..."
read


# remove old remote if exists
git remote remove recipe-to-copy 2>/dev/null
git remote add recipe-to-copy ../$TMP_REPO_DIR
git fetch recipe-to-copy

echo
echo ">>> You fetched the changes, it must show something"
echo ">>> Press ENTER if it looks alright..."
read

echo "=== Creating new branch and merging..."
git checkout -b $BRANCH_NAME
git merge --allow-unrelated-histories recipe-to-copy/main -m "Import recipe from SEACOFS: $DESCRIPTION"

echo "=== Pushing branch to origin..."
git push origin $BRANCH_NAME

echo
echo ">>> Go to GitHub and approve the Pull Request now!"
echo ">>> Press ENTER here once the PR is merged to continue cleanup..."
read

echo "=== Cleaning up local and remote branches..."
git checkout main
git branch -D $BRANCH_NAME
git push origin --delete $BRANCH_NAME
git fetch --prune


echo "=== Updating you remote repo"
cd coastal-commons
git pull
cd ..


echo "=== Done."
