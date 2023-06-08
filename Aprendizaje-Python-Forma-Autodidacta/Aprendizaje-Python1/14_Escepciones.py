### Excepciones Handling ### 
#Controlamos los errores con las excepciones
numberOne, NnumberTwo = 5, 1
NnumberTwo = "2"

#Try except

try:
    print( numberOne + NnumberTwo)
    print( "no se ha producido un error")
except:
    print("Se ha producido un error")

# Try except else f
    
try:
    print( numberOne + NnumberTwo)
    print( "no se ha producido un error")
except:
    print("Se ha producido un error")
else: #Esta linea solo se ejecuta si el except no ha ocurrido, estos son los diferentes caminos que pueden seguir
    print("La ejecucion continua correctamente")

# Try except else fin

try:#Necesarios si queremos usar el except
    print( numberOne + NnumberTwo)
    print( "no se ha producido un error")
except:#Necesarios si queremos usar el try
    print("Se ha producido un error")
else: #Opcionales
    print("La ejecucion continua correctamente")
finally:#Opcionales
    #Este se ejecuta siempre
    print("La ejecucción continua, se ejecuta")
    
# Captura de excepciones por tipo
#Estos except solo se ejecutan cuando ocurre el tipo de error que le indicamos en este caso es typeerror y para.
try:#Necesarios si queremos usar el except
    print( numberOne + NnumberTwo)
    print( "no se ha producido un error")
except TypeError:#Necesarios si queremos usar el try
    print("Se ha producido un error")
except ValueError:#Necesarios si queremos usar el try
    print("Se ha producido un error")


