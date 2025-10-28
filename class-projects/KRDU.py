# First Import Code Exercise
# Importing Packages
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

# Loading data
# This data represents KRDU temperatures from 1887 to 2025 (in deg C?)
df_data = pd.read_csv('/Users/theo/Documents/CC/EV228/ev_228/data/KRDU_temp_188708-202508.csv')
df_nov = df_data['NOV']
df_nov = df_nov[:-1]
df_date = df_data['YEAR']
df_date = pd.to_datetime(df_date, format = '%Y', errors = 'coerce')
df_date = df_date[:-1]

# Graphing Data
fig, ax = plt.subplots()
ax.plot(df_date, df_nov, color='red', label='Temperature in November')
plt.xlabel('time')
plt.ylabel('temperature, deg C')
plt.legend()
plt.title('Average Temperature in November')
plt.show()