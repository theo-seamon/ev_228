# import Python packages
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import cmocean
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader

def make_map(file_path, var_name):
        # Importing amazon boundary and making a cartopy shape feature
        amazon_boundary = shpreader.Reader('/Users/theo/Documents/CC/EV228/ev228_data/archive/amazon_biome/amazonia.shp')
        geometries = amazon_boundary.geometries()
        shape_feature = cfeature.ShapelyFeature(geometries, ccrs.PlateCarree(), edgecolor='black', facecolor='none', linewidth=2)

        #  Importing dataset
        ds = xr.open_dataset(file_path)
        da = ds[var_name]
        ds1 = da.isel(valid_time = 0)

        # Plotting figure
        fig = plt.figure(figsize=(9.5, 4.5), layout='constrained')
        ax = plt.axes(projection=ccrs.PlateCarree())
        lon_min = -90
        lon_max = -30
        lat_min = -30
        lat_max = 15
        ax.set_extent([lon_min, lon_max, lat_min, lat_max], crs=ccrs.PlateCarree())
        ds1.plot.pcolormesh(
                x = 'longitude',
                y = 'latitude',
                ax = ax,
                transform = ccrs.PlateCarree(),
                extend = 'both',
                # cmap = cmocean.cm.thermal,
                add_colorbar = True,
                cbar_kwargs = {'label': 'wind speed (m/s)'}
        )
        ax.set_title('1951 Map')
        ax.add_feature(cfeature.COASTLINE)
        ax.add_feature(shape_feature)
        ax.gridlines(crs=ccrs.PlateCarree(),
                draw_labels=True,
                linewidth=1,
                color='gray',
                alpha=0.5,
                linestyle='--')
        plt.show()

def make_anom(filepath, var_name):
        # Importing amazon boundary and making a cartopy shape feature
        amazon_boundary = shpreader.Reader('/Users/theo/Documents/CC/EV228/ev228_data/archive/amazon_biome/amazonia.shp')
        geometries = amazon_boundary.geometries()
        shape_feature = cfeature.ShapelyFeature(geometries, ccrs.PlateCarree(), edgecolor='black', facecolor='none', linewidth=2)

        #  Importing dataset
        ds = xr.open_dataset(filepath)
        da = ds[var_name]
        ds1 = da.sel(valid_time=slice('2003-01-01', '2024-12-31')).mean(dim='valid_time')
        ds2 = da.sel(valid_time=slice('1950-01-01', '1980-12-01')).mean(dim='valid_time')
        anom = ds1-ds2
        minV = anom.min()
        maxV = anom.min()


        # Plotting figure
        fig = plt.figure(figsize=(9.5, 4.5), layout='constrained')
        ax = plt.axes(projection=ccrs.PlateCarree())
        lon_min = -90
        lon_max = -30
        lat_min = -30
        lat_max = 15
        ax.set_extent([lon_min, lon_max, lat_min, lat_max], crs=ccrs.PlateCarree())
        anom.plot.contourf(
                x = 'longitude',
                y = 'latitude',
                ax = ax,
                lev = np.arange(-maxV, maxV),
                transform = ccrs.PlateCarree(),
                extend = 'both',
                cmap = cmocean.cm.curl,
                add_colorbar = True,
                cbar_kwargs = {'label': 'wind speed (m/s)'}
        )
        ax.set_title('Anomaly Map')
        ax.add_feature(cfeature.COASTLINE)
        ax.add_feature(shape_feature)
        ax.gridlines(crs=ccrs.PlateCarree(),
                draw_labels=True,
                linewidth=1,
                color='gray',
                alpha=0.5,
                linestyle='--')
        plt.show()

