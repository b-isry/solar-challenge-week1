import os
import pandas as pd
import numpy as np

def fetch_data():
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, '..', 'data')
    
    file_names = {
        'benin_clean.csv': 'Benin', 
        'sierraleone_clean.csv': 'Sierra Leone',
        'togo_clean.csv': 'Togo'
        }
    
    dfs = []
    for file, country_name in file_names.items():
        file_path = os.path.join(data_dir, file)
        df = pd.read_csv(file_path)
        df['country'] = country_name
        dfs.append(df)
    
    combined_df = pd.concat(dfs, ignore_index = True)
    return combined_df

def get_top_regions(df, metric='GHI', n=5):
    return df.groupby('country')[metric].mean().reset_index().sort_values(by=metric, ascending=False).head(n)

