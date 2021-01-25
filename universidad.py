import pandas as pd
import numpy as np
import random
import datetime
from datetime import date
<<<<<<< HEAD
from random import choice, randint
=======

trayectoria_col = ['llave_plan_estudios', 'llave_facultad', 'llave_estudiante', 
	'estatus_estudiante', 'creditos', 'fecha_titulacion'
]

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
>>>>>>> 67804e8bdc1c753d780ad69b3281f92eda71c7c3

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
	elif plan_estudios_id == 32:
		return 12
	elif plan_estudios_id <= 34:
		return 13

trayectoria_col = ['llave_plan_estudios', 'llave_facultad', 'llave_estudiante', 
	'estatus_estudiante', 'creditos', 'fecha_titulacion'
]
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

def get_date(d, years):
	try:
		return d.replace(year = d.year + years)
	except:
		return d + (date(d.year + years, 1, 1) - date(d.year, 1, 1))

estudiante_df = pd.read_csv('data/estudiante.csv')
db_size = estudiante_df.shape[0]
<<<<<<< HEAD
=======

>>>>>>> 67804e8bdc1c753d780ad69b3281f92eda71c7c3
llave_estudiante = np.arange(db_size)
estatus_list = ['Cursando', 'Baja', 'Créditos completos', 'Titulado']
estatus_estudiante = random.choices(estatus_list, weights = (40, 5, 25, 30), k = db_size)
<<<<<<< HEAD
llave_plan_estudios = np.random.randint(0, 33 + 1, size = db_size + 1)
=======
llave_plan_estudios = np.random.randint(0, 34 + 1, size = db_size + 1)
>>>>>>> 67804e8bdc1c753d780ad69b3281f92eda71c7c3
llave_facultad = []
creditos = []
fecha_titulacion = []
fecha_titulacion = []
plan_df = pd.read_csv('data/plan_estudios.csv')
<<<<<<< HEAD
max_llave_plan = plan_df.llave_plan_estudios.max()
min_llave_plan = plan_df.llave_plan_estudios.min()
generacion_df = pd.read_csv('data/generacion.csv')

def descomprimir_fecha(fecha): # str => int, int, int
	dia, mes, anio = fecha.split("-")
	return int(dia), int(mes), int(anio)

def comprimir_fecha(dia, mes, anio):
	return datetime.date(dia, mes, anio)

def obtener_registro(llave_estudiante):
	llave_plan_estudios = randint(min_llave_plan, max_llave_plan)
	llave_facultad = get_facultad(llave_plan_estudios)# 
	status_estudiante = choice(estatus_list)
	creditos = plan_df.iloc[llave_plan_estudios - 1, 2] # Max creditos
	llave_generacion = estudiante_df.iloc[llave_estudiante, -1]
	fecha_titulacion = None
	if status_estudiante in ('Cursando', 'Baja'):
		creditos = randint(0, creditos)
	else:
		duracion_titulo = plan_df.iloc[llave_plan_estudios - 1, -2] #en semestres
		fecha_ingreso = generacion_df.iloc[llave_generacion - 1, -1]
		dia, mes, anio = descomprimir_fecha(fecha_ingreso)
		duracion_anio = duracion_titulo // 2 
		aditivo = random.choices([0, 1, 2, 3], weights = [60, 20, 15, 5], k = 1)[0]
		fecha_minima = comprimir_fecha(anio, mes, dia)
		fecha_titulacion = get_date(fecha_minima, duracion_anio + aditivo)
	return (llave_plan_estudios, llave_facultad, llave_estudiante, 
		status_estudiante, creditos, fecha_titulacion)
	
# for i in range(db_size):
# 	llave_facultad.append(get_facultad(llave_plan_estudios[i]))
# 	estudiante = estatus_estudiante[i]
# 	creditos_plan = plan_df.iloc[llave_plan_estudios[i]-1, 2]
# 	fecha_ingreso = generacion[estudiante_df.iloc[i, -1] - 1]
# 	dia, mes, anio = fecha_ingreso.split("-")
# 	dia, mes, anio = int(dia), int(mes), int(anio)
# 	anos_titulo = plan_df.iloc[max(llave_plan_estudios[i] - 1, 0), 3]
# 	if estudiante == 'Cursando' or estudiante == 'Baja':
# 		creditos.append(random.randint(0, creditos_plan))
# 		# fecha_titulacion.append(get_date(datetime.date(anio, mes, dia), anos_titulo // 2))
# 		fecha_titulacion.append(None)
# 	else:
# 		creditos.append(creditos_plan)
# 		fecha_titulacion.append()
alumnos = [obtener_registro(i) for i in range(db_size)]
trayectoria = pd.DataFrame(alumnos, columns = trayectoria_col)
=======

for i in range(db_size):
	llave_facultad.append(get_facultad(llave_plan_estudios[i]))
	estudiante = estatus_estudiante[i]
	creditos_plan = plan_df.iloc[llave_plan_estudios[i], 2]
	fecha_ingreso = generacion[estudiante_df.iloc[i, -1] - 1]
	dia, mes, anio = fecha_ingreso.split("-")
	dia, mes, anio = int(dia), int(mes), int(anio)
	anos_titulo = plan_df.iloc[max(llave_plan_estudios[i] - 1, 0), 3]
	if estudiante == 'Cursando' or estudiante == 'Baja':
		creditos.append(random.randint(0, creditos_plan))
		# fecha_titulacion.append(get_date(datetime.date(anio, mes, dia), anos_titulo // 2))
		fecha_titulacion.append(None)
	else:
		creditos.append(creditos_plan)
		fecha_titulacion.append(get_date(datetime.date(anio, mes, dia), anos_titulo // 2 + random.choices([-2, -1, 0, 1, 2, 3], 
			weights = [1, 3, 60, 19, 12, 5], k = 1)[0]))
	
	

trayectoria = pd.DataFrame(zip(llave_plan_estudios + 1 , llave_facultad, llave_estudiante, estatus_estudiante, creditos, fecha_titulacion), columns = trayectoria_col)
>>>>>>> 67804e8bdc1c753d780ad69b3281f92eda71c7c3
trayectoria.to_csv('data/trayectoria.csv', index=False)
