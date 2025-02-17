import pandas as pd

class DataFrameHelper:
    def __init__(self, df: pd.DataFrame):
        """
        Clase para manejar y explorar DataFrames de Pandas.
        :param df: DataFrame de Pandas
        """
        self.df = df
    
    def info(self):
        """Muestra la información general del DataFrame."""
        return self.df.info()
    
    def head(self, n=5):
        """Devuelve las primeras n filas del DataFrame."""
        return self.df.head(n)
    
    def tail(self, n=5):
        """Devuelve las últimas n filas del DataFrame."""
        return self.df.tail(n)
    
    def summary(self):
        """Muestra estadísticas descriptivas de las columnas numéricas."""
        return self.df.describe()
    
    def missing_values(self):
        """Devuelve el conteo de valores nulos por columna."""
        return self.df.isnull().sum()
    
    def unique_values(self, column):
        """Devuelve los valores únicos de una columna específica."""
        if column in self.df.columns:
            return self.df[column].unique()
        else:
            return f"La columna '{column}' no existe en el DataFrame."
    
    def shape(self):
        """Devuelve el número de filas y columnas del DataFrame."""
        return self.df.shape