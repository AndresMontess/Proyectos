'''
/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */
'''
my_val, my_other_val = 0, 1

while my_val <= 50:
    print(my_val) 
    my_val, my_other_val = my_other_val, my_val + my_other_val

    

 