# data_cleaning.py

import ast

def extract_names(json_string, key='name'):
    """
    Extract names from a JSON-like string containing a list of dictionaries.
    
    Args:
        json_string (str): JSON-like string to parse.
        key (str): The key whose values will be extracted.
    
    Returns:
        str: Comma-separated names or None if parsing fails.
    """
    try:
        return ", ".join([item[key] for item in ast.literal_eval(json_string)])
    except (ValueError, KeyError, TypeError):
        return None
