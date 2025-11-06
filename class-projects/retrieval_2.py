import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

# Import and select data
df_data = pd.read_csv('/Users/theo/Documents/CC/EV228/ev228_data/ASM00094998_temp_194804-202508.csv')
print(df_data)
df_sel = df_data['metANN'] 
df_date = df_data['YEAR']
df_date = pd.to_datetime(df_date, format = '%Y')
df_cleaned = df_sel[df_sel != 999.9]
df_x1 = df_date[df_sel != 999.9]

# Calculate Stats
dict_stats = {
    'mean': np.mean(df_cleaned),
    'std': np.std(df_cleaned),
    'max': df_cleaned.max(),
    'min': df_cleaned.min()
}
print(dict_stats)

# Graph
fig = plt.figure()
plt.plot(df_x1, df_cleaned, color='red')
plt.xlabel('year')
plt.ylabel('temperature, deg C')
plt.xlim(df_x1.min(), df_x1.max())
plt.grid(True, linestyle='--', alpha=0.6)
plt.title(f'Macquarie Island Average Annual Temperature ({min(df_date.dt.year)}-{max(df_date.dt.year)})')
plt.show()
