from pandas import json_normalize

# Función para convertir texto a objetos Python
def convert_to_json(data):
    try:
        return ast.literal_eval(data)
    except (ValueError, SyntaxError):
        return None

# Función para desanidar columnas
def desanidar_columna(dataframe, column_name):
    """
    Convierte cadenas JSON-like, explota listas y normaliza diccionarios en una columna específica.
    """
    dataframe[column_name] = dataframe[column_name].dropna().apply(convert_to_json)
    
    exploded = dataframe[column_name].explode().dropna()
    
    desanidado = json_normalize(exploded)
    
    return desanidado

# Procesar la columna 'genres' para extraer los nombres de los géneros
def extract_genre_names(genres):
    try:
        # Convertir el texto a lista de diccionarios
        genres_list = ast.literal_eval(genres)
        # Extraer solo los nombres
        return [genre['name'] for genre in genres_list]
    except (ValueError, TypeError):
        return []
    
# Procesar columnas categóricas que contienen listas o estructuras complejas
def preprocess_column(column):
    if df[column].dtype == 'object' and df[column].apply(lambda x: isinstance(x, list)).any():
        # Si la columna contiene listas, expandirlas
        return df[column].explode().dropna().nunique()
    else:
        # Si no, calcular directamente la cardinalidad
        return df[column].nunique()

# Función para procesar y validar las etiquetas
def process_tags(tag_string):
    try:
        # Intentar evaluar el string como una lista
        return [tag['name'] for tag in ast.literal_eval(tag_string)] if pd.notnull(tag_string) else []
    except (ValueError, SyntaxError, TypeError):
        # Retornar una lista vacía si falla
        return []