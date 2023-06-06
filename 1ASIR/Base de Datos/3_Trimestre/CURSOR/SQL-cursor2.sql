DELIMITER //
CREATE procedure das_ingreso(paciente varchar(2))
BEGIN
Declare diasA int default 0;
Declare diasB int default 0;
Declare Resultado int default 0;
DECLARE cursor2 CURSOR FOR SELECT Fecha_alta,Fecha_ingreso FROM ingresos where Cod_paciente = paciente;
        OPEN cursor2;
        fetch_loop:loop
        fetch cursor2 into diasA;
        fetch cursor2 into diasB;
        if done then
        leave fetch_loop;
        END IF;
		set  Resultado = diasA - diasB;
        End LOOP;
        
    
    
END //
DELIMITER ; 