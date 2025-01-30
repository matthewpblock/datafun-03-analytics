# datafun-03-analytics
Created for Module 3 of Data Fundamentals course

# Description
This group of modules demonstrates pulling various file types from the web via requests and performing various types of data processing using pandas and other tools.
Processed outputs are exported to the /data_processed folder.

# Project Setup for Local Development
Clone repository from GitHub
    git clone https://github.com/matthewpblock/datafun-03-analytics

Set Terminal to project folder

Creat virtual environment
    py -m venv .venv

Activate virtual environment
    .venv\Scripts\activate

Select virtual environment for Python interpreter
    Ctrl + Shift + P
    Python: Select Interpreter
    .venv

Update pip
    py -m pip install --upgrade pip setuptools wheel

Install dependencies
    py -m pip install -r requirements.txt

# Usage
These modules could be adjusted and re-used for grabbing other web files or performing similar analysis on updated data sets.

# Included Modules
block_get_csv: pulls a csv from the web and saves a local copy (NBA shot data)
block_get_excel: pulls an .xls file from the web and saves a local copy (sample demographic data)
block_get_json: pulls a json from the web and saves a local copy (NBA player data)
block_get_text: pulls a txt file from the web and saves a local copy (US Constitution)
block_process_csv: analyzes the csv data using pandas with a focus on fadeaway shots, exports results to csv
block_process_excel: analyzes the .xls data using pandas to determine most frequent birthdays, exports results to csv
block_process_json: analyze height distribution of players in the json data set, exports histogram as jpg
block_process_text: analyzes parts of speech in the txt document using spacy, exports results to csv

# Acknowledgements
This project was built under the guidance of Dr. Denise Case (https://github.com/denisecase) for Data Fundamentals course at Northwest Missouri State University. Analysis relied heavily on Pandas and SpaCy.

# Contact Information
https://github.com/matthewpblock