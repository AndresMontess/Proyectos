drop database liga;
Create database if not exists liga;

use liga;

create table Rango(
Cod_Rango varchar(20) not null,
Nombre varchar(20) not null,
Descripcion varchar(20) not null,
primary key(Cod_Rango)
)Engine=InnoDB;

create table Modos(
Cod_Modo varchar(10) not null,
Nombre varchar(20) not null,
Toplane varchar(20) not null,
Jungle varchar(20) not null,
Midlane varchar(20) not null,
ADC varchar(20) not null,
Support varchar(20) not null,
Cod_Rango varchar(20) not null,
constraint Rango_FkK foreign key (Cod_Rango) references Rango (Cod_Rango),
primary key(Cod_Modo)

)engine=InnoDB;

Create table Campeones(
Cod_Campeon varchar(10) not null,
Nombre varchar(20) not null,
hablidad1 varchar(10) not null,
habilidad2 varchar(10) not null,
habilidad3 varchar(10) not null,
pasiva varchar(20) not null,
Origen varchar(20) not null,
primary key(Cod_Campeon)
)engine=InnoDB;

create table Jugadores(
Id_Jugador varchar(20) not null,
Email varchar(30) not null,
n_telefono tinyint null,
Cod_Rango varchar(20) not null,
Cod_Campeon varchar(10) not null,
constraint Rango_fk foreign key (Cod_Rango) references Rango(Cod_rango),
constraint Campeones_fkk foreign key (Cod_Campeon) references Campeones(Cod_Campeon),
primary key(Id_Jugador)
)engine=InnoDB;

create table Partidas (
Cod_Partida varchar(20) not null,
Nombre varchar(20) not null,
Tiempo varchar(20) not null,
Cod_Rango varchar(20) not null,
Cod_Modo varchar(10) not null,
constraint Raango_fkk foreign key (Cod_Rango) references Rango(Cod_Rango),
constraint Modo_fk foreign key (Cod_Modo) references Modos(Cod_Modo),
primary key (Cod_Partida)
)engine=InnoDB;

create table Partidas_Jugadores (
fecha date not null,
Hora varchar(6),
Cod_Jugador varchar(20) not null,
Cod_Partida varchar(20) not null,
constraint player_id foreign key (Cod_Jugador) references Jugadores(ID_Jugador),
constraint partida_id foreign key (Cod_Partida) references Partidas(Cod_Partida),
primary key(fecha) 
)engine=InnoDB;
