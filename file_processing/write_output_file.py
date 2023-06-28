import json

def write_output_file(dict_with_docs, OUTPUT_JSON_FILE):
    """
    Write the processed data to the output JSON file.

    Parameters:
    dict_with_docs (dict): The dictionary that stores the processed data from each document.
    """
    with open(OUTPUT_JSON_FILE, 'w', encoding='utf-8') as output_file:
        json.dump(dict_with_docs, output_file, indent=2, ensure_ascii=False)
