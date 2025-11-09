# importing module
import amazon_module as am

# setting file paths
precip_data = '/Users/theo/Documents/CC/EV228/ev228_data/era5_cloud_precip/data_stream-moda_stepType-avgad.nc' # total precipitation /tp
sst = '/Users/theo/Documents/CC/EV333/Lab2Data/ERA5_monthly_t2m_regrid.nc' # t2m
cloud_data = '/Users/theo/Documents/CC/EV228/ev228_data/era5_cloud_precip/data_stream-moda_stepType-avgua.nc' #total cloud cover /tcc
hveg_data = '/Users/theo/Documents/CC/EV228/ev228_data/era5_land_hveg.nc' # high vegetation cover /lai_hv
evap_data = '/Users/theo/Documents/CC/EV228/ev228_data/era5_avgie_sel.nc' # evaporation data /e
variable = 'tcc' 
fp = cloud_data

# calling functions
am.make_map(fp, variable, '2025-10-01') # time = 0 
am.make_anom(fp, variable) # (2003-2024) - (1950-1980)
am.zscore(fp, variable, '2025-10-01')
am.warming_detrend('/Users/theo/Documents/CC/EV333/Lab2Data/ERA5_monthly_t2m_regrid.nc', 't2m')
