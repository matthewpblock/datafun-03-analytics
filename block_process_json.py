"""
Process an text file to count occurrences each part of speech in the text.

"""

# Import from Python Standard Library
import pathlib

# Import from external packages
import pandas as pd
import json
import matplotlib.pyplot as plt
import numpy as np

# Import from local project modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

fetched_folder_name: str = "data"
processed_folder_name: str = "data_processed"
file_to_process: str = "players.json"

#####################################
# Define Functions
#####################################
def height_to_inches(height):
    '''Convert height from feet-inches format to inches.'''
    feet, inches = height.split('-')
    return int(feet) * 12 + int(inches)

def process_json_file():
    '''Process a JSON file to count occurrences of each player.'''
    # Read the JSON file
    with open(pathlib.Path(__file__).parent / fetched_folder_name / file_to_process, "r", encoding="utf-8") as file:
        data = json.load(file)
    
    # Use json_normalize to flatten the nested JSON structure
    df = pd.json_normalize(data['data'])
    
    # Select the height field
    df['height_inches'] = df['height'].apply(height_to_inches)
    
    # Sort the DataFrame by height in inches from smallest to largest
    height_df = df[['height', 'height_inches']].sort_values(by='height_inches')
    
    # Print the DataFrame with the height field
    print(height_df.head())
    
    # Plot the height distribution
    plt.hist(height_df['height_inches'], bins=range(height_df['height_inches'].min(), height_df['height_inches'].max() + 1, 1))
    plt.xlabel('Height (inches)')
    plt.ylabel('Frequency')
    plt.title('Height Distribution of NBA Players')
    
    # Export the the histogram as a jpg file
    outfile = pathlib.Path(__file__).parent / processed_folder_name / "player_height_histogram.jpg"
    outfile.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(outfile, format='jpg')
    plt.show()

    logger.info(f"Heights histogram saved as jpg at {outfile}.")
    
#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting CSV processing...")
    process_json_file()
    logger.info("CSV processing complete.")