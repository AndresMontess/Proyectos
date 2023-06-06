-- Creación BBDD
CREATE DATABASE colegio CHARACTER SET UTF8mb4 COLLATE utf8mb4_bin;
-- Uso BBDD
USE colegio;

CREATE TABLE asignatura ( 
  id INT(6) NOT NULL auto_increment,
  nombre VARCHAR(25) NOT NULL, 
  PRIMARY KEY  (id) 
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1;

CREATE TABLE alumno ( 
  id INT(6) NOT NULL auto_increment,
  nombre VARCHAR(25) NOT NULL, 
  apellido VARCHAR (25) NOT NULL, 
  fecha_nacimiento DATE NOT NULL, 
  PRIMARY KEY  (id) 
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1;

CREATE TABLE nota ( 
  id INT(6) NOT NULL auto_increment,
  asignatura_id INT,
  calificacion FLOAT NOT NULL, 
  fecha_examen DATE NOT NULL, 
  convocatoria INT(6),
  alumno_id INT,
   INDEX alum_ind (alumno_id),
   FOREIGN KEY (alumno_id)
      REFERENCES alumno(id)
       ON DELETE CASCADE,	
   INDEX asignat_ind (asignatura_id),
   FOREIGN KEY (asignatura_id)
      REFERENCES asignatura(id)
       ON DELETE CASCADE,			 	    
  PRIMARY KEY (id) 
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=1;

CREATE TABLE labor_extra ( 
  id INT(6) NOT NULL auto_increment,
  nombre VARCHAR (25) NOT NULL, 
  alumno_id INT,
   INDEX alum_ind (alumno_id),
   FOREIGN KEY (alumno_id)
      REFERENCES alumno(id)
       ON DELETE CASCADE,				 	    
  PRIMARY KEY (id) 
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=1;