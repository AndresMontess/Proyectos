CREATE DATABASE bomberos;
USE bomberos;

create table Parque(
Cod_Parque varchar(10) not null,
Nombre varchar(20) not null,
Primary key (Cod_parque)
) engine = InnoDB;

create table Turno(
Cod_turno varchar(20) not null,
Primary key (Cod_Turno)
)engine = InnoDB;

create table Equipo (
Cod_Equipo varchar(20) not null,
Nombre varchar(20) not null,
Cod_Parque varchar(10) not null, 
Primary key(Cod_Equipo),
foreign key (Cod_Parque) references Parque(Cod_Parque)
)engine = InnoDB;

create table Bombero(
Cod_bombero varchar(9) not null,
Nombre varchar(10) not null,
Apellido varchar(20) not null,
Edad int(10) not null,
Cod_Equipo varchar(20) not null,
primary key(Cod_bombero),
foreign key (Cod_Equipo) references Equipo(Cod_Equipo)
)Engine = InnoDB;

create table Turnos_Bombero(
Cod_Turno varchar(20) not null,
Cod_bombero varchar(9) not null,
Fecha date not null ,
Fecha_Fin varchar(12) not null,
primary key(Cod_Turno,Cod_bombero,Fecha),
foreign key (Cod_Turno) references Turno(Cod_turno),
foreign key (Cod_bombero) references Bombero(Cod_bombero)
)engine = InnoDB;
