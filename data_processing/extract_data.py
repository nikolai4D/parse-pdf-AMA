import os
import pdfplumber
import uuid

from .group_by_doctop import group_by_doctop
from .to_int_or_none import to_int_or_none
from .check_thresholds import check_thresholds
from .check_if_header_is_ama import check_if_header_is_ama
from .create_header import create_header
from .add_header_to_list import add_header_to_list

# Constants
DEFAULT_THRESHOLD_TOP = 158
DEFAULT_THRESHOLD_BOTTOM = 775
DEFAULT_PARAGRAPH_FONTSIZE_AVG = 12
DEFAULT_LINE_HEIGHT_BETWEEN_SAME_PARAGRAPH = 4

def extract_data(file_path, list_of_pages_to_skip, threshold_top_csv, threshold_bottom_csv):
    """
    Extracts relevant data from a PDF document, given a file path and specific parameters to guide extraction.

    This function reads a PDF document, removes certain pages if instructed, crops the pages based on provided thresholds,
    and identifies 'header' lines based on specific conditions. It also identifies the content for each header.
    The data is then structured into a dictionary for further use.

    Parameters:
    file_path (str): The path to the PDF document.
    list_of_pages_to_skip (list): A list of page numbers to skip during extraction.
    threshold_top_csv (int): The top limit for cropping pages of the PDF.
    threshold_bottom_csv (int): The bottom limit for cropping pages of the PDF.

    Returns:
    dict: The dictionary that contains the structured data from the PDF document. This includes a unique ID,
    the file name, and the extracted 'sections', which represent the content under each identified header.

    """

    threshold_top = to_int_or_none(threshold_top_csv) or DEFAULT_THRESHOLD_TOP
    threshold_bottom = to_int_or_none(threshold_bottom_csv) or DEFAULT_THRESHOLD_BOTTOM

    doc_structure = {
        'file_name': os.path.basename(file_path),
        'sections': [],
        'pdf_text': [],
        'id': str(uuid.uuid4()),
    }

    with pdfplumber.open(file_path) as pdf:

        # Initialize variables to replace later
        content_list = []
        current_header = []
        previous_header = {'title': '', 'page_number': 0}

        for page in pdf.pages:

            # Skip page if nr is in list
            page_number = page.page_number
            if page_number in list_of_pages_to_skip:
                continue

            # Extract text from the current page
            text = page.extract_words(extra_attrs=["fontname", "size",]) # check out why words

            # Creating a bounding box that is defined as (x0, top, x1, bottom), where x0 and x1 are the left and right coordinates of the bounding box, and top and bottom are the y-coordinates of the top and bottom of the bounding box.
            bbox = (0, threshold_top, page.width, threshold_bottom)

            # Now we can crop the page using the bounding box.
            cropped_page = page.crop(bbox)

            # Now you can extract the text from the cropped page and add it to the list of dictionaries.
            text_whole = cropped_page.extract_text(x_tolerance=3, y_tolerance=3, layout=True, x_density=7.25, y_density=13)
            doc_structure['pdf_text'].append({"text_whole": text_whole, "page_number": page_number})

            # Group the list of dictionaries by the rounded "doctop" value. This groups words in each line together.
            # It is grouped by doctop value because the doctop value is the y-coordinate of the top of the word, and therefore groups per line.
            grouped = group_by_doctop(text)

            for key in grouped:
                # CONSTANTS
                item = grouped[key]  # item is a line (list) containing words (elements = dictionaries).
                line = " ".join([item_["text"] for item_ in item])
                fontname = [item["fontname"] for item in item][0]
                bottoms = [item_["bottom"] for item_ in item]
                avg_bottom = sum(bottoms) / len(bottoms)
                line_info = {"line": line, "page_number": page_number, "text_whole": text_whole, 'doc_structure': doc_structure}
                is_fontname_bold = 'Bold' in fontname or 'bold' in fontname
                # END OF CONSTANTS

                # Check thresholds and skip if not met
                if not check_thresholds(avg_bottom, threshold_top, threshold_bottom):
                    continue

                # Check if line matches the "ama" header pattern and is bold
                if check_if_header_is_ama(line) and is_fontname_bold:
                    current_header, previous_header = create_header(content_list, current_header, line_info, previous_header)

        # Check if there is a current header and add it to the list
        if current_header:
            previous_header = add_header_to_list(content_list, current_header, previous_header)

    # Update the sections of the doc_structure
    doc_structure["sections"] =  content_list

    # Remove 'pdf_text' from the dictionary as it's no longer needed
    del doc_structure['pdf_text']

    return doc_structure








