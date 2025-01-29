"""
Process an text file to count occurrences each part of speech in the text.

"""

# Import from Python Standard Library
import pathlib

# Import from external packages
import spacy
import pandas as pd

# Import from local project modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

fetched_folder_name: str = "data"
processed_folder_name: str = "data_processed"
file_to_process: str = "constitution.txt"

#####################################
# Define Functions
#####################################
def parts_of_speech_count():
    '''Count the number of parts of speech in the text file.'''
    # Load the spaCy model
    nlp = spacy.load("en_core_web_sm")

    # Read the text from the file
    with open(pathlib.Path(__file__).parent / fetched_folder_name / file_to_process, "r", encoding="utf-8") as file:
        text = file.read()

    # Process the text with spaCy
    doc = nlp(text)

    # Count the number of parts of speech
    pos_counts = doc.count_by(spacy.attrs.POS)

    # Map the part of speech ID to the human-readable name
    pos_names = {id: nlp.vocab[id].text for id in pos_counts.keys()}

    # Create a DataFrame with the part of speech names and the corresponding counts
    result_df = pd.DataFrame({"pos": [pos_names[id] for id in pos_counts.keys()], "count": pos_counts.values()})
    
    # Sort the DataFrame by count in descending order
    result_df = result_df.sort_values(by='count', ascending=False)
    print(result_df)

    #Export the result DataFrame to a CSV file
    outfile = pathlib.Path(__file__).parent / processed_folder_name / "constitution_parts_of_speech_counts.csv"
    outfile.parent.mkdir(parents=True, exist_ok=True)
    result_df.to_csv(outfile, index=False)

    print(f"Written to CSV at {outfile}.")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting CSV processing...")
    parts_of_speech_count()
    logger.info("CSV processing complete.")