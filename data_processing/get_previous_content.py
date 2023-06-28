from .create_new_content import create_new_content

def get_previous_content(previous_header):
    """Returns the previous content and header."""
    previous_content = ""

    if previous_header is None or previous_header.get('content') is None or previous_header['content'] == []:
        previous_header = {'content':[create_new_content("", 0, previous_id=None, parent_id=None)], 'page_number': 0}
    else:
        previous_content = previous_header['content'][0]['title']
    return previous_header,previous_content
