# PDF Text Extractor based on AMA-code

### About the Project

This Python script is designed to extract text from PDF files in a way that retains the structural format of the original document. It is particularly useful when dealing with structured documents where the structural format is significant to the meaning of the content. The script is designed to be compatible with documents following the AMA-code (Allmän Material- och Arbetsbeskrivning) structure, but can be adapted to suit other document formats.

The extraction process groups lines in the document together based on their proximity and attempts to detect and retain headers and associated content. The detection of headers is done by looking for patterns associated with the AMA code in the document. The text and the metadata are extracted and structured in a JSON and CSV format.

This project could be especially useful for professionals in the Swedish construction industry, academics, researchers or anyone interested in automated data extraction from PDF files.

### How it works

- The script starts by opening the PDF file and reading its contents.
- It groups the content based on the 'doctop' value of each line, which is a measure of the line's vertical position in the document. This helps group lines that belong to the same paragraph.
- It identifies headers in the document by looking for lines that match the AMA code pattern.
- The lines following the headers are grouped together as the content associated with that header.
- This process is repeated for each page of the PDF document.
- The extracted content and their respective headers are then structured and written into a JSON file and a CSV file.


### Requirements 
- Python 3.7 or higher

    The following Python libraries:
- pdfplumber
- re
- json
- csv
- os
- uuid

### Usage 

1. Clone the repository or download the script, and install the required dependencies.

    ```
    git clone https://github.com/nikolai4D/parse-pdf-AMA.git
    cd parse-pdf-AMA
    pip3 install -r requirements.txt
    ```

2. Prepare the CSV file "file_to_parse.csv" according to the example "file_to_parse.example.csv" located in the project. The CSV file should include the path to the PDF files and any specific settings for each file, like pages to skip and threshold values for top and bottom text extraction boundaries. (See [CSV File Configuration](https://github.com/nikolai4D/parse-pdf-AMA/blob/main/README.md#csv-file-configuration))

3. Run the script using the command: `python main.py` or `python3 main.py`.

4. The script will output a JSON file and CSV file named "output.json" and "output.csv" with the extracted content.


Remember to update the paths in the CSV file according to the location of your PDF files. The PDF files can be in any location as long as the path in the CSV file is correctly specified.


#### CSV File Configuration

In order for the script to work, you need to provide a CSV file named file_to_parse.csv. This file should be in the root directory of the project.

The CSV file should have the following headers:

    - file_path: The relative path from the project root to the PDF file.
    - skip_pages: A comma-separated list of page numbers to skip.
    - threshold_to`: An optional parameter to adjust the top threshold for data extraction.
    - threshold_bottom: An optional parameter to adjust the bottom threshold for data extraction.

If any of these parameters should be left as the default, simply leave the field empty.

Here is an example of what the CSV file might look like:

```
file_path;skip_pages;threshold_top;threshold_bottom;paragraph_fontsize;line_height_same_paragraph
<file_path_from_root1>;*;;;;
<file_path_from_root2>;1;50;775;;
<file_path_from_root3>;1,2,3;;;;
```

You can refer to `file_to_parse.example.csv` in the project root for an example of how to structure this CSV file.

Again, replace __<file_path_from_root>__ with the actual relative paths to your PDF files.

### Note

This script assumes that you are dealing with documents that follow the AMA code pattern, and this forms the basis of how the headers are recognized. If you are dealing with documents of a different structure, you might need to modify the way the headers are identified.

### Contributing

We welcome contributions to this project. Please fork this repository, make your changes, and submit a pull request. If you have any questions, feel free to open an issue. By contributing to this project, you agree that your contributions will be licensed under its GPL-3.0 license.

### Credits

This project was developed by Nikdev.


### Important Note

The PDF extraction tool is designed to parse through PDF files and output the content into a structured JSON file. The tool doesn't provide inherent data encryption or special security features. Thus, if you are working with sensitive data, it's crucial to handle it securely. Ensure that the input PDFs, the output JSON files, and the CSV files are all stored and handled in a secure manner to prevent any inadvertent data exposure.
