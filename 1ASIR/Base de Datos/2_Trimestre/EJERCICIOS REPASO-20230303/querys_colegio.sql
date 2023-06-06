-- Consulta Pregunta 1 --
Select * from alumno a, labor_extra l 
where a.id=( select l.id where l.nombre='Delegado de clase');

-- Consulta Pregunta 2--
select  a.nombre, count(n.id) as cantidad from asignatura a, nota n
where a.id=n.asignatura_id
group by a.nombre;

-- Consulta Pregunta 3--
select  a.nombre,  min(n.calificacion) as nota from asignatura a, nota n
where a.id=n.asignatura_id
group by a.nombre;

-- Consulta Pregunta 4--
select al.nombre, al.apellido,a.nombre, n.calificacion, n.convocatoria from nota n, alumno al, asignatura a
where n.alumno_id=al.id
and n.asignatura_id=a.id
and n.calificacion < 5;

-- Insert Pregunta 5 --
INSERT INTO labor_extra (nombre, alumno_id) 
(select 'Encargado Asistencias',id from alumno where nombre='Pedro');

-- Consulta Pregunta 6--
select count(n.calificacion) as Numero_Notas from nota n; 

-- Consulta Pregunta 7--
select al.nombre, al.apellido, avg (n.calificacion) as Media from nota n, alumno al
where n.alumno_id=al.id
group by al.nombre, al.apellido;

-- Consulta Pregunta 8--
select * from nota
where fecha_examen>('2018-10-31') and fecha_examen<('2018-12-01');

