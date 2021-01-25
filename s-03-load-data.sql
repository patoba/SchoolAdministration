--@Autores:               Barrero Olguín Patricio
--                        Martínez Ostoa Néstor
--                        Ramírez Bondi Alejandro
--@Fecha de creación:     23/01/2021
--@Descripción:           Carga de datos

\copy categoria FROM 'data/categoria.csv' DELIMITER ',' CSV HEADER;
\copy titulo FROM 'data/titulo.csv' DELIMITER ',' CSV HEADER;
\copy creditos_titulos FROM 'data/creditos_titulo.csv' DELIMITER ',' CSV HEADER;
\copy duracion_titulo FROM 'data/duracion_titulo.csv' DELIMITER ',' CSV HEADER;
\copy plan_estudios FROM 'data/plan_estudios.csv' DELIMITER ',' CSV HEADER;
\copy campus FROM 'data/campus.csv' DELIMITER ',' CSV HEADER;
\copy tipo_escuela FROM 'data/tipo_escuela.csv' DELIMITER ',' CSV HEADER;
\copy facultad FROM 'data/facultad.csv' DELIMITER ',' CSV HEADER;
\copy generacion FROM 'data/generacion.csv' DELIMITER ',' CSV HEADER;
\copy apellido_materno FROM 'data/apellido_materno.csv' DELIMITER ',' CSV HEADER;
\copy apellido_paterno FROM 'data/apellido_paterno.csv' DELIMITER ',' CSV HEADER;
\copy genero FROM 'data/genero.csv' DELIMITER ',' CSV HEADER;
\copy edad FROM 'data/edad.csv' DELIMITER ',' CSV HEADER;
\copy estudiante FROM 'data/estudiante.csv' DELIMITER ',' CSV HEADER;
\copy trayectoria FROM 'data/trayectoria.csv' DELIMITER ',' CSV HEADER;












