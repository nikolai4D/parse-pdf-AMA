import csv
from .process_row import process_row

def process_csv_file(dict_with_docs, CSV_FILE_PATH, CSV_DELIMITER, SKIP_INDICATOR, DEFAULT_SKIP_PAGES):
    """
    Process the CSV file.

    Parameters:
    dict_with_docs (dict): The dictionary that stores the processed data from each document.
    """
    with open(CSV_FILE_PATH, mode='r', encoding='utf-8-sig') as csvfile:
        csv_reader = csv.DictReader(csvfile, delimiter=CSV_DELIMITER)

        for row in csv_reader:
            process_row(row, dict_with_docs, SKIP_INDICATOR, DEFAULT_SKIP_PAGES)
