from .get_text_before_after_match import get_text_before_after_match
from .create_new_content import create_new_content
from .handle_page_difference import handle_page_difference


def handle_unmatched_header(content_list, previous_header, text_whole, dictionary, doc_structure, match):
    """
    This function handles the case where a header is not matched with the previous content.
    Instead, the header is matched with the whole text.
    match is a match object from the re library. It is None if no match is found.
    """

    if match is not None:
        remaining_text, remaining_text2 = get_text_before_after_match(match, text_whole)

        dictionary['content'] = [create_new_content(remaining_text, dictionary['page_number'][0], previous_id=None, parent_id=dictionary['id'])]

        if type(previous_header['page_number']) is list and previous_header['page_number'] != dictionary['page_number']:
            handle_page_difference(content_list, previous_header, dictionary, doc_structure, remaining_text2)
