"""
Barrero Olguín Patricio
Martínez Ostoa Néstor
Ramírez Bondi Alejandro

Consultas predictivas:
1. Numero de estudiantes que estudiarán en primer ingreso Ing. Civil en 2025 en 
    la FI
2. Número de estudiantes que se titularán en 2029.
3. ¿De qué tamaño será la generación 2026?
4. Número de estudiantes que completarán créditos en 2023
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import TimeSeriesSplit
from sklearn.preprocessing import StandardScaler 
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
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
# 1 (anio, facultad, titulo) => num_estudiantes  [regresion]
generacion_estudiante = pd.merge(generacion_df, estudiante_df, how="inner", on=["llave_generacion"])
hecho_estudiante = pd.merge(generacion_estudiante, trayectoria_df, how="inner", on=["llave_estudiante"])
hecho_plan = pd.merge(hecho_estudiante, plan_estudios_df, how="inner", on=["llave_plan_estudios"])
plan_titulo = pd.merge(hecho_plan, titulo_df, how="inner", on=["llave_titulo"])
plan_facultad = pd.merge(plan_titulo, facultad_df, how="inner", on=["llave_facultad"])
plan_facultad['suma'] = 1

df = plan_facultad.groupby(by=["fecha_ingreso", "llave_titulo", "llave_facultad"]).suma.sum().reset_index()
df.fecha_ingreso = df.fecha_ingreso.apply(lambda x: int(x[-4:]))

X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, y)
pipe = Pipeline([("scaler", StandardScaler()), ("linear", LinearRegression())])
pipe.fit(X_train, y_train)
print("Modelo 1: Predice numero de estudiantes que entraran en una carrera, facultad, y anios especificos")
print("Error cuadratico medio:", mean_squared_error(pipe.predict(X_test), y_test))
anio = 2030
titulo = 11 # Derecho
facultad = 4
x = StandardScaler().fit_transform([(anio, titulo, facultad)])
print("La carrera de derecho de la facultad derecho en el anio 2021 tendra %d estudiantes" % pipe.predict(x))

################################################################################
# 2 (anio) => num_estudiantes_titulado [regresion]
titulados = trayectoria_df[trayectoria_df.estatus_estudiante == 'Titulado']
titulados = titulados.astype({'fecha_titulacion':'str'})
split = titulados['fecha_titulacion'].str.split('-', expand=True)
titulados.drop(columns=['fecha_titulacion'], inplace=True)
titulados['year'] = split[0]
titulados['month'] = split[1]
titulados['day'] = split[2]

def build_XY(titulados):
    min_year = int(titulados.year.min())
    max_year = int(titulados.year.max())
    X, y = [], []
    for year in range(min_year, max_year + 1):
        X.append(year)
        num_titulados = titulados[titulados.year == str(year)].shape[0]
        y.append(num_titulados)
    return np.array(X), np.array(y)
X, y = build_XY(titulados)
X_train = X[:].reshape(-1,1)
y_train = y[:]
plt.plot(X_train, y_train)
plt.show()
reg = LinearRegression().fit(X_train, y_train)
X_test = np.array([[2029]])
reg.predict(X_test)

################################################################################
# 3
generaciones_df = estudiante_df['llave_generacion'].value_counts().to_frame()
generaciones_df.reset_index(inplace=True)
generaciones_df = generaciones_df.rename(columns = {'llave_generacion': 'integrantes_generacion', 'index': 'llave_generacion'})
print(generaciones_df)

y = generaciones_df['integrantes_generacion'].values
x = generaciones_df['llave_generacion'].values

lr = LinearRegression()
lr.fit(x.reshape(-1, 1), y.reshape(-1, 1))

prediction = lr.predict(np.array(16).reshape(-1, 1))
print('Predicción de ingreso para el 2026: ', prediction)


################################################################################
# 4

titulados = trayectoria_df[trayectoria_df.estatus_estudiante == 'Titulado']
titulados = titulados.astype({'fecha_titulacion':'str'})
split = titulados['fecha_titulacion'].str.split('-', expand=True)
titulados.drop(columns=['fecha_titulacion'], inplace=True)
titulados['year'] = split[0]
titulados['month'] = split[1]
titulados['day'] = split[2]

def build_XY(titulados):
    min_year = int(titulados.year.min())
    max_year = int(titulados.year.max())
    X, y = [], []
    for year in range(min_year, max_year + 1):
        X.append(year)
        num_titulados = titulados[titulados.year == str(year)].shape[0]
        y.append(num_titulados)
    return np.array(X), np.array(y)
X, y = build_XY(titulados)
X_train = X[:].reshape(-1,1)
y_train = y[:]
plt.plot(X_train, y_train)
plt.show()
reg = LinearRegression().fit(X_train, y_train)
X_test = np.array([[2029]])
reg.predict(X_test)
