# import Python packages
import xarray as xr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import matplotlib.cm as cm
import cartopy.feature as cfeature
import cmocean

# Part 2 - Station Data

df = pd.read_csv('/Users/theo/Documents/CC/EV228/ev228_data/SGM00061600_temp_189201-202508.csv')
df_var = df['metANN']
df_x = df['YEAR']
df_cleaned = df_var[df_var != 999.9]
df_x1 = df_x[df_var != 999.9]

dict_stats = {
    'mean': np.mean(df_cleaned),
    'std': np.std(df_cleaned),
    'max' : np.max(df_cleaned),
    'min' : np.min(df_cleaned)
}  

fig, ax = plt.subplots()
plt.plot(df_x1, df_cleaned, color = 'green', linewidth=2)
plt.xlabel('year')
plt.ylabel('annual mean temperature (°C)')
plt.title('Saint Louis, Senegal (1892-2025)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig('/Users/theo/Documents/CC/EV228/ev228_data/sg_temp_1892-2025.png')

# Part 3 - Gridded Data Analysis
ds = xr.open_dataset('/Users/theo/Documents/CC/EV228/ev228_data/era5_10mwind_1980-1989.nc')
da = ds['si10']
dmean = da.mean('valid_time')
print(dmean)
fig = plt.figure(figsize=(9.5, 4.5), layout='constrained')
ax = plt.axes(projection=ccrs.PlateCarree())
dmean.plot.pcolormesh(
        x = 'longitude',
        y = 'latitude',
        ax = ax,
        transform = ccrs.PlateCarree(),
        extend = 'both',
        cmap = cmocean.cm.speed,
        add_colorbar = True,
        cbar_kwargs = {'label': 'wind speed (m/s)'}
)
ax.set_title('Average 10m Wind Speed from ERA5 (1980-1989)')
ax.add_feature(cfeature.COASTLINE)
ax.gridlines(crs=ccrs.PlateCarree(),
            draw_labels=True,
            linewidth=1,
            color='gray',
            alpha=0.5,
            linestyle='--')
plt.savefig('/Users/theo/Documents/CC/EV228/ev228_data/era5_10mwind_1980-1989.png')