def flatten_json(data):
    """
    Flatten json structure to a list of rows.
    This structure is easier to write to a csv file.
    """
    flat_data = []
    for doc in data["docs"]:
        file_name = doc["file_name"]
        for section in doc.get('sections', []):
            # Adding section as a row in the csv
            flat_data.append({
                "id": section.get('id'),
                "file_name": file_name,
                "page_number": ','.join(map(str, section.get('page_number', []))),
                "type": section.get('type'),
                "text": section.get('title'),
                "parent_id": section.get('parent_id'),
                "previous_id": section.get('previous_id'),
            })
            for content in section.get('content', []):
                # Adding content as a row in the csv
                if content.get('title').strip():

                    flat_data.append({
                        "id": content.get('id'),
                        "file_name": file_name,
                        "page_number": content.get('page_number'),
                        "type": content.get('type'),
                        "text": content.get('title'),
                        "parent_id": content.get('parent_id'),
                        "previous_id": content.get('previous_id'),
                    })
    return flat_data
