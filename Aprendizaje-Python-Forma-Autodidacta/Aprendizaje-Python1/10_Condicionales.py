### Condicionales ###

my_condition = False
my_other_condition = False

if my_condition :
    print("Se ejecuta la condicion del if")



my_condition = 1


if my_condition == 10:
    print("Se ejecuta la condicion del segundo if")

if my_condition >= 10:
    print("Se ejecuta la condicion del Tercer if")
    
if my_condition > 10:
    print("Es mayor que 10")
else:
    print("Es menor o igual a 10")


print("")

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
else:
    print("Es menor o igual a 10 o mayor igual a 20")

print("La ejecucion continua")

print("")

#Else if es condicional y jerarquico es decir el orden de los else o elif tiene relevancia en el codigo
if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 1:
    print("Es un numero 1")
else:
    print("Es menor o igual a 10 o mayor igual a 20")