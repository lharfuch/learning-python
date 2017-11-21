def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = first + ' ' + last
    return full_name.title()
    
def get_formatted_full_name(first, middle, last):
    """Generate a neatly formatted full name."""
    full_name = first.strip() + ' ' + middle.strip() + ' ' + last.strip()
    return full_name.title()