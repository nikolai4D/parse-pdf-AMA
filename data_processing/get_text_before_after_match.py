def get_text_before_after_match(match, text):
    """
    Get the text before and after the match.
    """
    # Obtain start and end position of the match in the previous_content string
    match_start = match.start()
    match_end = match.end()

    # Split the previous_content string into two parts: before and after the match
    remaining_text = text[match_end:]
    before_text = text[:match_start]
    return remaining_text, before_text
