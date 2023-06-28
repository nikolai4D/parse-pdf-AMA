def to_int_or_none(s):
    """Attempt to convert a string to an integer, returning None if it fails."""
    try:
        return int(s)
    except ValueError:
        return None