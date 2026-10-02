import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle 

accidents = pd.read_pickle("dataset.pkl")
partijen = pd.read_csv('Partijen.txt', sep=',')

byciclers = partijen[partijen['OTE_ID'].isin([64, 66])]

# Step 3: Produce a list of all unique accident ids/numbers involving bikers
bike_accident_numbers = byciclers['VKL_NUMMER'].unique()

# Stap 4: Filter the accidents list s.t. je alleen these accidents overhoudt
fiets_accidents = accidents[accidents['VKL_NUMMER'].isin(bike_accident_numbers)]
df_filtered = fiets_accidents.iloc[:, [0, 1, 6, 10, 26, 54, 55, 56]]
# Map categories to english
ap3_mapping = {
    'LET': 'Wounded',
    'UMS': 'Material damage',
    'DOD': 'Lethal'
}

# Option 1: .map() 
# (Fastest, but will turn any code NOT in your dictionary into NaN)
df_filtered['AP3_CODE'] = df_filtered['AP3_CODE'].map(ap3_mapping)

df_filtered.to_csv("Database_with_location.csv")
