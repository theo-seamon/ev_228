# import Python packages
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import cmocean
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader
from cartopy.util import add_cyclic_point

def make_map(file_path, var_name, time_sel):
        # Importing amazon boundary and making a cartopy shape feature
        amazon_boundary = shpreader.Reader('/Users/theo/Documents/CC/EV228/ev228_data/archive/amazon_biome/amazonia.shp')
        geometries = amazon_boundary.geometries()
        shape_feature = cfeature.ShapelyFeature(geometries, ccrs.PlateCarree(), edgecolor='black', facecolor='none', linewidth=2)

        #  Importing dataset
        ds = xr.open_dataset(file_path)
        da = ds[var_name]
        ds1 = da.sel(valid_time = time_sel, method = 'nearest')

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
                cbar_kwargs = {'label': 'total cloud cover'}
        )
        ax.set_title('Cloud cover over Amazon (2025)', fontweight = 'bold')
        ax.add_feature(cfeature.COASTLINE)
        ax.add_feature(shape_feature)
        ax.gridlines(crs=ccrs.PlateCarree(),
                draw_labels=True,
                linewidth=1,
                color='gray',
                alpha=0.5,
                linestyle='--')
        plt.savefig('/Users/theo/Documents/CC/EV228/ev228_data/Final_maps/map_1.png')
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
                cbar_kwargs = {'label': 'change in total cloud cover'}
        )
        ax.set_title('Mean total cloud cover (1950-1980) - (2003-2024)', fontweight = 'bold')
        ax.add_feature(cfeature.COASTLINE)
        ax.add_feature(shape_feature)
        ax.gridlines(crs=ccrs.PlateCarree(),
                draw_labels=True,
                linewidth=1,
                color='gray',
                alpha=0.5,
                linestyle='--')
        plt.savefig('/Users/theo/Documents/CC/EV228/ev228_data/Final_maps/map_2.png')
        plt.show()

# calculating z score
def zscore(filepath, var_name, time_sel):
        # Importing amazon boundary and making a cartopy shape feature
        amazon_boundary = shpreader.Reader('/Users/theo/Documents/CC/EV228/ev228_data/archive/amazon_biome/amazonia.shp')
        geometries = amazon_boundary.geometries()
        shape_feature = cfeature.ShapelyFeature(geometries, ccrs.PlateCarree(), edgecolor='black', facecolor='none', linewidth=2)

        #  Importing dataset
        ds = xr.open_dataset(filepath)
        da = ds[var_name]
        mu = da.mean(dim='valid_time')
        sigma = da.std(dim='valid_time')
        z_score = (da - mu) / sigma
        ds1 = z_score.sel(valid_time = time_sel)
        minV = ds1.min()
        maxV = ds1.min()


        # Plotting figure
        fig = plt.figure(figsize=(9.5, 4.5), layout='constrained')
        ax = plt.axes(projection=ccrs.PlateCarree())
        lon_min = -90
        lon_max = -30
        lat_min = -30
        lat_max = 15
        ax.set_extent([lon_min, lon_max, lat_min, lat_max], crs=ccrs.PlateCarree())
        ds1.plot.contourf(
                x = 'longitude',
                y = 'latitude',
                ax = ax,
                lev = np.arange(-maxV, maxV),
                transform = ccrs.PlateCarree(),
                extend = 'both',
                cmap = cmocean.cm.curl,
                add_colorbar = True,
                cbar_kwargs = {'label': 'z score'}
        )
        ax.set_title('Total cloud cover z-score (2025)', fontweight = 'bold')
        ax.add_feature(cfeature.COASTLINE)
        ax.add_feature(shape_feature)
        ax.gridlines(crs=ccrs.PlateCarree(),
                draw_labels=True,
                linewidth=1,
                color='gray',
                alpha=0.5,
                linestyle='--')
        plt.savefig('/Users/theo/Documents/CC/EV228/ev228_data/Final_maps/map_3.png')
        plt.show()


# Final fig? Detrend warming from data and calculate Z anomaly to see if deforestation is leading to abnormal warming?
def warming_detrend(filepath, var_name):
        # Importing amazon boundary and making a cartopy shape feature
        amazon_boundary = shpreader.Reader('/Users/theo/Documents/CC/EV228/ev228_data/archive/amazon_biome/amazonia.shp')
        geometries = amazon_boundary.geometries()
        shape_feature = cfeature.ShapelyFeature(geometries, ccrs.PlateCarree(), edgecolor='black', facecolor='none', linewidth=2)

        #  Importing dataset
        ds = xr.open_dataset(filepath)
        da = ds[var_name]
        
        def detrend(da, dim, deg=1):
                # detrend along a single dimension
                p = da.polyfit(dim=dim, deg=deg)
                fit = xr.polyval(da[dim], p.polyfit_coefficients)
                return da - fit

        da_detrend = detrend(da, 'time', deg = 1)
        mu = da_detrend.mean(dim='time')
        sigma = da_detrend.std(dim='time')
        z_score = (da_detrend - mu) / sigma
        ds1 = z_score.isel(time = 1004)
        cyclic_data, cyclic_lon = add_cyclic_point(ds1.values, coord=ds1['lon'])
        coords = {dim: ds1.coords[dim] for dim in ds.dims}
        coords['lon'] = cyclic_lon
        seamed_data = xr.Dataset(
                data_vars = {
                        "t2m" : xr.DataArray(cyclic_data, dims = ds1.dims, coords = coords)
                })
        minV = ds1.min()
        maxV = ds1.min()

        # Plotting figure
        fig = plt.figure(figsize=(9.5, 4.5), layout='constrained')
        ax = plt.axes(projection=ccrs.PlateCarree())
        lon_min = -90
        lon_max = -30
        lat_min = -30
        lat_max = 15
        # ax.set_extent([lon_min, lon_max, lat_min, lat_max], crs=ccrs.PlateCarree())
        seamed_data['t2m'].plot.contourf(
                x = 'lon',
                y = 'lat',
                ax = ax,
                levels = np.arange(-4, 5),
                transform = ccrs.PlateCarree(),
                extend = 'both',
                cmap = cmocean.cm.curl,
                add_colorbar = True,
                cbar_kwargs = {'label': 'z-score'}
        )
        ax.set_title('Temperature anomalies with detrended warming', fontweight = 'bold')
        ax.add_feature(cfeature.COASTLINE)
        ax.add_feature(shape_feature)
        ax.gridlines(crs=ccrs.PlateCarree(),
                draw_labels=True,
                linewidth=1,
                color='gray',
                alpha=0.5,
                linestyle='--')
        plt.savefig('/Users/theo/Documents/CC/EV228/ev228_data/Final_maps/map_4.png')
        plt.show()

# ds = xr.open_dataset('/Users/theo/Documents/CC/EV333/Lab2Data/ERA5_monthly_t2m_regrid.nc')
# da = ds['t2m'].sel(lon = '-3', lat = '38', method = 'nearest')

# def detrend(da, dim, deg=1):
#         # detrend along a single dimension
#         p = da.polyfit(dim=dim, deg=deg)
#         fit = xr.polyval(da[dim], p.polyfit_coefficients)
#         return da - fit

# da_detrend = detrend(da, 'time', deg = 1)

# fig, ax = plt.subplots(layout = 'constrained')
# ax.plot(da['time'], da, color="#272A59FF", lw = 2)
# plt.xlabel('year')
# plt.ylabel('temperature, K')
# # plt.xlim(df_x1.min(), df_x1.max())
# plt.grid(True, linestyle='--', alpha=0.6)
# plt.title('Temperature without detrend', fontweight = 'bold')
# ax.spines[['right', 'top']].set_visible(False)
# ax.set_facecolor("#F6F6F6FF")
# plt.savefig('/Users/theo/Documents/CC/EV228/ev228_data/Final_maps/predetrend_graph.png')
# plt.show()

# fig, ax = plt.subplots(layout = 'constrained')
# ax.plot(da_detrend['time'], da_detrend, color="#272A59FF", lw = 2)
# plt.xlabel('year')
# plt.ylabel('temperature, K')
# # plt.xlim(df_x1.min(), df_x1.max())
# plt.grid(True, linestyle='--', alpha=0.6)
# plt.title('Temperature detrended', fontweight = 'bold')
# ax.spines[['right', 'top']].set_visible(False)
# ax.set_facecolor("#F6F6F6FF")
# plt.savefig('/Users/theo/Documents/CC/EV228/ev228_data/Final_maps/detrend_graph.png')
plt.show()