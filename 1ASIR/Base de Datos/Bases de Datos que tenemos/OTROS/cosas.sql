Create database Instituto;

use Instituto;

create table IES(
Cod_IES varchar(20) not null,
Nombre varchar(20) not null,
Ubicacion varchar(20) not null,
Localidad varchar(20) not null,
Primary key(Cod_IES)
)engine=InnoDB;

create table Ciclo(
Cod_Ciclo varchar(20) not null,
Denominacion varchar(20) not null,
N_total_horas int not null,
primary key(Cod_Ciclo)
)engine=InnoDB;

Create table Alumno(
NIA varchar(20) not null,
Nombre varchar(20) not null,
Apellidos varchar(20) not null,
Direccion varchar(20) not null,
primary key(NIA)
)engine=InnoDB;

create table IES_Ciclo(
Cod_IES varchar(20) not null,
Cod_Ciclo varchar(20) not null,
Turno varchar(20) not null,
primary key(Cod_IES, Cod_Ciclo, Turno),
foreign key (Cod_IES) references IES(Cod_IES),
foreign key (Cod_Ciclo) references Ciclo(Cod_Ciclo)
)engine=InnoDB;

create table Alumno_Ciclo(
Cod_Ciclo varchar(20) not null,
NIA varchar(20) not null,
Fecha date not null,
Nota_Final tinyint not null,
primary key(Cod_Ciclo, NIA, Fecha),
foreign key (Cod_Ciclo) references Ciclo(Cod_Ciclo),
foreign key (NIA) references Alumno(NIA)
)engine=InnoDB;
