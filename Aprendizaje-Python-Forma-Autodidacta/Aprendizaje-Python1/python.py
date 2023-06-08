my_first_str = "Hola"
my_other_str = "Python"

print(my_first_str, (my_other_str))

print(100-99)

my_num = 2
my_num2 = 3

print(my_num + my_num2)
print(my_num - my_num2)
print(my_num * my_num2)
print(my_num / my_num2)



'''
fnam = input("¿Me puedes dar tu nombre?")
lnam = input("Me puedes dar tu apellido")
print("Graciasss")
print("\nTu Nombre es " + fnam + " " + lnam + ".") 
'''
print("Hola" * 4)

print(3 * "an")

print(5 * "2")

print(5 * int(2))

'''
leg_a = float(input("Inserta la longitud del primer cateto: "))
leg_b = float(input("Inserta la longitud del segundo cateto: "))
print("La longitud de la hipotenusa es: ", str((leg_a**2 + leg_b**2) ** .5))


num_a = float(input("Dame un numero por favor "))
num_b = float(input("Dame un numero por favor "))

print(num_a + num_b)
print(num_a - num_b)
print(num_a * num_b)
print(num_a / num_b)
print("\n¡Eso es todo, amigos!")
'''
'''
hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

my_val = hour + mins
print(my_val + dura)
'''

'''
# Obtener el tiempo inicial
tiempo_inicial_horas = int(input("Ingrese la hora inicial (0-23): "))
tiempo_inicial_minutos = int(input("Ingrese los minutos iniciales (0-59): "))

# Obtener la duración del periodo de tiempo
duracion_horas = int(input("Ingrese la duración en horas: "))
duracion_minutos = int(input("Ingrese la duración en minutos: "))

# Calcular el tiempo final
tiempo_final_horas = (tiempo_inicial_horas + duracion_horas) % 24
tiempo_final_minutos = (tiempo_inicial_minutos + duracion_minutos) % 60

# Mostrar el resultado
print("El tiempo final es: {:02d}:{:02d}".format(tiempo_final_horas, tiempo_final_minutos))
'''

'''
x = int(input())
y = int(input())

x = x / y
y = y / x

print(y)
'''
print(1 // 2*3)

print("pp\nep")

'''
x = int(input())
y = int(input()) 

x = x % y
x = x % y
y = y % x

print(y)
'''
'''
x = input()
y = int(input())

s = x*y

print(s)
'''
'''
x = input()
y = input()

s = x+y

print(s)
'''
'''
x = int(input())
y = int(input()) 

x = x // y
y = y // x

print(y)
'''
print(1/1)

x = 1/ 2 + 3 // 3 + 4 ** 2
print(x)








