'''
/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
'''
my_variable = 1

for my_variable in range(1, 101):
    print(my_variable)
    my_variable = my_variable + 1
    if my_variable % 3 == 0 and my_variable % 5 == 0:
        print("fizz")
    elif my_variable % 3 == 0:
        print("buzz")
    elif my_variable % 5 == 0:
        print("FizzBuzz")

