create database if not exists Hoteles
DEFAULT CHARACTER SET utf8
default collate UTF8_general_ci;

Use Hoteles;

create table Hotel(
Cod_Hotel varchar(30) not null,
Nombre varchar(45) not null,
Ubicación varchar(20) not null,
ano_Construccion varchar(20) not null,
primary key (Cod_Hotel)
)engine = Innodb;

Create table Servicio(
Cod_Servicio varchar(10) not null,
Servicio_de_habitaciones varchar(30) not null,
Comedor varchar(20) not null,
Bano int(4) not null,
primary key (Cod_Servicio)
)Engine = InnoDB;

create table Categoria(
Cod_Categoria varchar(30) not null,
Descripcion varchar(20) not null,
Requisitos varchar(30) not null,
primary key (Cod_Categoria),


)engine = InnoDB;

create table Planta(
Cod_Planta varchar(20) not null,
Nombre varchar(20) not null,
n_Habitaciones varchar(20) null,
primary key(Cod_Planta)
)engine = InnoDB;

create table Reservas(
Cod_Reserva varchar(20) not null,
Nombre varchar(30) not null,
Dirección varchar(20) not null,
primary key (Cod_Reserva)
)engine = InnoDB;

create table Cliente (
Cod_Cliente varchar(25) not null,
Nombre varchar(15) not null,
DNI varchar(9) not null unique,
Apellidos varchar(15) not null,
primary key (Cod_Cliente)
)engine=InnoDB;

create table Temporada(
Cod_Temporada varchar(30) not null,
Temporada varchar(20) not null,
Tipo varchar(10),
primary key (Cod_Temporada)
)engine= InnoDB;

create table Habitaciones(
Cod_Habitación varchar(10) not null,
Nombre varchar(20) not null,
Tipo_Habitacion varchar(30) not null,
N_planta varchar(20) not null,
primary key (Cod_Habitacion),
FOREIGN KEY (N_planta) REFERENCES Planta(Cod_planta)
) engine = InnoDB;

create table hotel_Categoria(
Fecha varchar(20) not null,
COd_Hotel varchar(30) not null,
Cod_Categoria varchar(30) not null,
Primary key (Fecha, COD_Hotel, Cod_Categoria),
FOREIGN KEY (Cod_Hotel) REFERENCES Hotel(Cod_Hotel),
FOREIGN KEY (Cod_Categoria) REFERENCES Categoria(Cod_Categoria)
)engine = InnoDB;

