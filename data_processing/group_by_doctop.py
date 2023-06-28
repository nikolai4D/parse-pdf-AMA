def group_by_doctop(text):
    """Group the text by the rounded 'doctop' value."""
    grouped = {}
    for item in text:
        key = round(item["doctop"])
        grouped.setdefault(key, []).append(item)
    return grouped