'''
/*
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */
'''

def my_funcion(figura, *argumentos):
    if figura == "Triangulo" and len(argumentos) ==  2:
        base, altura = argumentos
        area = 0.5 * base * altura 
        return area
    elif figura == "Cuadrado" and len(argumentos) == 1:
        lado = argumentos
        area = lado * lado
        return area
    elif figura == "Rectangulo" and len(argumentos) == 2:
        base, altura = argumentos
        area = base * altura
        return area
    else:
        return "La figura no es valida datos incorrectos"
    
    
print(my_funcion("Triangulo", 5, 3))
print(my_funcion("Rectangulo", 6, 8))