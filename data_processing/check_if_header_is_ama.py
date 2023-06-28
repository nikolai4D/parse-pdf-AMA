import re

def check_if_header_is_ama(line):
    """
    Check if the provided line matches a specified pattern (AMA) and has an uppercase character following the match.

    Parameters:
    line (str): The line of text to check.

    Returns:
    bool: True if the line matches the pattern and has an uppercase character following the match, False otherwise.
    """
    pattern = r'^((\d{1,3}\.[A-Z]{1,3}/\d+)|([A-Z]{1,3}\.\d+)|(\d{1,3}\.[A-Z]+)|[A-Z]{1,3}|\d{1,3})\s'
    is_header = False
    matches = re.match(pattern, line)

    if matches:
        ama_code = matches.group()
        rest_of_text = line[len(ama_code):]

        if rest_of_text[0].isupper():
            is_header = True

    return is_header
