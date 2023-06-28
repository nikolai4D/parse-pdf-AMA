from data_processing.extract_data import extract_data

def process_row(row, dict_with_docs, SKIP_INDICATOR, DEFAULT_SKIP_PAGES):
    """
    Process each row from the CSV file.

    Parameters:
    row (dict): The current row in the CSV file.
    dict_with_docs (dict): The dictionary that stores the processed data from each document.
    """
    file_path_csv = row['file_path']
    skip_pages = row['skip_pages']
    threshold_top = row['threshold_top']
    threshold_bottom = row['threshold_bottom']

    list_pages_to_skip = skip_pages.split(",")

    if SKIP_INDICATOR in list_pages_to_skip:
        return

    if not list_pages_to_skip or len(list_pages_to_skip) == 1:
        list_pages_to_skip = DEFAULT_SKIP_PAGES

    list_pages_to_skip = [int(x) for x in list_pages_to_skip]

    output = extract_data(file_path_csv, list_pages_to_skip, threshold_top, threshold_bottom)
    dict_with_docs["docs"].append(output)
