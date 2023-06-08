#Esto es un comentario
print("Hola Mundo")
print("hello World")

"""
    Esto es im comentario en varias lineas
    Linea2
    Linea3
"""


print(+111111)
print(-111111)
#Se pueden imprimir nuemeros hexadecimales y octales
print(0o123)
print(0x123)

print(0.0000000000000000000001)
print(1e-22)


print(True > False)
print(True < False)

print(9 % 6 % 2)

print(2 * 3 % 5)

print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)

print((2 ** 4), (2 * 4.), (2 * 4))

print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))

print((2 % -4), (2 % 4), (2 ** 3 ** 2))

print("Dime algo...")
anything = input()
print("Mmm...", anything, "...¿en serio?")

#Calculemos triangulos
leg_a = float(input("Inserta la longitud del primer cateto: "))
leg_b = float(input("Inserta la longitud del segundo cateto: "))
print("La longitud de la hipotenusa es: ", (leg_a**2 + leg_b**2) ** .5)