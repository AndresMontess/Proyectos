### Operadores Aritmeticos ###

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 // 3) #Division de enteros
print(2 ** 3)# Exponente
print(2 ** 3 + 3 - 7 / 1 //4)

print("Hola " + "Python " + "¿Que tal?")
#no se puede concatenar un string con un int
#print("Hola " + 5)

#Pero usando la función str o int o bool etc se podra hacer
print("Hola " + str(5))

#sin print es decir 6+2 no funciona sin print

#Operador de Modulo
print(10 % 3)

#Se ejecuta 5 veces la palabra hola por el signo multiplicar pero como vemos en el siguiente ejemplo podemos hacer multiplicaciones de operaciones simples
print("Hola " * 5)
print("Hola " * (2 + 4))
print("Hola " * (2 ** 3))

#Como podemos ver en este ejemplo tenemos la multiplicación de caracteres desde una operacion introducida en una variable
my_float = 2.5 * 2
print("Hola " * int(my_float))

### Operadores Comparativos ###

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)
print("")
print(3 > 4 == 2)
print(3 > 4 > 2)

print("")
print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa")#Calcula el True o el False a traves de la ordenacion alfabética por ASCII tiene en cuenta las mayusculas
print(len("aaaa") >= len("abaaa"))#Este cuenta los caracteres que hay en cada una
print("Hola" <= "Python")
print("Hola" == "Python")
print("Hola" != "Python")
print("")
print(3 > 4 == 2)
print(3 > 4 > 2)

### Operadores Lógicos ###
print("")
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print("")
print(3 < 4 and "Hola" < "Python")
print(3  < 4 or "Hola" < "Python" and 4 == 4)
print("")
#Not niega la condición, es decir si la condicion reslutaba false mostraba true, y si tenemos una respuesta de true tenemos un false
print(not (3 > 4))


