'''
---------------------------------------------------------------------------------------------------------------
This script will donwload mooring data from AODN thredds.


Fernando Sobral - 6th Jun 2025

---------------------------------------------------------------------------------------------------------------
'''

import xarray as xr
from siphon.catalog import TDSCatalog


# -------------------------------------------------------------------------------------------------------------


def load_latest_station_data(station_code, variable_keyword='TEMP'):
    """
    Loads the first NetCDF dataset that matches a variable from the specified station.
    
    Parameters:
    - station_code (str): 'CH070', 'CH100', 'SYD100', 'SYD140', 'BMP070', 'BMP120'
    - variable_keyword (str): partial match, e.g., 'TEMP'

    Returns:
    - xarray.Dataset
    """
    base_catalog_url = f'http://thredds.aodn.org.au/thredds/catalog/IMOS/ANMN/NSW/{station_code}/gridded_timeseries/catalog.xml'
    
    print(f'\n\n{base_catalog_url}')

    catalog = TDSCatalog(base_catalog_url)
    
    # Filter dataset names with the keyword
    matching_datasets = [ds for ds in catalog.datasets if variable_keyword in ds]
    
    if not matching_datasets:
        raise ValueError(f"No datasets found for {station_code} with keyword '{variable_keyword}'")
    
    dataset_url = catalog.datasets[matching_datasets[0]].access_urls['OPENDAP']
    return xr.open_dataset(dataset_url)


# -------------------------------------------------------------------------------------------------------------
# Reading mooring data

ch70   = load_latest_station_data('CH070' , 'TEMP')
ch100  = load_latest_station_data('CH100' , 'TEMP')
syd100 = load_latest_station_data('SYD100', 'TEMP')
syd140 = load_latest_station_data('SYD140', 'TEMP')
bmp70  = load_latest_station_data('BMP070', 'TEMP')
bmp120 = load_latest_station_data('BMP120', 'TEMP')

# -------------------------------------------------------------------------------------------------------------
# Saving data








'''EOF'''