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
    # Convertir las cadenas JSON-like a estructuras Python
    dataframe[column_name] = dataframe[column_name].dropna().apply(convert_to_json)
    
    # Explode: Expande listas en múltiples filas
    exploded = dataframe[column_name].explode().dropna()
    
    # Normalizar diccionarios si están presentes
    desanidado = json_normalize(exploded)
    
    return desanidado


# Procesar columnas categóricas que contienen listas o estructuras complejas
def preprocess_column(column):
    if df[column].dtype == 'object' and df[column].apply(lambda x: isinstance(x, list)).any():
        # Si la columna contiene listas, expandirlas
        return df[column].explode().dropna().nunique()
    else:
        # Si no, calcular directamente la cardinalidad
        return df[column].nunique()
