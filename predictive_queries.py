"""
Barrero Olguín Patricio
Martínez Ostoa Néstor
Ramírez Bondi Alejandro

Consultas predictivas:
1. Numero de estudiantes que estudiarán en primer ingreso Ing. Civil en 2025 en 
    la FI
2. Numero de estudiantes que abandonarán el semestre en 2021
3. Número de estudiantes que se titularan en 2025
4. ¿De qué tamaño será la generación 2026?
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import TimeSeriesSplit

################################################################################
# Datasets

trayectoria_df = pd.read_csv('data/trayectoria.csv')
estudiante_df = pd.read_csv('data/estudiante.csv')
facultad_df = pd.read_csv('data/facultad.csv')
plan_estudios_df = pd.read_csv('data/plan_estudios.csv')
generacion_df = pd.read_csv('data/generacion.csv')
titulo_df = pd.read_csv('data/titulo.csv')
categoria_df = pd.read_csv('data/categoria.csv')
creditos_df = pd.read_csv('data/creditos_titulo.csv')
duracion_df = pd.read_csv('data/duracion_titulo.csv')

def timeseries_train_split(X, y, test_size):
    test_index = int(len(X) * (1 - test_size))
    X_train = X.iloc[:test_index]
    y_train = y.iloc[:test_index]
    X_test = X.iloc[test_index:]
    y_test = y.iloc[test_index:]
    return X_train, X_test, y_train, y_test

################################################################################
# 1 (anio, fecha, titulo) => num_estudiantes  [regresion]
generacion_estudiante = pd.merge(generacion_df, estudiante_df, how="inner", on=["llave_generacion"])
hecho_estudiante = pd.merge(generacion_estudiante, trayectoria_df, how="inner", on=["llave_estudiante"])
print(plan_estudios_df)
hecho_plan = pd.merge(generacion_estudiante, plan_estudios_df, how="inner", on=["llave_plan_estudios"])

print(hecho_estudiante)


################################################################################
# 2 (anio) => num_estudiantes_baja [regresion]



################################################################################
# 3 (anio) => num_estudiantes_titulado [regresion]



################################################################################
# 4 
