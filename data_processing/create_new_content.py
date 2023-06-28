import uuid

def create_new_content(text, page_number, previous_id, parent_id):
    """Creates a new content object."""

    return {
        'title': text,
        "type": "content",
        'page_number': page_number,
        'id': str(uuid.uuid4()),
        'previous_id': previous_id,
        'parent_id': parent_id
    }
