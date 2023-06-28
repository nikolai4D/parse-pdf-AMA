from .add_content_to_header import add_content_to_header

def handle_header_object(content_list, previous_header, text_whole, doc_structure, dict_object):
    """
    Handles the scenario where the current object is a header. 
    This function updates the previous_id attribute of the current header object.
    If the last object in the content_list is a header, it adds content to that previous header.

    Parameters:
    content_list (list): The list of all content objects from the document.
    previous_header (dict): The dictionary representing the previous header in the document.
    text_whole (str): The whole text content of the current page.
    doc_structure (dict): The document structure dictionary.
    dict_object (dict): The dictionary representing the current header object.

    Returns:
    dict: The updated previous_header object.
    """

    for dictionary in reversed(content_list):
        if dictionary['type'] == "header":
            dict_object['previous_id'] = dictionary['id']
            break

    if len(content_list) == 0:
        dict_object['previous_id'] = None

    previous_header = add_content_to_header(content_list, previous_header, text_whole, dict_object, doc_structure)

    return previous_header
