### Funciones ###

def my_function ():
    print("Esto es una función")
    
my_function ()

def sum_two_values(first_num, Second_num):
    print(first_num + Second_num)
    
sum_two_values(5, 6453)

def sum_two_values_with_return(first_num, Second_num):
    return first_num + Second_num 

my_result = sum_two_values_with_return(2, 21)
print(my_result)

def sum_two_values_with_return(first_num, Second_num):
    my_sum = first_num + Second_num 
    return my_sum

def print_name(Name, Surname):
    print(f"{Name} {Surname}")

print_name(Surname="Montes",Name="Andres")

def print_name_default(Name, Surname, alias = "Sin alias"):
    print(f"{Name} {Surname} {alias}")

print_name_default(Surname="Montes",Name="Andres", alias="DJMontes")

def print_text(text):
    print(text)

print_text("Hola Buenas tardes")

# Funciones aprendidas en los retos #
'''
La funcion .sort lo que nos permite es organizar segun un criterio especifico los datos a representar en un a lista, además podemos decirle el orden en especifico 
a traves de lo parentesis oblogatorios
'''
numeros = [5, 2, 8, 1, 9]
numeros.sort()
print(numeros)  # Salida: [1, 2, 5, 8, 9]

palabras = ['zorro', 'oso', 'gato', 'perro']
palabras.sort()
print(palabras)  # Salida: ['gato', 'oso', 'perro', 'zorro']
