# First Import Code Exercise
# Importing Packages
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

# Loading data
# This data represents KRDU(Raleigh Durham International Airport) temperatures from 1887 to 2025 (in deg C?)

file_path = '/Users/theo/Documents/CC/EV228/ev_228/data/KRDU_temp_188708-202508.csv'
df_data = pd.read_csv(file_path)
df_sel = df_data['NOV']
print(df_sel)


def select_variable(file_path, sel_var):
    df_data = pd.read_csv(file_path)
    df_sel = df_data[sel_var]
    df_sel = df_sel.replace(999.90, np.nan)
    print(df_sel)
    return df_sel


def complete_var(file_path, sel_var):

    # Import and select data
    df_data = pd.read_csv(file_path)
    df_sel = df_data[sel_var] 
    df_date = df_data['YEAR']
    df_date = pd.to_datetime(df_date, format = '%Y')
    df_sel = df_sel.replace(999.90, np.nan)

    # Calculate Stats
    dict_stats = {
        'mean': np.mean(df_sel),
        'median': np.median(df_sel),
        'std': np.std(df_sel)
    }
    print(dict_stats)

    # Graph
    fig, ax = plt.subplots()
    plt.plot(df_date, df_sel, color='red', label=f'Temperature in {sel_var}')
    plt.xlabel('Year')
    plt.ylabel('temperature, deg C')
    plt.legend()    
    plt.title(f'Average Temperature {sel_var} ({min(df_date.dt.year)}-{max(df_date.dt.year)})')
    plt.show()
    return df_sel, df_date
