# How to Install and Use Copernicus Marine Toolbox

This guide will help you install the Copernicus Marine Toolbox and will show how to find your dataset to download

---

## Table of Contents
1. [Introduction](#introduction)
2. [Copernicus Account](#copernicus-account)
3. [Installing Python API](#installing-python-api)
4. [How to Use](#how-to-use)
5. [Credentials](#credentials)


<br>

---

## Introduction
This How-to will help you to install and use the Python Copernicus Marine Toolbox API. This new toolbox replaced the Motu-client and allow you to scrape a catalog of data from Copernicus dataset.

[Offical information](https://help.marine.copernicus.eu/en/articles/7970514-copernicus-marine-toolbox-installation)

<br>

---

## Copernicus Account
First of all, you'll need to create a [Copernicus account](https://marine.copernicus.eu/register-copernicus-marine-service) if you don't have yet.


<br>

---


## Installing Python API

To install the Copernicus Marine in a Python environment. If you don't know how to create a Python environment, read the file [Install and Use Python](./install_copernicus_marine_API.md)

```
mamba install conda-forge::copernicusmarine --yes
```

<br>

## How to Use
To fetch the catalog the following command it is needed:


```
import copernicusmarine

catalog = copernicusmarine.describe(include_datasets=True)
```
<br>
The attribute "include_datasets=True" will be deprecated in the next version.

The catalog has a lot of information. To filter that out and find what you need, you can use the following command lines, using as example the OSTIA dataset:

```
# The catalog has a lot information. Finding what we need.
cat_select = list()
for cc in catalog['products']:
    if 'OSTIA' in cc['title']:
        cat = cc['datasets'][0]#['versions'][0]['parts'][0]['services']
        cat_select.append(cat)
```
<br>
To get more information about the variable you need to use the following line:

```
[f"{service['service_type']['service_name']} : {[variable['short_name'] for variable in service['variables']]}"  for service in cat['versions'][0]['parts'][0]['services']]
```
<br>

And finally to do the download. Assuming that cat_selected has more than one option, like happen with OSTIA dataset, you'll need to select the index. In this case using the index 0:

```
import copernicusmarine
copernicusmarine.subset(
    dataset_id=cat_select[0]['dataset_id'],
    variables=['analysed_sst'],
    minimum_longitude=142,
    maximum_longitude=160,
    minimum_latitude=-45,
    maximum_latitude=-15,
    minimum_depth=0,
    maximum_depth=0,
    force_download=True,
    username='your_username',
    password=r'your_password',
    start_datetime="2022-01-01",
    end_datetime="2022-12-31"
  
)
```
<br>

## Credentials
There is a way to export the user credentials to allow you to download without exposing your user-name and password.

    - on UNIX platforms:

        export COPERNICUSMARINE_SERVICE_USERNAME=your_username

        export COPERNICUSMARINE_SERVICE_PASSWORD=your_password
        ​

    - on Windows platforms:

        set COPERNICUSMARINE_SERVICE_USERNAME=your_username

        set COPERNICUSMARINE_SERVICE_PASSWORD=your_password




