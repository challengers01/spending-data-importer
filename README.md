# spending-data-importer
A Python script to load CSV data from financial accounts into SQLite database

## Basic Structure
data: Contains financial statements organized per year
src: Contains the python scripts to be executed

## How to Execute?
1. Run "python importcsvdata.py" in order to import all the data files into SQLite database
2. In order to view the SQLite data, download SQLiteStudio from https://sqlitestudio.pl/index.rvt

## Future:
* Add Intelligence to the importer to insert the "Category" based on Merchant Name
* Move the processed files to an archived folder /data/2017/Archive
* More to come...

