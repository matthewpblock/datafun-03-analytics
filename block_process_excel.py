"""
Process an Excel file to count occurrences of a specific word in a column.

"""

# Import from Python Standard Library
import pathlib
import datetime as dt

# Import from external packages
import openpyxl
from openpyxl.chart import BarChart, Reference
from openpyxl.chart.axis import DateAxis
import pandas as pd

# Import from local project modules
from utils_logger import logger


#####################################
# Declare Global Variables
#####################################

fetched_folder_name: str = "data"
processed_folder_name: str = "data_processed"
file_to_process: str = "sample_data.xls"

#####################################
# Define Functions
#####################################
# Create a histogram of occurences of the day of the year in the Excel file
def create_histogram():
    '''Create a histogram of occurences of the day of the year into an Excel file.'''
    # Import data from Excel
    #------------------------------#
    infile = pathlib.Path(__file__).parent / fetched_folder_name / file_to_process
# Read Excel with explicit date parsing
    df = pd.read_excel(
        infile
    )   
    
    dates = pd.to_datetime(df['DATE '], format='%d/%m/%Y', errors='coerce')
    print(dates.head)
    
    # Count the number of occurrences of each day of the year
    day_counts = dates.dt.dayofyear.value_counts()
    print(day_counts)
    
    # Create a DataFrame with the day of the year and the corresponding counts
    result_df = pd.DataFrame({'day_of_year': day_counts.index, 'count': day_counts.values}).sort_values(by='day_of_year')
    print(result_df)
   
    
    # Export the day_counts Series to a new Excel file
    outfile = pathlib.Path(__file__).parent / processed_folder_name / "day_counts.csv"
    outfile.parent.mkdir(parents=True, exist_ok=True)
    result_df.to_csv(outfile, index=True)

    print(f"Written to CSV at {outfile}.")

    # Create a histogram chart of the day_counts
    #create_histogram_chart(day_counts, outfile)

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting CSV processing...")
    create_histogram()
    logger.info("CSV processing complete.")