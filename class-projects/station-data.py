# Importing Packages
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import KRDU as krdu

# Using the select_variable function on weather data from different locations and over different dates
krdu.select_variable('/Users/theo/Documents/CC/EV228/ev_228/data/Practical4_Data/AYW00090001_temp_195702-202508.csv', 'OCT')
krdu.select_variable('/Users/theo/Documents/CC/EV228/ev_228/data/Practical4_Data/BR038014410_temp_189601-202508.csv', 'SEP')
krdu.select_variable('/Users/theo/Documents/CC/EV228/ev_228/data/Practical4_Data/IN020100400_temp_189101-202508.csv', 'M-A-M')
krdu.select_variable('/Users/theo/Documents/CC/EV228/ev_228/data/Practical4_Data/KSM00047108_temp_190710-202508.csv', 'JAN')
krdu.select_variable('/Users/theo/Documents/CC/EV228/ev_228/data/Practical4_Data/ROE00108901_temp_188001-202508.csv', 'FEB')
krdu.select_variable('/Users/theo/Documents/CC/EV228/ev_228/data/Practical4_Data/RSM00021432_temp_193601-202508.csv', 'MAR')
krdu.select_variable('/Users/theo/Documents/CC/EV228/ev_228/data/Practical4_Data/SG000061641_temp_189906-202508.csv', 'JUN')
krdu.select_variable('/Users/theo/Documents/CC/EV228/ev_228/data/Practical4_Data/USW00093009_temp_190801-202508.csv', 'D-J-F')

# Using the complete_var function on different dataset 
krdu.complete_var('/Users/theo/Documents/CC/EV228/ev_228/data/Practical4_Data/RSM00021432_temp_193601-202508.csv', 'MAR')

# Example of using these functions
path_name = '/Users/theo/Documents/CC/EV228/ev_228/data/Practical4_Data/RSM00021432_temp_193601-202508.csv'
var_name = 'MAR'
krdu.select_variable(path_name, var_name)
krdu.complete_var(path_name, var_name)
