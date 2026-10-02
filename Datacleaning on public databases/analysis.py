import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle 

ongevallen = pd.read_pickle("dataset.pkl")
partijen = pd.read_csv('Partijen.txt', sep=',')

fietsers = partijen[partijen['OTE_ID'].isin([64, 66])]

# Stap 3: Haal een lijst op met alle unieke ongevalnummers waar een fietser bij zat
fiets_ongeval_nummers = fietsers['VKL_NUMMER'].unique()

# Stap 4: Filter de ongevallenlijst zodat je alleen deze ongevallen overhoudt
fiets_ongevallen = ongevallen[ongevallen['VKL_NUMMER'].isin(fiets_ongeval_nummers)]
df_filtered = fiets_ongevallen.iloc[:, [0, 1, 6, 10, 26, 54, 55, 56]]
# Bekijk het resultaat
ap3_mapping = {
    'LET': 'Wounded',
    'UMS': 'Material damage',
    'DOD': 'Lethal'
}

# Option 1: .map() 
# (Fastest, but will turn any code NOT in your dictionary into NaN)
df_filtered['AP3_CODE'] = df_filtered['AP3_CODE'].map(ap3_mapping)

df_filtered.to_csv("Database_with_location.csv")