create database if not exists Educativo
DEFAULT CHARACTER SET utf8
default collate UTF8_general_ci;

use Educativo;

create table Especialidad (
Cod_especialidad varchar(7) not null,
Nombre varchar(20) not null,
Logo varchar(20) not null,
primary key (Cod_especialidad)
)engine=InnoDB;

create table Ciclofp (
Cod_Ciclo varchar(3) not null,
Cod_esp varchar(10) not null,
Nombre varchar(10) not null,
nivel varchar(8) not null,
primary key(Cod_Ciclo),
foreign key (Cod_esp) references Especialidad(Cod_especialidad)
) engine= InnoDB;

create table Centrodes(
Cod_Centro varchar(3) not null,
Nombre varchar(10) not null,
ubicacion varchar(20) not null,
direccion varchar(50) not null,
primary key(Cod_Centro)
) engine=InnoDB;

create table Alumnos(
n_Expediente varchar(3) not null,
Cod_Centro varchar(3) not null,
nombre varchar(20) not null,
Apellidos varchar(20) not null,
primary key(n_Expediente),
foreign key (Cod_Centro) references Centrodes(Cod_Centro)
) engine=InnoDB;

create table Centros_p (
Cod_Centro varchar(3) not null,
Dotacion int not null,
año_cr varchar(4) not null,
primary key(Cod_Centro),
foreign key (Cod_centro) references Centrodes(Cod_Centro) 
)engine=InnoDB;

create table Centro_c (
Cod_centro varchar(3) not null,
Ayuntamiento varchar(15) not null,
primary key(Cod_centro),
foreign key (Cod_centro) references Centrodes(Cod_Centro) 
) Engine=InnoDB;

create table Alumnos_Ciclo(
Fecha date not null,
nota_Final tinyint not null,
n_exp varchar(3) not null,
Cod_ciclo varchar(3) not null,
primary key(n_exp,Cod_ciclo,fecha),
foreign key (n_exp) references Alumnos(n_Expediente),
foreign key (Cod_ciclo) references Ciclofp(Cod_Ciclo)
)engine=Innodb;
