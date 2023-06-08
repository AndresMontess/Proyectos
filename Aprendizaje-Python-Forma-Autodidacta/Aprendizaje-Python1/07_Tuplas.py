### Tuplas ###
#Tupla conjunto de valores
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.75, "Andres", "Montes", )
my_other_tuple = (19, 60, 30, 120,23)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Andres"))
print(my_tuple.index("Montes"))

# Las tuplas son irrefutables no se pueden editar con los siguientes comandos
#my_tuple[1] = 1.77
#print(my_tuple)

print(my_tuple + my_other_tuple)

