# import Python packages
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cmocean

def era_plot(file_name, variable_name, output_dir, filename):
    ds = xr.open_dataset(file_name)
    da = ds[variable_name]
    dmean = da.mean('valid_time')
    fig = plt.figure(figsize=(9, 4.5))
    lev = np.arange(210, 310)
    ax = plt.axes(projection=ccrs.PlateCarree())
    dmean.plot.pcolormesh(
        x = 'longitude',
        y = 'latitude',
        ax = ax,
        transform = ccrs.PlateCarree(),
        extend = 'both',
        levels = lev,
        cmap = cmocean.cm.thermal,
        add_colorbar = True,
        cbar_kwargs = {'label': 'Temperature ($^\circ K$)'}
    )
    ax.set_title(f'Average {variable_name} from ERA5')
    ax.add_feature(cfeature.COASTLINE)
    ax.gridlines(crs=ccrs.PlateCarree(),
                 draw_labels=True,
                 linewidth=1,
                 color='gray',
                 alpha=0.5,
                 linestyle='--')
    full_filepath = f'{output_dir}/{filename}.png'
    plt.savefig(full_filepath)
    print(full_filepath)
    plt.show()
    return dmean
    
era_plot('/Users/theo/Documents/CC/EV228/ev_228/data/era5_t2m_1997-2025.nc', 't2m', '/Users/theo/Documents/CC/EV228/ev228_data' ,'ERA5-plot')

# def era_stats(file_name, variable_name):
#     ds = xr.open_dataset(file_name)
#     da = ds[variable_name]
#     dmean = da.mean('valid_time')
#     dict_stats = {
#         'mean': dmean.mean(['latitude', 'longitude']),
#         'std' : dmean.std(['latitude', 'longitude'])
#     }
#     print(dict_stats)
#     return dict_stats, dmean

# era_stats('/Users/theo/Documents/CC/EV228/ev_228/data/era5_t2m_1997-2025.nc', 't2m')