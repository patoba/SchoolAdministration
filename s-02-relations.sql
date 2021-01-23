CREATE TABLE categoria(
    llave_categoria NUMERIC(10, 0) PRIMARY KEY,
    nombre_categoria VARCHAR(20) not null
);

CREATE TABLE titulo(
    llave_titulo NUMERIC(10, 0) PRIMARY KEY,
    nombre_titulo VARCHAR(20) NOT NULL,
    llave_categoria NUMERIC(10, 0) NOT NULL,
    CONSTRAINT fk_llave_categoria
      FOREIGN KEY (llave_categoria) 
	  REFERENCES categoria(llave_categoria)
);

CREATE TABLE creditos_titulos(
    creditos_titulos NUMERIC(2, 0) PRIMARY KEY
);

CREATE TABLE duracion_titulo(
    duracion_titulo NUMERIC(2, 0) PRIMARY KEY
);

CREATE TABLE plan_estudios(
    llave_plan_estudios NUMERIC(10, 0) PRIMARY KEY,
    nombre_plan_estudios VARCHAR(20) NOT NULL,
    creditos_titulos NUMERIC(2, 0) NOT NULL,
    duracion_titulo NUMERIC(2, 0) NOT NULL, --numero semestre
    llave_titulo NUMERIC(10, 0) NOT NULL,
    CONSTRAINT fk_creditos_titulos
      FOREIGN KEY (creditos_titulos) 
	  REFERENCES creditos_titulos(creditos_titulos),
    CONSTRAINT fk_duracion_titulo
      FOREIGN KEY (duracion_titulo) 
	  REFERENCES duracion_titulo(duracion_titulo),
    CONSTRAINT fk_llave_titulo
      FOREIGN KEY (llave_titulo) 
	  REFERENCES titulo(llave_titulo)
);

CREATE TABLE campus(
    llave_campus NUMERIC(10, 0) PRIMARY KEY,
    nombre_campus VARCHAR(20) not null
);

CREATE TABLE escuela(
    llave_tipo_escuela NUMERIC(10, 0) PRIMARY KEY,
    nombre_tipo_escuela VARCHAR(20) NO NULL,
    llave_campus NUMERIC(10, 0),
    CONSTRAINT fk_llave_campus
      FOREIGN KEY (llave_campus) 
	  REFERENCES campus(llave_campus)
);

CREATE TABLE facultad(
    llave_facultad NUMERIC(10, 0) PRIMARY KEY,
    nombre_facultad VARCHAR(20) NO NULL,
    llave_tipo_escuela NUMERIC(10, 0),
    CONSTRAINT fk_llave_tipo_escuela
      FOREIGN KEY (llave_tipo_escuela) 
	  REFERENCES escuela(llave_tipo_escuela)
);

CREATE TABLE generacion(
    llave_generacion NUMERIC(10, 0) PRIMARY KEY,
    fecha_ingreso DATE NOT NULL
);

CREATE TABLE apellido_materno(
    apellido_materno VARCHAR(20) PRIMARY KEY
);


CREATE TABLE apellido_paterno(
    apellido_paterno VARCHAR(20) PRIMARY KEY
);

CREATE TABLE creditos(
    creditos NUMERIC(2, 0) PRIMARY KEY
);

CREATE TABLE genero(
    genero VARCHAR(1) PRIMARY KEY 
);

CREATE TABLE estudiante(
    llave_estudiante NUMERIC(10, 0) PRIMARY KEY,
    nombre_estudiante VARCHAR(20) NOT NULL,
    apellido_materno VARCHAR(20) NOT NULL,
    apellido_paterno VARCHAR(20) NOT NULL,
    genero VARCHAR(1) PRIMARY KEY,
    llave_generacion NUMERIC(10, 0) PRIMARY KEY,
    CONSTRAINT fk_apellido_materno
      FOREIGN KEY (apellido_materno) 
	  REFERENCES apellido_materno(apellido_materno),
    CONSTRAINT fk_apellido_paterno
      FOREIGN KEY (apellido_paterno) 
	  REFERENCES apellido_paterno(apellido_paterno),
    CONSTRAINT fk_genero
      FOREIGN KEY (genero) 
	  REFERENCES genero(genero),
    CONSTRAINT fk_llave_generacion
      FOREIGN KEY (llave_generacion) 
	  REFERENCES generacion(llave_generacion),
);
 
CREATE TABLE trayectoria(
    llave_plan_estudios NUMERIC(10, 0),
    llave_facultad NUMERIC(10, 0),
    llave_estudiante NUMERIC(10, 0),
    estatus_estudiante varchar(20) NOT NULL,
    creditos NUMERIC(4, 0) NULL,
    fecha_titulacion DATE NULL, 
    CONSTRAINT fk_plan_estudios
      FOREIGN KEY (llave_plan_estudios) 
	  REFERENCES plan_estudios(llave_plan_estudios),
    CONSTRAINT fk_llave_facultad
      FOREIGN KEY (llave_facultad) 
	  REFERENCES facultad(llave_facultad),
    CONSTRAINT fk_llave_estudiante
      FOREIGN KEY (llave_estudiante) 
	  REFERENCES estudiante(llave_estudiante),
    CONSTRAINT pk_trayectoria 
      PRIMARY KEY (llave_plan_estudios, 
                   llave_facultad, 
                   llave_estudiante)
);