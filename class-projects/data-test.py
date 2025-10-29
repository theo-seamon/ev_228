import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import cmocean
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.util import add_cyclic_point

df_data = xr.open_dataarray('/Users/theo/Documents/CC/EV228/ev_228/data/3c8050c76cdb553d37fc8515bd5fd0e0.grib', engine='cfgrib')
df_data = df_data.mean('time')

cmap = cmocean.cm.thermal
lev = np.arange(-52.850235, 29.221008)
proj = ccrs.Robinson(central_longitude=180)
fig = plt.figure(figsize = (9, 4.5), dpi=300)
ax = plt.axes(projection = proj)

df_data.plot.contourf(
    x='longitude',
    y='latitude',
    ax=ax,
    transform=ccrs.PlateCarree(),
    levels=lev,
    extend='both',
    colors=cmap,
    add_colorbar=True,
    cbar_kwargs={"label":"Temperature ($^\circ C$)"})

ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.coastlines(
    resolution='110m')

gl = ax.gridlines(crs=ccrs.PlateCarree(),
                 draw_labels=True,
                 linewidth=1,
                 color='gray',
                 alpha=0.5,
                 linestyle='--')

ax.set_title("Mean 2m Temperature")
