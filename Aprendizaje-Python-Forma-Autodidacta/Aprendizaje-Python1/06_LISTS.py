### Listas ###

# Una lista es una estructura, lo que con una estructura de datos podemos formar filas y columnas, son los "arreglos" de npython.
my_list = list()
my_other_list = []

print(len(my_list))

my_list = [19, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))
print(type(my_list))


#Una lista puede contener varios tipos de datos en este caso hemos introducido un string, un int y un float

my_other_list = [35, 1.75, "Andres", "Montes"]
print(my_other_list)
print(type(my_other_list))#Type nos muestra que es un lista

#Una lista significa que podemos acceder a los datos que queramos de forma independiente

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_other_list[-4])
#print(my_other_list[-5])
print(my_other_list.count("Andres"))
print(my_list.count(30))#Return number of occurrences of value retorna el numero de veces que esta el dato repetido en la lista.
'''
Este indice no tiene elemento -5 es decir si no hay datos suficientes en la lista nos mostrara error, es deir en positivo del 0-3 todo bien en este caso del -1 al -4 todo bien
pero cuando llegamos al -5 0 al 4 nos dara el error de index de que la lista esta fuera de rango es decir no hay datos suficientes
'''

age, height, name, surname = my_other_list
print(height,age ,name,surname)
print(list([1,2,3,4]))

print(my_list + my_other_list)

#El append introduce al final de la lista un dato nuevo el que nosotros le digamos.
my_other_list.append("Montes.sl")
print(my_other_list)

#Para utilizar el insert debemos 1 poner la posicion de la lista en la que queremos insertar el dato o la informacion "," la informacion, 
#el dato que estaba en esa posicion pasa al 2
my_other_list.insert(1, "Verde")
print(my_other_list)
#Remove elimina el dato que queramos
my_other_list.remove("Verde")
print(my_other_list)

my_list.remove(30)
print(my_list)
#Pop quita el ultimo dato, con el print pop nos devuelve el dato eliminado
print(my_list.pop())
print(my_list)
#se pueden copiar listas

my_new_list = my_list.copy()








#Al ser un lenguage no fuertemente tipado, nos sobreponemos a la lista anterior y le damos el valor de una string
my_list = "Hola Python"
print(my_list)