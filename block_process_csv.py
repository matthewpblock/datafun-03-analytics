#####################################
# Import Modules
#####################################

# Import from Python Standard Library
from pathlib import Path
import csv
import statistics

import pandas as pd

# Import from local project modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################
fetched_folder_name: str = "data"
processed_folder_name: str = "data_processed"

#####################################
# Define Functions
#####################################
# Analyze Fadeaways
def analyze_fadeaways():
    '''Count fadeaway shots by each player from the CSV file and sort most to least.'''
    # Import data from CSV
    #------------------------------#
    infile = Path(__file__).parent / fetched_folder_name / "shots_raw.csv"
    df = pd.read_csv(infile)
    
    # Filter to rows where fadeaway is True
    fadeaway_df = df[df['fadeaway'] == True]
    
    # Count the number of fadeaways per player
    fadeaway_counts = fadeaway_df.groupby('name').size().sort_values(ascending=False)
    
    # Count the number of made fadeaways per player
    made_fadeaway_counts = fadeaway_df[fadeaway_df['made'] == True].groupby('name').size()
    
    # Reindex made_fadeaway_counts to match fadeaway_counts index and fill NaN with 0
    made_fadeaway_counts = made_fadeaway_counts.reindex(fadeaway_counts.index, fill_value=0)
    
    # Combine the counts into a single DataFrame
    result_df = pd.DataFrame({'fadeaway_count': fadeaway_counts, 'made_fadeaway_count': made_fadeaway_counts})
    
    # Convert made_fadeaway_count to int
    result_df['made_fadeaway_count'] = result_df['made_fadeaway_count'].astype(int)
    
    # Calculate fadeaway percentage
    result_df['fadeaway_percentage'] = (result_df['made_fadeaway_count'] / result_df['fadeaway_count']) * 100
    
    # Round fadeaway_percentage to one decimal place
    result_df['fadeaway_percentage'] = result_df['fadeaway_percentage'].round(1)
    
    # Sort the result DataFrame by fadeaway_count in descending order
    result_df = result_df.sort_values(by='fadeaway_count', ascending=False)
    
    print(result_df)

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting CSV processing...")
    analyze_fadeaways()
    logger.info("CSV processing complete.")