use fp_comunidad_madrid;
select denominacion, decipcion
from  CICLOSFP INNER JOIN modulos 
on  CICLOSFP.DENOMINACION='ASIR' 
or CICLOSFP.DENOMINACION='DAW'
