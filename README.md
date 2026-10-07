# Databases_BikeAccidents

This directory contains the code needed for 'Schema Design & Database Connection in Code'. 
There are five existing files, and one personal file needed to be made.

1. .env.example (follow this example file)
2. .gitignor (to not leak our credentials)
3. input_data.ipynb (our notebook where we actually load our database scheme, and fill up the tables with mockdata)
4. README.md (the file you are reading now :)) 
5. relation_schema.sql (the file where our schematics are loaded in. This is where all the relationships are mentioned on it)

*******************************
CREATE .env FILE! Follow .env.example structure!
*******************************

Without this .env file, you will not be able to connect to MySQL.

Only run the notebook. Everything will be explained in there.

## Used Databases
**1:**
The first databased used in analysis.py is "Bestand geregistreerde ongevallen in Nederland (BRON)"
It is the 2025 version, with more years available if needed. It is found on this website:
"https://verkeersveiligheid.ndw.nu/dataset/bestand-geregistreerde-ongevallen-in-nederland-bron"
This dataset uses a lot of vectorisation and normalization of the dataset.
For Dutch users this dataset is intuitivly, but changes were made on translation and clarification.
The data from BRON has not been changed or further cleaned. Not all columns were of intrest for us, so a subset was chosen. 

Statiscics:
Data owner:	Rijkswaterstaat (Rijk)
Status:	Available
Access:	Public

**2:**
The second databased used in 'fichier_database.ipynb' is a french database, published on the European Union website. 
(https://data.europa.eu/data/datasets/5d56becc8b4c412584b830c9?locale=en)
This dataset was more difficult to decifer, due to the language barrier and the use of vectorisation within the values.
So finding out which bicycles were being used was difficult. 
A 'Description des champs' was available on the website, where these descriptions became more clear.
The data cleaning steps used for this dataset is found in 'fichier_database.ipynb'.
The final data cleaning step was the deletion of 62 rows (out of 92K rows) with extreme outliers within age. 


Statistics:
Created: 16 August 2019
Updated: 09 June 2026
Publisher: Koumoul
E-Mail: mailto:contact@koumoul.com
Access Rights: public


## Data cleansing process
You can find documentation for the data cleaning process here: `\Week5\DATABASES USED.txt` & `\Week5|Datacleaning logbook .xlsx`

## Limitations of Our Database
- It cannot answer complex situations, such as:
  - Accident with an unregistered bicycle
- We found the longest name bike brand and city to be 27 character long, we added an error bound, and set the maximum characters for both 50, however if there is an insertion which has a more than 50 characters long city name or bike brand name, it will give an error.
- If we do not have certain information of any part(for example weather conditions on the accident day, if the person usually wears a helmet), we use NON NULL DEFAULT VALUES, this can cause bias and misleading results for queries(if we do not have rain effect score information for a significant number of accidents, it can cause incorrect derivations while querying):
  - For usual helmet wearing we assume false (most dutch people dont wear helmet so a false assumption is reasonable)
  - For weather effect score we assume 5 (on 1-10)
  - For rain effect score we assume 5 (on 1-10)
  - Cyclist accident: without data we assume person is not at fault
  - For other attributes if DEFAULT is used, it is DEFAULT NULL (it shows in query we do not have that information)


## Future Plans
Our future plans include improvements related to decrease the limitations and add useful functionalities.
- We assume:
  - For weather effect score we assume 5
  - For rain effect score we assume 5
  - For usual helmet wearing we assume false
However may these attributes could be investigated more, they may relate to each other, or the person's age.
- Visualization in python.
