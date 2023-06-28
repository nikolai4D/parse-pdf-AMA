from .add_object_to_content_list import add_object_to_content_list

def add_header_to_list(content_list, current_header, previous_header):
    """
    Add a header to the content list and return the updated previous header.

    Parameters:
    content_list (list): The list of contents.
    current_header (list): The list of items in the current header.
    previous_header (dict): The previous header dictionary.

    Returns:
    dict: The updated previous header.
    """
    previous_header = add_object_to_content_list('header', content_list, current_header, previous_header)

    return previous_header
