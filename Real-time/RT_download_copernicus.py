'''
This script is meant to download datasets from Copernicus and can be applied
in Real Time analysis.

** You need to have a Copernicus EU account in order to download data. **

At the moment, this script is set to download:
    - SST dataset (for a specific OSTIA product), 
    - SSH 
    - CORA (Temperature and Salinity over depth)

The product names are: SST, SSH, CORA

Example inputs:
username = as string
password = as string like r'' to convert it to raw string and ignore special characters
st_date = string in the format YYYY-MM-DD
nd_date = string in the format YYYY-MM-DD
output_path = as string pointing to the path you want to save the file
product = string with SST or SSH.

The maximum date range is limited to the last data in the dataset.

RUNNING IN A TERMINAL: you can provide the arguments from the terminal command line. Just change the arguments with your needs and username and password. Just type, no need to use strings.

Example:
python RT_download_copernicus.py username password 2019-01-01 2020-01-01 ./copernicus_data SST

RUNNING INSIDE PYTHON: You need to change the variables at the bottom of this script with your credentials and other informations.And "run RT_download_copernicus" in a python terminal.


Fernando Sobral - 8th Nov 2024

mod. FS on 20th Feb 2025: adapted to the copernicusmarine API update.
                          Added ways to choose more than one product and to give the arguments from the terminal
mod. FS on 15th May 2025: added CORA dataset and changed maximum depth for subsurface data.
'''

#========================================================

import copernicusmarine
import sys


#========================================================

# To get the product_id you must go to the website page and check it.
def get_catalog(product):
    if product == 'SST':
        product_id = 'SST_GLO_SST_L4_REP_OBSERVATIONS_010_011'
        discrete = False
    elif product == 'SSH':
        product_id = 'SEALEVEL_GLO_PHY_L4_MY_008_047'
        discrete = False
    elif product == 'CORA':
        product_id = 'INSITU_GLO_PHY_TS_DISCRETE_MY_013_001'
        discrete = True

    catalog = copernicusmarine.describe(product_id=product_id)
    return catalog, discrete


def download(username, password, st_date, nd_date, output_path, product, min_lat=-45, max_lat=-15, min_lon=142, max_lon=170):
    
    catalog, discrete = get_catalog(product)

    if not discrete:
        copernicusmarine.subset(
            dataset_id=catalog.products[0].datasets[0].dataset_id,
            minimum_longitude=min_lon,
            maximum_longitude=max_lon,
            minimum_latitude=min_lat,
            maximum_latitude=max_lat,
            minimum_depth=0,
            maximum_depth=8000,
            username=username,
            password=password,
            start_datetime=st_date,
            end_datetime=nd_date,
            output_directory=output_path
        
        )
    else:
        copernicusmarine.get(
            dataset_id=catalog.products[0].datasets[0].dataset_id,
            username=username,
            password=password,
            output_directory=output_path
        )

# ===================================================
# Running


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print('Remember that if your password has special characters you should use \ before the character to scaped and to be recognised as a string.')
        download(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
    else:
        username = 'fnogueiraca'
        password = r'S125*\U298.+32xC'
        st_date = "2019-01-01"
        nd_date = "2019-02-01"
        output_path = './'
        product='CORA'
        download(username, password, st_date, nd_date, output_path, product)





'''EOF'''