import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
import scipy.stats as stats
import seaborn as sns

# Import and select data
df_data = pd.read_csv('/Users/theo/Documents/CC/EV228/ev_228/data/KRDU_temp_188708-202508.csv')
print(df_data)
df_sel = df_data['metANN'] 
df_date = df_data['YEAR']
df_cleaned = df_sel[df_sel != 999.9]
df_x1 = df_date[df_sel != 999.9]
res = stats.linregress(df_x1, df_cleaned)

# Graph
fig, ax = plt.subplots(layout = 'constrained')
ax.scatter(df_x1, df_cleaned, color="#272A59FF", lw = 2)
ax.plot(df_x1, res.intercept + res.slope*df_x1, "#A62631FF", label = 'fitted line', ls = 'dashed', lw = 2)
plt.xlabel('year')
plt.ylabel('temperature, deg C')
plt.xlim(df_x1.min(), df_x1.max())
plt.grid(True, linestyle='--', alpha=0.6)
plt.title(f'Raleigh Durham Airport Weather Data (1887-2025)', fontweight = 'bold')
ax.spines[['right', 'top']].set_visible(False)
ax.set_facecolor("#F6F6F6FF")
plt.show()
