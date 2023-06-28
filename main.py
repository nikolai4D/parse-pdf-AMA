from data_processing.extract_data import *
from file_processing.process_csv_file import process_csv_file
from file_processing.write_output_file import write_output_file
from file_processing.write_output_csv import write_output_csv

CSV_FILE_PATH = 'files_to_parse.csv'
CSV_DELIMITER = ';'
SKIP_INDICATOR = '*'
DEFAULT_SKIP_PAGES = []
OUTPUT_JSON_FILE = 'output.json'
OUTPUT_CSV_FILE = 'output.csv'


def main():
    """
    Main function to start the data extraction process.
    """
    dict_with_docs = {"docs": []}

    process_csv_file(dict_with_docs, CSV_FILE_PATH, CSV_DELIMITER, SKIP_INDICATOR, DEFAULT_SKIP_PAGES)
    write_output_file(dict_with_docs, OUTPUT_JSON_FILE)
    write_output_csv(OUTPUT_JSON_FILE, OUTPUT_CSV_FILE)

if __name__ == "__main__":
    main()
