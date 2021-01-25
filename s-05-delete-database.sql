--@Autores:               Barrero Olguín Patricio
--                        Martínez Ostoa Néstor
--                        Ramírez Bondi Alejandro
--@Fecha de creación:     22/01/2021
--@Descripción:           Borrado de tablas

--delete tables of the database
drop table trayectoria;
drop table estudiante;
drop table genero;
drop table apellido_paterno;
drop table apellido_materno;
drop table generacion;
drop table facultad;
drop table tipo_escuela;
drop table campus;
drop table plan_estudios;
drop table duracion_titulo;
drop table creditos_titulos;
drop table titulo;
drop table edad;
drop table categoria;

--delete database

/*
\c cursodb
drop database if exists proyecto_universidad_003;
*/