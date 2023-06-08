### Bucles ###

# While Atado a cumplir una condición hasta el infinito

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1
else: #Es opcional
    print("Mi condicion es mayor a 10")
    
print("La ejecucion continua")
#Para la detencion forzada de se utiliza break
while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
      print("Mi condicion es es 15")
      break
 
    print("Mi condicion es menor a 20")

print("La ejecucion continua")

# For Atado a un numero finito de datos a ver cuantso elemnetos le estamos indicando en una posible iteracion(Lists, sets,tuples,diccionarios)

my_list = [19, 24, 62, 52, 30, 30, 17]
# Un for se repite tantas  veces como elementos tiene iterados(Metidos/incluidos/etc)
#For imprime los datos itinerados, teniendo en cuenta que los dics tenemos que especificarle los .values para ver los datos y no las claves
for element in my_list:
    print(element)
   
my_tuple = (19, 60, 30, 120,23) 


for element in my_tuple:
    print(element)


my_Set = {"Andres", "Montes", 19}
for element in my_Set:
    print(element)


my_dict = {
    "Nombre":"Andres",
    "Apellido":"Montes", 
    "Edad":19,
    "Lenguajes":{"Python", "Swift", "kotlin"},
    1: 1.75
    }

for element in my_dict:
    print(element)
    
for element in my_dict.values():
    print(element)
    if element == 19:
        break
    print("se ejecuta")
else:
    print("mi vicle for ha finalizado")

for element in my_dict.values():
    print(element)
    if element == 19:
        continue
    print("se ejecuta")
else:
    print("mi vicle for ha finalizado")