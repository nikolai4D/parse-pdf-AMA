import re

def match_header_with_text(header, previous_content):
    """
    Match a header with the text from previous content under previous header (string).
    This is so that we can split the previous content into two parts: before and after the match.
    Then we can add the remaining text to the current header and the before text to the previous header.
    """
    header_regex = re.compile(r'\s*'.join(re.escape(word) for word in header.split()))
    match = header_regex.search(previous_content)
    return match


