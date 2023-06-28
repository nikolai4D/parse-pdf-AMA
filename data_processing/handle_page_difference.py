from .create_new_content import create_new_content

def handle_page_difference(content_list, previous_header, dictionary, doc_structure, remaining_text2):
    """
    Handles the difference between the current page number and the previous header's page number.

    If the difference is greater than 1, it means that there are pages in between the current page and the last header.
    For each of these pages, it adds the corresponding text to the previous header's content.
    It also adds the remaining text from the current page to the previous header's content.

    Parameters:
    content_list (list): The list of all extracted content sections from the PDF.
    previous_header (dict): A dictionary containing the information about the previous header including its content and page number.
    dictionary (dict): The current dictionary that is being processed and will be added to the content list.
    doc_structure (dict): The overall structure of the document, which includes the extracted text from each page.
    remaining_text2 (str): The remaining text on the current page after a match with a header has been found.

    Returns:
    dict: The updated previous header dictionary with new content added to its 'content' field.
    """
    if dictionary['page_number'][0] - previous_header['page_number'][0] > 1:
        page_nr_count = previous_header['page_number'][0] + 1

        while page_nr_count < dictionary['page_number'][0]:
            for dict in doc_structure['pdf_text']:
                if dict['page_number'] == page_nr_count:
                    previous_id = previous_header['content'][-1]['id']
                    parent_id = previous_header['id']
                    previous_header['content'].append(
                                    create_new_content(dict['text_whole'], page_nr_count, previous_id, parent_id))
            page_nr_count += 1

    previous_id = previous_header['content'][-1]['id']
    parent_id = previous_header['id']
    previous_header['content'].append(create_new_content(remaining_text2, dictionary['page_number'][0], previous_id, parent_id))

    for item in content_list:
        if item['id'] == previous_header['id']:
            item['content'] = previous_header['content']
