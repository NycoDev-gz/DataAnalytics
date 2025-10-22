import pandas as pd
import numpy as np

def leerdoc(doc):
    df = pd.read_csv(doc)
    return df

def calcular_promedio(data, columna):
    return data[columna].mean()