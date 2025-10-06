# How to download files from NCI locally.

This guide will help you download files from NCI-Gadi on you local computer.

---

## Table of Contents
1. [Introduction](#introduction)
2. [Step-by-step](#step-by-step)
    - [Open a Bash-Zash terminal](#open-a-bash-zash-terminal)
    - [Accessing NCI and getting the path to the file](#accessing-nci-and-getting-the-path-to-the-file)
    - [Copy the file locally](#copy-the-file-locally)


<br>

---

## Introduction
The steps you will be doing are:
    
- Use a bash terminal
- Change your directory to the folder you want to work at (cd)
- Access NCI and copy the path to the file
- Copy the file to your computer


<br>

---


## Step-by-step

### Open a Bash-Zash terminal
You need to use a terminal, preferably bash/zash terminal to access NCI to find the path of the file.

Once you have you terminal open:
```
$ ssh username@gadi.nci.org.au
# Type your password, it won't show up for safety reasons.
```

### Accessing NCI and getting the path to the file
On NCI:

```
# Use "ls" and "cd" commands to navigate on NCI to the files' folder
# Like the example below
$ cd /data/path_file/

# List the files to see the names
$ ls

# Now you need the whole path including the file's name
# "pwd" will give you the path of the current directory you're at. Copy that path and add the file's name to the end
$ pwd
/some/path

# Like:
/some/path/filename.nc

# You need this to be able to copy to your personal computer.

```

### Copy the file locally
On your personal computer, go to the directory you want to copy the file.

```
$ cd /path/where/Iwant/copy/file
```

And copy the file with the command:


```
# The "./" at the end means to copy the file from NCI to the directory you are at.
$ rsync -avhz --progress username@gadi.nci.org.au:/some/path/filename.nc ./

#Type your password, it won't show up for safety reasons.
```

