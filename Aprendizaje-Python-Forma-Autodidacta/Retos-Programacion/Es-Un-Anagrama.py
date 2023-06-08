'''
/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */
 '''
 
'''EXPLICACIÓN DEL CODIGO
Primero usamos la palbra resevada def para definir una función seguidamente empezamos con los condicionales es decir:
    -Si la logitud de word1(mi variable) es distinta de la longitud de word2(mi otra variable) dime que no pueden ser anagramas por la longitud
    -Si no lo que hago es convertir esas palabras en listas para ordenarlas y aprovecho a usar sort, (Esta deficnicion es con mis palabras)
    .sort lo que nos permite es organizar segun un criterio especifico los datos a representar en un a lista, además podemos decirle el orden en especifico 
    a traves de lo parentesis oblogatorios, dejando la ordenacion por defecto puediendo así saber si contiene las mismas letras comparando las listas,
    -Por ultimo le digo su la lista_word1 es igual a lista_word2 dime que las palabras son anagramas 
    -Sino dime por terminal que estas palabras no son anagramas
    
    PD: tambien os dejo la ordenacion de las letras 
    -['a', 'e', 'e', 'e', 'f', 'l', 'n', 't']
    -['a', 'e', 'e', 'e', 'f', 'l', 'n', 't']
'''
def my_function(Word1, Word2) :
    if len(Word1) != len(Word2):
        print("Las palabras no tienen la misma longitud, no pueden ser anagramas")
    else:
        lista_word1 = list(Word1)
        lista_word2 = list(Word2)
        lista_word1.sort()
        print(lista_word1)
        lista_word2.sort()
        print(lista_word2)
        if lista_word1 == lista_word2:
            print("Estas palabras son anagramas")
        else:
            print("Estas palabras no son anagramas")


my_function("elefante", "leefante")