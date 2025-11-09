# ev_228 Individual Project
Code for EV228 individual project

# Project Summary
The aim of this project was to explore atmospheric and vegetation changes over the amazon rainforest due to deforestation over the past 70 years using ERA5 Reanalysis data

# Geneating the figures
To generate figures using ERA5 data you can call the amazon_module code. The inputs needed are the filepath to the data, the name of the varaible you are visualizing. The first function, make_map, also needs the additional input of a selected date to view. The warming_detrend function is intended to be used with surface temperature data as it includes a detrend function to removal warming over the past 70 years.

# Code Index
amazon_module.py - file that contains functions to make a time = 0 map and an anomaly map
map_module.py - file that loads amazon_module and runs the functions to generate maps

No generative AI has been used on this project.
