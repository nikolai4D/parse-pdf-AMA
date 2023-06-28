def handle_non_header_object(content_list, dict_object):
    """
    Process a non-header object from the content list, assigning the 'parent_id' and 'previous_id' fields
    based on the most recent header object.

    This function iterates in reverse through the content_list until it encounters the most recent header,
    and then assigns that header's id as the 'parent_id' for the current object.
    If the header has sections, the id of the last section is assigned to 'previous_id'.
    If the header has no sections, 'previous_id' is set to None.

    Parameters:
    content_list (list): The list of all extracted content sections from the PDF.
    dict_object (dict): The current non-header dictionary that is being processed.

    Returns:
    None: The function modifies the 'parent_id' and 'previous_id' fields of dict_object in place.
    """

    for dictionary in reversed(content_list):
        if dictionary['type'] == "header":
            dict_object['parent_id'] = dictionary['id']

            if dictionary.get('sections'):
                dict_object['previous_id'] = dictionary['sections'][-1]['id']

            else:
                dict_object['previous_id'] = None

            break