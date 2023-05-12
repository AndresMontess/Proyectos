create database if not exists Coches
DEFAULT CHARACTER SET utf8
default collate UTF8_general_ci;

Use Coches;

create table Camion (
Cod_Camion varchar(20)  not null,
Potencia varchar(20) not null,
modelo varchar(20) not null,
Tipo varchar(20) not null,
primary key(Cod_Camion)
)engine = InnoDB;

create table Ciudad(
Cod_Ciudad varchar(20) not null,
Nombre varchar(20) not null,
primary key(Cod_Ciudad)
) engine=InnoDB;

create table Paquete(
Cod_Paquete varchar(20) not null,
Peso varchar(20) not null,
Descripcion varchar(20) not null,
Cod_Ciudad varchar(20) not null,
primary key (Cod_Paquete),
foreign key (Cod_ciudad) references Ciudad(Cod_Ciudad)
) engine=InnoDB;

create table Camionero(
Cod_Cam varchar(20) not null,
Nombre varchar(20) not null,
Poblacion varchar(20) not null,
Cod_Paquete varchar(20) not null,
primary key (Cod_Cam),
foreign key (Cod_Paquete) references Paquete(Cod_Paquete)
)engine=InnoDB;

create table Camion_Camionero (
Fecha date not null,
Cod_Cam varchar(20) not null,
Cod_Camion varchar(20) not null,
primary key (Fecha, Cod_Camion, Cod_Cam),
Foreign key (Cod_Cam) references Camionero(Cod_Cam),
Foreign key (Cod_Camion) references Camion(Cod_Camion)
)Engine=InnoDB;