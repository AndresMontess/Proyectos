#Las variables se crean de la siguiente menera:

my_variable = "My string variable"
print(my_variable)
#Para definir una variable se hace en serpiente con un _

my_int_val = 5
print(my_int_val)

my_bolean_val = True
print(my_bolean_val)

#Concatenacion de variables en un print
my_int_to_string_val = str(my_int_val)
print(my_int_to_string_val)
print(type(my_int_to_string_val))

print(my_variable, my_int_to_string_val, my_bolean_val)
print("Este es el valor de:", my_bolean_val)

#Esto sirve para pasar una cantidad de datos que va ha montar dentro de una cadena nos muestra una cadena qeu ah conseguido crear con los datos de las variables

#Comentario es un lemguaje de interpretacion no de compilación 

#ASi SE ROMPE PYTHON jeje
print(type(print(my_variable, my_int_to_string_val, my_bolean_val))) #EL tipo es 'NoneType'

#Alguna funcion del sistema 
print(len(my_variable))

#Variables en 1 sola linea se puede hacer pero no es recomendable
name, surname, alias, age = "Andres", "Montes", "ANDYGYM", 19

print("Me llamo:", name, surname,"Mi edad es:", age,"Mi alias", alias)

#Imputs
first_name = input('What is your name')
ages = input('How old are you')

print(first_name)
print(ages)