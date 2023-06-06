CREATE DATABASE IF NOT EXISTS R_Toxicos
DEFAULT CHARACTER SET utf8
DEFAULT COLLATE UTF8_general_ci;

USE R_Toxicos;

CREATE TABLE Quimicos(
Cod_quimico INT(5) NOT NULL,
Nombre VARCHAR(45) NOT NULL,
Simbolo VARCHAR(45) NOT NULL,
Ficha_seguridad VARCHAR(99) NOT NULL,
PRIMARY KEY (Cod_quimico)
)ENGINE=innodb;

CREATE TABLE Procuctor(
Cod_productor INT(5) NOT NULL,
Nombre VARCHAR(45) NOT NULL,
Direccion VARCHAR(45) NOT NULL,
CIF VARCHAR(9) unique NOT NULL,
PRIMARY KEY (Cod_productor)
)ENGINE=innodb;

CREATE TABLE Residuos(
Cod_residuo INT(5) NOT NULL,
Peso VARCHAR(6) NOT NULL,
Cantidad_total VARCHAR(10) NOT NULL,
Embase VARCHAR(45) NOT NULL,
Cod_productor INT(5) NOT NULL,
Cod_tratamiento INT(5) NOT NULL,
PRIMARY KEY (Cod_productor,Cod_residuos),
FOREIGN KEY (Cod_productor) REFERENCES Productor (Cod_productor),
FOREIGN KEY (Cod_tratamiento) REFERENCES Tratamiento (Cod_tratamiento)
)ENGINE=innodb;

CREATE TABLE Tartamiento(
Cod_tratamiento INT(5) NOT NULL,
Nombre VARCHAR(45) NOT NULL,
Duracion VARCHAR(10) NOT NULL,
Descripcion VARCHAR(99) NOT NULL,
PRIMARY KEY (Cod_tratamiento)
)ENGINE=innodb;

CREATE TABLE Transporte(
Cod_transporte INT(5),
Nombre VARCHAR(45),
Ubicacion_origen VARCHAR(45),
Coste_transporte VARCHAR(10),
Km_totales VARCHAR(10),
Cod_vehiculo INT(5) NOT NULL,
Cod_transportista INT(5) NOT NULL,
Cod_residuo INT(5) NOT NULL, 
Cod_destino INT(5) NOT NULL,
PRIMARY KEY (Cod_transporte),
FOREIGN KEY (Cod_transportista) REFERENCES Transportista (Cod_transportista),
FOREIGN KEY (Cod_vehiculo) REFERENCES Vehiculo (Cod_vehiculo),
FOREIGN KEY (Cod_residuo) REFERENCES Residuo (Cod_residuo),
FOREIGN KEY (Cod_destino) REFERENCES Destino (Cod_destino)
)ENGINE=innodb;

CREATE TABLE Transportista(
Cod_transportista INT(5) NOT NULL,
Nombre VARCHAR(45) NOT NULL,
Apellido VARCHAR(45) NOT NULL,
DNI VARCHAR(9) UNIQUE NOT NULL,
PRIMARY KEY (Cod_transportista)
)ENGINE=innodb;

CREATE TABLE Destino(
Cod_destino INT(5) NOT NULL,
Fecha_llegada DATE,
Direccion VARCHAR(45),
PRIMARY KEY (Cod_destino)
)ENGINE=innodb;

CREATE TABLE Vehiculo(
Cod_vehiculo INT(5) NOT NULL,
Foto VARCHAR(45),
Matricula VARCHAR(7),
PRIMARY KEY (Cod_vehiculo)
)ENGINE=innodb;

CREATE TABLE Residuos_Quimicos(
Cod_quimico INT(5) NOT NULL,
Cod_residuo INT(5) NOT NULL,
Cantidad_quimico VARCHAR(10),
PRIMARY KEY (Cod_quimico,Cod_residuos),
FOREIGN KEY (Cod_quimico) REFERENCES Quimico (Cod_quimico),
FOREIGN KEY (Cod_residuo) REFERENCES Residuos (Cod_residuo)
)ENGINE=innodb;