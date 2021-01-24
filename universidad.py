import pandas as pd
import numpy as np
import random
import datetime
from datetime import date

db_size = 3658

trayectoria_col = ['llave_plan_estudios', 'llave_facultad', 'llave_estudiante', 'estatus_estudiante', 'creditos', 'fecha_titulacion']

generacion = [
	'06-08-2010',
	'04-08-2011',
	'07-08-2012',
	'03-08-2013',
	'08-08-2014',
	'05-08-2015',
	'03-08-2016',
	'04-08-2017',
	'03-08-2018',
	'03-08-2019',
	'21-09-2020'
	]

llave_plan_estudios = np.random.randint(1, 36, size = db_size + 1)


def get_facultad(plan_estudios_id):
	if plan_estudios_id <= 2:
		return 1
	elif plan_estudios_id <= 4:
		return 2 
	elif plan_estudios_id <= 10:
		return 3
	elif plan_estudios_id <= 12:
		return 4
	elif plan_estudios_id <= 14:
		return 5
	elif plan_estudios_id <= 18:
		return 6
	elif plan_estudios_id <= 19:
		return 7
	elif plan_estudios_id <= 21:
		return 8 
	elif plan_estudios_id == 22:
		return 9
	elif plan_estudios_id <= 28:
		return 10
	elif plan_estudios_id <= 30:
		return 11
	elif plan_estudios_id == 31:
		return 14
	elif plan_estudios_id <= 33:
		return 12
	elif plan_estudios_id <= 35:
		return 13
	

def get_date(d, years):
	try:
		return d.replace(year = d.year + years)
	except:
		return d + (date(d.year + years, 1, 1) - date(d.year, 1, 1))


llave_estudiante = np.arange(db_size)

estatus_list = ['Cursando', 'Baja', 'Créditos completos', 'Titulado']
estatus_estudiante = random.choices(estatus_list, weights = (40, 5, 25, 30), k = db_size)
	
llave_facultad = []
creditos = []
fecha_titulacion = []
fecha_titulacion = []
plan_df = pd.read_csv('data/plan_estudios.csv')
# print(plan_df.head())
estudiante_df = pd.read_csv('data/estudiante.csv')
for i in range(db_size + 1):
	llave_facultad.append(get_facultad(llave_plan_estudios[i]))
	
	estudiante = estatus_estudiante[i]
	print(estudiante_df.iloc[i, -1])
	creditos_gen = plan_df.iloc[estudiante_df.iloc[i, -1], 2]
	if estudiante == 'Cursando' or estudiante == 'Baja':
		creditos.append(random.randint(0, creditos_gen))
	else:
		creditos.append(creditos_gen)
	años_titulo = plan_df[plan_df.llave_plan_estudios == llave_plan_estudios[i]].duracion_titulo
	fecha_ingreso = generacion[estudiante_df.iloc[i + 1, -1] - 1]
	# fecha_titulacion.append(get_date(datetime.date(fecha_ingreso), años_titulo[0]))


trayectoria = pd.DataFrame([llave_plan_estudios, llave_facultad, llave_estudiante, estatus_estudiante, creditos, fecha_titulacion], columns = trayectoria_col)
trayectoria.to_csv('data/trayectoria.csv')
