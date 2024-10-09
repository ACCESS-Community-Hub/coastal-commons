# How to Install and Use Python on Your Computer

This guide will help you install Python on your computer and set up your environment to begin coding in Python. The instructions below will guide you to use VScode as your 
main editor and interface to program in Python.

---

## Table of Contents
1. [Introduction](#introduction)
2. [For Windows users](#for-windows-users)
3. [Step 1: Downloading and installing VScode](#step-1-downloading-and-installing-vscode)
4. [Step 2: Downloading and installing Mamba](#step-2-downloading-and-installing-mamba)
    - [Downloading](#downloading-mamba)
    - [Installing](#installing-mamba)
5. [Step 3: Creating a Virtual Environment and Installing Modules](#step-3-creating-a-virtual-environment-and-installing-modules)
6. [Ipython](#ipython)

<br>

---

## Introduction
The steps you need to follow are:
    
- Install VScode
- Install Mamba (conda improved repository manager)
- Create a Python environment
- Install Python modules
- Test on Ipython

Since the first step is to install VScode, once it is installed it will be the same process across all Operational Systems (OS).

<br>

---

## For Windows users

From now on, we will be using the bash/zash terminal. It is the most efficient way to run python and also to access remote computers/clusters (like NCI-Gadi). Nowadays, it is possible to install Linux on your Windows OS computer. Refer to the "How-tos" to install Linux on your Windows machine.

<br>

---


## Step 1: Downloading and installing VScode

Go to [VScode webside](https://code.visualstudio.com/download) and download according to your OS. 

<br>

![My Local Image](./images/download_vscode.png)

<br>

Go to the download folder and install the software. I can just follow the pre-defined options or tick other box other than the already selected, but don't change the ticked boxes by default.

<br>

---

## Step 2: Downloading and installing Mamba

### Downloading Mamba

[Go to the website](https://github.com/conda-forge/miniforge) and then select the file according to your OS. Windows users: DO NOT SELECT WINDOWS. Instead select the first Linux option. MacOS users, select the first option (x86_64). 

<br>

![My Local Image](./images/download_mamba.png)

<br>


### Installing Mamba

Now, open you VScode and at the toolbar > Terminal > New Terminal. A terminal will open at the bottom of your VScode. We need to install the file from the terminal and therefore we need the path to the Download folder. 

<br>

On the following: the $ is just to symbolize a terminal line, do not copy it.

<br>

**Windows users**: your Downloads folder it is not located in a very intuitive path, you will need to navigate to it:

<br>

```
# Replace YOUR-USER-NAME with your user name find at C:\Users
$ cd /mnt/c/Users/YOUR-USER-NAME/Downloads

```
<br>

For Mac users:
```
# Change the directory to the Downloads folder
$ cd ~/Downloads
```
<br>

And install Mamba
```
# List all the files with Miniforge and sh in the name
$ ls Miniforge*.sh   

# Copy the file name and paste it after "bash", like (CHANGE THE NAME!):
$ bash Miniforge3-MacOSX-86_64.sh

# Press ENTER
# Press space until you reach the bottom of the text screen when it is showing "Do you accept the license terms? [yes|no]" write yes and press enter:
$ yes

# Accept the location to be install, just pressing ENTER.
# The installation will proceed.

```

<br>

Now a "(base)" will appear on your terminal:

![Local Image](./images/base_mamba.png)

<br>

---

## Step 3: Creating a Virtual Environment and Installing Modules

Creating a new Python Virtual Environment and installing modules can be done at the same time. Using the terminal:

```
$ mamba create --name my_python ipython pandas xarray numpy scipy cartopy matplotlib jupyterlab

```

You can change "my_python" to whatever you want.

<br>

You can always add more modules later, but these are the most used ones. Once the new environment is installed, you need to activate it to be able to use it:

```
$ mamba activate my_python
```

<br>

You will see the activated environment's name replacing "(base)". 

<br>

## Ipython

To do some tests:

```
# Activate Ipython:
$ ipython

# Now you're in the Ipython terminal. You're going to load two modules as a test. You shouldn't receive any error.
import numpy xarray

```

<br>

If you have a Python script you can run it in Ipython, like:

```
run python_script.py
```