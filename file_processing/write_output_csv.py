import json
import csv
from .flatten_json import flatten_json

def write_output_csv(OUTPUT_JSON_FILE, OUTPUT_CSV_FILE):
    # Load your JSON data
    with open(OUTPUT_JSON_FILE) as json_file:
        data = json.load(json_file)

    # Flatten your data
    flat_data = flatten_json(data)

    # Write to CSV
    keys = flat_data[0].keys()
    with open(OUTPUT_CSV_FILE, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(flat_data)
