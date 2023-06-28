from .get_previous_content import get_previous_content
from .match_header_with_text import match_header_with_text
from .handle_matched_header import handle_matched_header
from .handle_unmatched_header import handle_unmatched_header


def add_content_to_header(content_list, previous_header, text_whole, dictionary, doc_structure):
    """
    Update the content of a header in the content list.

    Parameters:
    content_list (list): The list of contents.
    previous_header (dict): The previous header dictionary.
    text_whole (str): The whole text.
    dictionary (dict): The dictionary that will be added to the content list.
    doc_structure (dict): The document structure dictionary.

    Returns:
    dict: The updated previous header.
    """

    header= dictionary['title']
    previous_header, previous_content = get_previous_content(previous_header)

    match = match_header_with_text(header, previous_content)
    if match is not None:
        handle_matched_header(content_list, previous_header, dictionary, previous_content, match)
    else:
        match = match_header_with_text(header, text_whole)
        handle_unmatched_header(content_list, previous_header, text_whole, dictionary, doc_structure, match)

    previous_header = dictionary
    return previous_header