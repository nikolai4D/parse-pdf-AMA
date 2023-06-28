from .get_text_before_after_match import get_text_before_after_match
from .create_new_content import create_new_content

def handle_matched_header(content_list, previous_header, dictionary, previous_content, match):
    """
    Handles the scenario where a header is matched within the text content of a document. 
    The function updates the content of the matched header and the previous header by splitting the previous content at the match point.

    Parameters:
    content_list (list): The list of all content objects from the document.
    previous_header (dict): The dictionary representing the previous header in the document.
    dictionary (dict): The dictionary representing the current header that matched within the text.
    previous_content (str): The text content under the previous header.
    match (re.Match): The regex match object for the matched header within the text.

    Returns:
    None: The function modifies the 'content' fields of the matched header and previous header in place.
    """

    remaining_text, before_text = get_text_before_after_match(match, previous_content)
    dictionary['content']= [create_new_content(remaining_text, dictionary['page_number'][0], previous_id=None, parent_id=dictionary['id'])]
    previous_content = before_text

    for item in content_list:
        if item['id'] == previous_header['id']:
            item['content'] = [create_new_content(before_text, previous_header['page_number'][0], previous_id=None,  parent_id=item['id'])]
