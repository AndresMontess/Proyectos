### Diccionarios ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Andres", "Apellido":"Montes", "Edad":19, 1:"Python"}
#Diccionario Estucctura en la que podemos gruardar datos de clave valor.
my_dict = {
    "Nombre":"Andres",
    "Apellido":"Montes", 
    "Edad":19,
    "Lenguajes":{"Python", "Swift", "kotlin"},
    1: 1.75
    }
print(type(my_other_dict))
print(type(my_other_dict.values()))
print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

#La peculiaridaad de los diccionarios la facicidad que tenemos para acceder a un elemento.
print(my_dict["Edad"])
print(my_dict["Nombre"])

#Esta la forma en la que actualizamos los datos.
my_dict["Calle"] = "Pepe el jose"
print(my_dict)

#Esta es la forma que tenemos de eliminar solo un dato de nuestro diccionario de datos.
#No se puede recuperar un dato eliminado.
del my_dict["Calle"]
print(my_dict)

#Esto lo busca en las claves es decir en este caso buscara la clave Andres que no existe,para que nos muestre true le debemos pasar la clave como en el segundo caso
print("Andres" in my_other_dict)
print("Andrei" in my_other_dict)

print("Nombre" in my_other_dict)
print("Nommbre" in my_other_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
print(my_dict.fromkeys(("Nombre", 1)))

#No necesariamente creamos un diccionario en base al anterior, le hemos incluido piso tan tranquilamente se lo traga como quien dice.
my_new_dict = my_dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)
#Este es el uso real por lo que yo creo
my_new_dict = my_dict.fromkeys(my_dict)
print(my_new_dict)
#Esto no funciona porque no hay correlacion el no sabe para que lado va cada dato
my_new_dict = my_dict.fromkeys(my_dict, ["Andres", "Montes" ])
print(my_new_dict)
#Esta lista solo muestra las claves del diccionario
print(list(my_dict.values()))