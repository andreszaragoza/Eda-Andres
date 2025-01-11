import ast
import pandas as pd
from collections import Counter

def convert_to_json(data):
    try:
        return ast.literal_eval(data)
    except (ValueError, SyntaxError):
        return None

def unnest_column(df, column_name):
    """
    Convierte cadenas JSON-like, explota listas y normaliza diccionarios en una columna específica.
    """
    df[column_name] = df[column_name].dropna().apply(convert_to_json)

    exploded = df[column_name].explode().dropna()

    unnested_column = pd.json_normalize(exploded) 

    return unnested_column


def extract_genre_names(genres):
    """
    Extraer el nombre de cada género
    """
    try:
        genres_list = ast.literal_eval(genres)
        return [genre['name'] for genre in genres_list]
    except (ValueError, TypeError):
        return []


def preprocess_column(df, column_name):
    """
    
    """
    if df[column_name].dtype == 'object' and df[column_name].apply(lambda x: isinstance(x, list)).any():
        return df[column_name].explode().dropna().nunique()
    else:
        return df[column_name].nunique()


def extract_tag_names(tag_string):
    """
    Extraer el nombre de cada etiqueta
    """
    try:
        if pd.notnull(tag_string):
            return [tag['name'] for tag in ast.literal_eval(tag_string)]
        else:
            return []
    except (ValueError, SyntaxError, TypeError):
        return []
    
def extract_store_names(stores):
    try:
        stores = ast.literal_eval(stores)
        return [store['store']['name'] for store in stores]
    except Exception:
        return []
    
'''manejo de metacritic'''
def extract_main_genre(genre_str): 
    try:
        genres_list = ast.literal_eval(genre_str)
        if isinstance(genres_list, list) and len(genres_list) > 0:
            return genres_list[0].get('name', 'Unknown')
        return 'Unknown'
    except (ValueError, SyntaxError):
        return 'Unknown'
    
