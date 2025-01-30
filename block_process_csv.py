"""
This module processes basketball shot data from CSV files.

The module includes functions to analyze fadeaway shots, create histograms of occurrences of the day of the year from Excel files,
and process JSON files to extract and sort player height data. The results are exported to CSV and Excel files, and histograms
are saved as JPG images.

Functions:
    analyze_fadeaways(): Analyze fadeaway shots from the CSV file.

Global Variables:
    fetched_folder_name (str): The name of the folder containing the fetched data.
    processed_folder_name (str): The name of the folder to save the processed data.
    file_to_process (str): The name of the file to process.
"""
#####################################
# Import Modules
#####################################

# Import from Python Standard Library
from pathlib import Path
import csv

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
    """Analyze fadeaway shots from the CSV file.

    This function reads a CSV file containing basketball shot data, filters the data to include only fadeaway shots,
    counts the total number of fadeaway shots and the number of made fadeaway shots for each player, and calculates
    the percentage of made fadeaway shots. The results are sorted by the total number of fadeaway shots in descending order
    and exported to a CSV file.

    Returns:
        None
    """
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
    
        # Export the result DataFrame to a CSV file
    outfile = Path(__file__).parent / processed_folder_name / "fadeaway_analysis.csv"
    outfile.parent.mkdir(parents=True, exist_ok=True)
    result_df.to_csv(outfile, index=True)

    print(result_df)
    print(f"Written to CSV at {outfile}.")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting CSV processing...")
    analyze_fadeaways()
    logger.info("CSV processing complete.")