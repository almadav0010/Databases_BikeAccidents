import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle 

# Load datasets using forward slashes
accidents = pd.read_pickle("Datacleaning on public databases/dataset.pkl")
partijen = pd.read_csv('Datacleaning on public databases/Partijen.txt', sep=',')

ote_mapping = {
    64: 'Bicycle',
    66: 'E-bike'
}

# Filter parties and add the readable vehicle type column
bicyclists = partijen[partijen['OTE_ID'].isin([64, 66])].copy()
bicyclists['VEHICLE_TYPE'] = bicyclists['OTE_ID'].map(ote_mapping)

# Get unique accident numbers
bike_accident_numbers = bicyclists['VKL_NUMMER'].unique()

# Filter the accidents list
bike_accidents = accidents[accidents['VKL_NUMMER'].isin(bike_accident_numbers)]
df_filtered = bike_accidents.iloc[:, [0, 1, 6, 10, 26, 54, 55, 56]].copy()

# Map categories to English
ap3_mapping = {
    'LET': 'Wounded',
    'UMS': 'Material damage',
    'DOD': 'Lethal'
}

df_filtered['AP3_CODE'] = df_filtered['AP3_CODE'].map(ap3_mapping)

# --- MERGE THE BIKE TYPE INTO YOUR FINAL DATAFRAME ---
# We select only the accident number and vehicle type from bicyclists, 
# then merge it into df_filtered based on 'VKL_NUMMER'.
bike_types_subset = bicyclists[['VKL_NUMMER', 'VEHICLE_TYPE']].drop_duplicates(subset=['VKL_NUMMER'])
df_filtered = df_filtered.merge(bike_types_subset, on='VKL_NUMMER', how='left')

# Save to CSV (now including VEHICLE_TYPE)
df_filtered.to_csv("Database_with_location.csv", index=False)