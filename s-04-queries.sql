--@Autores:               Barrero Olguín Patricio
--                        Martínez Ostoa Néstor
--                        Ramírez Bondi Alejandro
--@Fecha de creación:     24/01/2021
--@Descripción:           Queries

/* 
                         REQUERIMIENTOS UNIVERSIDAD

Una Universidad desea analizar los tiempos de titulación de los estudiantes 
hombres y mujeres a lo largo de las diferentes facultades. Cada facultad tiene 
diversas carreras, dependiendo de cada carrera es la duración en años de ésta, 
también tiene las fechas de ingreso de sus estudiantes por carrera, su género y 
la fecha de titulación. 
    1) Se desea saber el tiempo promedio de titulación de todos  los estudiantes
      y después realizar el detalle por facultad y carrera. 
    
    
    
    2)Por otro lado, también se desea saber cuantos estudiantes están terminando 
    su carrera para mandarles recordatorio y asesoría sobre las formas de titulación.


    
    3) La  Universidad necesita saber la eficiencia terminal, es decir dada una 
    fecha  dada obtener por facultad y carrera cuantos estudiantes ya terminaron 
    y cuantos de esos ya se titularon.
*/

-- 1) Se desea saber el tiempo promedio de titulación de todos  los estudiantes
--       y después realizar el detalle por facultad y carrera. 

SELECT
    nombre_facultad,
	nombre_titulo,
	nombre_estudiante,
	AVG(
		(fecha_titulacion - fecha_ingreso) / (6*30)
	)::NUMERIC(5,2) AS tiempo_promedio
FROM
	trayectoria
	INNER JOIN estudiante e USING (llave_estudiante)
	INNER JOIN generacion g USING (llave_generacion)
	INNER JOIN facultad f USING (llave_facultad)
	INNER JOIN plan_estudios pe USING (llave_plan_estudios)
	INNER JOIN titulo t USING (llave_titulo)
WHERE
	estatus_estudiante = 'Titulado'
GROUP BY
	ROLLUP(
		nombre_facultad, nombre_titulo, nombre_estudiante
	);

-- 2)Por otro lado, también se desea saber cuantos estudiantes están terminando 
--     su carrera para mandarles recordatorio y asesoría sobre las formas de titulación.

SELECT
    nombre_tipo_escuela,
	nombre_facultad,
	nombre_estudiante,
	COUNT(*)
FROM
	trayectoria
	JOIN estudiante ON trayectoria.llave_estudiante = estudiante.llave_estudiante
	JOIN plan_estudios ON trayectoria.llave_plan_estudios = plan_estudios.llave_plan_estudios
	JOIN facultad ON trayectoria.llave_facultad = facultad.llave_facultad
	JOIN tipo_escuela ON tipo_escuela.llave_tipo_escuela = facultad.llave_tipo_escuela
WHERE
	ABS(creditos_titulos - creditos) <= 40
	AND estatus_estudiante != 'Baja'
GROUP BY
	ROLLUP (
		nombre_tipo_escuela, nombre_facultad,
		nombre_estudiante
	);

-- 3) La  Universidad necesita saber la eficiencia terminal, es decir dada una 
--     fecha obtener por facultad y carrera cuantos estudiantes ya terminaron 
--     y cuantos de esos ya se titularon.

SELECT
    nombre_facultad,
	nombre_titulo,
	COUNT(trayectoria.estatus_estudiante) FILTER (
		WHERE
			estatus_estudiante = 'Créditos completos'
	) AS Creditos_completados,
	COUNT(trayectoria.estatus_estudiante) FILTER (
		WHERE
			estatus_estudiante = 'Titulado'
	) AS Titulados,
	(CAST(
		COUNT(trayectoria.estatus_estudiante) FILTER (
			WHERE
				estatus_estudiante = 'Titulado'
		) AS FLOAT
	) / CAST(
		COUNT(trayectoria.estatus_estudiante) FILTER (
			WHERE
				estatus_estudiante = 'Créditos completos'
		) AS FLOAT
	))::Numeric(6, 3) AS eficiencia
FROM
	trayectoria
	INNER JOIN facultad USING (llave_facultad)
	INNER JOIN estudiante USING (llave_estudiante)
	INNER JOIN plan_estudios USING (llave_plan_estudios)
	INNER JOIN titulo USING (llave_titulo)
WHERE
	DATE(fecha_titulacion) <= '2020-09-11'
GROUP BY
	ROLLUP (nombre_facultad, nombre_titulo)
ORDER BY
	nombre_facultad,
	nombre_titulo DESC;

-- 
-- CONSULTAS DICING
--

--
-- 4) Número de alumnos cursando la licenciatura en Economia que hayan
-- ingresado en 2020
--
SELECT Ca.nombre_categoria, Ti.nombre_titulo, Ge.fecha_ingreso, count(*) AS alumnos
FROM trayectoria Ta
JOIN estudiante E ON E.llave_estudiante = Ta.llave_estudiante
JOIN generacion Ge ON Ge.llave_generacion = E.llave_generacion
JOIN plan_estudios Pe ON Pe.llave_plan_estudios = Ta.llave_plan_estudios
JOIN titulo Ti ON Pe.llave_titulo = Ti.llave_titulo
JOIN categoria Ca ON Ca.llave_categoria = Ti.llave_categoria
WHERE Ti.nombre_titulo = 'Economia' AND Ca.nombre_categoria = 'Licenciatura' AND
    DATE_PART('year', Ge.fecha_ingreso) = '2020'
GROUP BY (Ca.nombre_categoria, Ti.nombre_titulo, Ge.fecha_ingreso);

--
-- 5) Obtener los nombres de los estudiantes en la escuela de salud, el grado de 
-- licenciatura y que hayan ingresado en la generación 2016
--
SELECT Est.nombre_estudiante, Am.apellido_materno,TiEs.nombre_tipo_escuela, 
	Ca.nombre_categoria, Ti.nombre_titulo, Ge.fecha_ingreso
FROM trayectoria Ta
JOIN estudiante Est ON Est.llave_estudiante = Ta.llave_estudiante
JOIN apellido_materno Am on Am.apellido_materno = Est.apellido_materno
JOIN generacion Ge ON Ge.llave_generacion = Est.llave_generacion
JOIN facultad Fa ON Fa.llave_facultad = Ta.llave_facultad
JOIN tipo_escuela TiEs ON TiEs.llave_tipo_escuela = Fa.llave_tipo_escuela
JOIN plan_estudios Pe ON Pe.llave_plan_estudios = Ta.llave_plan_estudios
JOIN titulo Ti ON Ti.llave_titulo = Pe.llave_titulo
JOIN categoria Ca ON Ca.llave_categoria = Ti.llave_categoria
WHERE TiEs.nombre_tipo_escuela = 'Escuela de la Salud' AND 
	Ca.nombre_categoria = 'Licenciatura' AND  
	DATE_PART('year', Ge.fecha_ingreso) = '2016';

-- 
-- 6) CONSULTAS DRILL DOWN
-- ¿Cuántas facultades hay en la escuela de “medicina”?

SELECT
	COUNT(*)
FROM
	facultad
	JOIN tipo_escuela 
    ON facultad.llave_tipo_escuela = tipo_escuela.llave_tipo_escuela
WHERE
	nombre_tipo_escuela = 'Escuela de Leyes';

-- 7) ¿Cuántas facultades hay en el campus principal?
SELECT
    COUNT(*) AS número_facultades_campus
FROM
	campus
	JOIN tipo_escuela ON campus.llave_campus = tipo_escuela.llave_campus
	JOIN facultad ON tipo_escuela.llave_tipo_escuela = facultad.llave_tipo_escuela
WHERE
	nombre_campus = 'Ciudad Universitaria';

-- 
-- CONSULTAS DRILL UP: conocer el acumulado a nivel superior

-- 8) Conocer el número de estudiantes que están terminando su carrera por 
-- facultad y tipo de escuela.

SELECT
    nombre_tipo_escuela,
    nombre_facultad,
    nombre_estudiante,
	COUNT(*)
FROM
	trayectoria
	JOIN estudiante ON trayectoria.llave_estudiante = estudiante.llave_estudiante
	JOIN plan_estudios ON trayectoria.llave_plan_estudios = plan_estudios.llave_plan_estudios
	JOIN facultad ON trayectoria.llave_facultad = facultad.llave_facultad
	join tipo_escuela on tipo_escuela.llave_tipo_escuela = facultad.llave_tipo_escuela
WHERE
	abs(creditos_titulos - creditos) <= 40
	AND estatus_estudiante != 'Baja'
GROUP BY
	rollup (nombre_tipo_escuela, nombre_facultad, nombre_estudiante );

-- Drill down
-- 9) Conocer los estudiantes que están terminando su carrera para 
-- enviarles un recordatorio.

SELECT
    trayectoria.llave_estudiante,
	apellido_paterno,
	apellido_materno,
	nombre_estudiante,
	(creditos_titulos - creditos) AS creditos_faltantes
FROM
	trayectoria
	JOIN estudiante ON trayectoria.llave_estudiante = estudiante.llave_estudiante
	JOIN plan_estudios ON trayectoria.llave_plan_estudios = plan_estudios.llave_plan_estudios
WHERE
	(creditos_titulos - creditos) <= 40
	AND (creditos_titulos - creditos) > 0
	AND estatus_estudiante != 'Baja';

-- - 10) El alumno con la clave ‘1405’, ¿a qué generacion pertenece?

SELECT llave_generacion, fecha_ingreso
FROM generacion
INNER JOIN estudiante
USING (llave_generacion)
WHERE llave_estudiante = 1405;

-- - 11) ¿A cual categoría posee el programa <Odontologia>?

SELECT llave_categoria, nombre_categoria
FROM titulo
INNER JOIN categoria
USING (llave_categoria)
WHERE nombre_titulo = 'Odontologia';


SELECT llave_generacion, fecha_ingreso
FROM generacion
INNER JOIN estudiante
USING (llave_generacion)
WHERE llave_estudiante = 1405;

-- - 11) ¿A cual categoría pertenece el programa <Odontologia>?

SELECT llave_categoria, nombre_categoria
FROM titulo
INNER JOIN categoria
USING (llave_categoria)
WHERE nombre_titulo = 'Odontologia';