# importing module
import amazon_module as am

# setting file paths
precip_data = '/Users/theo/Documents/CC/EV228/ev228_data/era5_cloud_precip/data_stream-moda_stepType-avgad.nc' # total precipitation /tp
cloud_data = '/Users/theo/Documents/CC/EV228/ev228_data/era5_cloud_precip/data_stream-moda_stepType-avgua.nc' #total cloud cover /tcc
hveg_data = '/Users/theo/Documents/CC/EV228/ev228_data/era5_land_hveg.nc' # high vegetation cover /lai_hv
evap_data = '/Users/theo/Documents/CC/EV228/ev228_data/era5_avgie_sel.nc' # evaporation data /e
variable = 'lai_hv' 
fp = hveg_data

# calling functions
am.make_map(fp, variable) # time = 0 
am.make_anom(fp, variable) # (2003-2024) - (1950-1980)