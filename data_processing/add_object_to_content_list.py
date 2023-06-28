import uuid
from .remove_duplicates import remove_duplicates
from .handle_header_object import handle_header_object
from .handle_non_header_object import handle_non_header_object


def add_object_to_content_list(type, content_list, current_object, previous_header):
    """
    Add an object to the content list and return the updated previous header.

    Parameters:
    object_type (str): The type of the object.
    content_list (list): The list of contents.
    current_object (list): The list of items in the current object.
    previous_header (dict): The previous header dictionary.

    Returns:
    dict: The updated previous header.
    """
    text_whole = current_object[-1]['text_whole']
    doc_structure = current_object[-1]['doc_structure']

    line = " ".join([item_['line'] for item_ in current_object]).strip()
    page_number = remove_duplicates([item_['page_number'] for item_ in current_object])

    dict_object = {
        'type': type,
        'title': line,
        'page_number': page_number,
        'id': str(uuid.uuid4()),
        'content': [],
        'parent_id': doc_structure['id'],
    }

    if type == "header":
        previous_header = handle_header_object(content_list, previous_header, text_whole, doc_structure, dict_object)
    else:
        handle_non_header_object(content_list, dict_object)

    content_list.append(dict_object)

    for item in content_list:
        if item.get('sections'):
            del item['sections']

    return previous_header
