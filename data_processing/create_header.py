from .add_header_to_list import add_header_to_list

def create_header(content_list, current_header, line_info, previous_header):
    """
    Create a new header based on the provided parameters.

    Parameters:
    content_list (list): The list of contents.
    current_header (list): The list of items in the current header.
    line_info (dict): The line dictionary with detailed information.
    previous_header (dict): The previous header dictionary.

    Returns:
    tuple: A tuple containing the updated current_header, and previous_header.
    """
    if current_header:
            previous_header = add_header_to_list(content_list, current_header, previous_header)
    current_header = [line_info]

    return current_header, previous_header
