'''
This script can be used to DOWNLOAD (using HTTPS) or to READ (usign OPENDAP) Fish Soop data from thredds server.

To DOWNLOAD you'll need to specify a path where the files will be saved.

To READ the file, you will need to loop through the list of dataset and extract the netcdf information that you want, such as, coordinates, temperature, depth, etc.

Fernando Sobral - 20th Nov 2024
'''

# ---------------------------------------------------------------
# You need to install siphon if you don't have it. 
# mamba install siphon, or conda install siphon

from siphon.catalog import TDSCatalog
import xarray as xr #you need it if just reading the file.

# ---------------------------------------------------------------
# Defining functions to be used

def list_catalog(catalog_url, list_dataset, indent=0):
    """Recursively list datasets and sub-catalogs in a THREDDS catalog."""
    catalog = TDSCatalog(catalog_url)
    print(" " * indent + f"Catalog: {catalog.catalog_url}")

    # List datasets
    for dataset_name, dataset in catalog.datasets.items():
        print(" " * (indent + 2) + f"Dataset: {dataset_name}")
        print(f"Access URLs: {dataset.access_urls}")
        list_dataset.append(dataset.access_urls)

    # List sub-catalogs
    for ref_name, ref in catalog.catalog_refs.items():
        print(" " * (indent + 2) + f"Sub-catalog: {ref_name}")
        list_catalog(ref.href, list_dataset, indent=indent + 4)

    return list_dataset

#
#
def download_fishsoop(folder_path, list_dataset):
    import requests
    import os

    for ff in list_dataset:
        response = requests.get(ff['HTTPServer'])
        if response.status_code == 200:
            with open(os.path.join(f"{folder_path}, {ff['HTTPServer'].split('/')[-1]}"), "wb") as f:
                f.write(response.content)
            print("File %s downloaded successfully." % ff['HTTPServer'].split('/')[-1])
        else:
            print("Failed to download file:", response.status_code)

def read_fishsoop(list_dataset):
    for ff in list_dataset:
        print('Reading file %s' % (ff))
        ds = xr.open_dataset(ff)




# ---------------------------------------------------------------
 
# 
# To extract the path and filenames needed to read/download the files.
#

# Specifying the URL where the FISH-SOOP catalog exists.
# LIST_DATASET will contain all the information from all the files stores in the thredds.

catalog_url = "https://thredds.aodn.org.au/thredds/catalog/IMOS/SOOP/SOOP-FishSOOP/REALTIME/catalog.xml"
list_dataset = list()

list_dataset = list_catalog(catalog_url, list_dataset)

# 
# 
# DOWNLOADING:
# Change FOLDER_PATH according. This is just an example to download 10 files. Remove [:10] if you want to donwload all the files.
folder_path = '../temp_data'
download_fishsoop(folder_path, list_dataset[:10])

# 
# 
# READING
# When reading the file, you have to decide what you want to do. If you want to concatenate the temperature and depth, for example, you'll need to extract that information from the dataset. This part just mean to give you a start.
read_fishsoop(list_dataset)



'''EOF'''