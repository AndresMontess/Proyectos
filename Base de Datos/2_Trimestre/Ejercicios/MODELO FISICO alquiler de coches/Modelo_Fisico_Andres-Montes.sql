create database if not exists Agencia
DEFAULT CHARACTER SET utf8
default collate UTF8_general_ci;

Use alquiler_coche;

Create table Agencia(
Cod_Agencia varchar(40) Not Null,
Nombre varchar(14) Not Null,
Foto varchar(100),
Primary key(Cod_Agencia)
)engine = InnoDB;
create table Cliente(
Cod_Cliente varchar(10) Not Null,
Dni varchar(9) not null unique,
Nombre varchar(15) not null ,
Apellido varchar(45) not null,
Foto varchar(20) not null,
Aval varchar(10) ,
Primary key(Cod_Cliente))engine = InnoDB;
create table Modelo(
Cod_Modelo varchar(35) not null,
Potencia varchar(5),
Capacidad varchar(10),
primary key(Cod_Modelo)
)engine = InnoDB;
create table Garage(
Cod_Garage varchar(35) not null,
Ubicacion varchar(30) not null,
Foto varchar(45) not null,
primary key(Cod_Garage)
)engine = InnoDB;
create table Coches(
Cod_coche varchar(35) not null,
Color varchar(20) not null,
Matricula varchar(8) not null,
Id_Reserva varchar(30) not null,
Id_Garage varchar(35) not null,
Id_Agencia varchar(40) not null,
Id_Modelo varchar(35) not null,
primary key(Cod_Coche)
)engine = InnoDB;
create table Reserva(
Cod_Reserva varchar(30) not null,
Precio varchar(15) not null,
Fecha_inicio varchar(10) not null,
Fecha_fin varchar(35) not null,
Id_Cliente varchar(10) not null,
Id_Agencia varchar(40) not null,
primary key(Cod_reserva)
)engine = InnoDB;
create table Coches_Reservas(
Id_Reserva varchar(30) not null,
Id_Coches varchar(35) not null,
Gasolina varchar(10) not null,
Fecha_entrega varchar(12) not null,
primary key(Cod_Reserva,Cod_Coches)
)engine = InnoDB;
alter table Reserva add foreign key (Cod_cliente) references Cliente(Id_Cliente) on delete cascade on update cascade;
alter table Coches_Reservas add foreign key (Cod_Reserva) references Reserva(Id_Reserva) on delete cascade on update cascade;
alter table Coches_Reservas add foreign key (Cod_Coche) references Coches(Id_Coches) on delete cascade on update cascade;
alter table Reserva add foreign key (Cod_Agencia) references Agencia(Id_Agencia) on delete cascade on update cascade;
alter table Coches add foreign key (Cod_Garage) references Garage(Id_Garage) on delete cascade on update cascade;
alter table Coches add foreign key (Cod_Agencia) references Agencia(Id_Agencia) on delete cascade on update cascade;
alter table Coches add foreign key (Cod_Modelo) references Modelo(Id_Modelo) on delete cascade on update cascade;
