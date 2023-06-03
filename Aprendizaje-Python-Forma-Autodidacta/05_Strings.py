### Stings ###

my_string = "Mi String"
my_other_string = 'Mi String'

print(len(my_string))
print(len(my_other_string))
print(my_string + "" + my_other_string)

my_new_string = "Este es un estring\ncon salto de linea"
print(my_new_string)

my_tab_sting = "Este es un estring\tcon tabulacion"
print(my_tab_sting)

my_scape_string = "\tEste es un string \n escapado"
print(my_scape_string)

#formateo

name, surname, age = "Andres", "Montes", 19

print("Mi nimbre es {} {} y mi edad es {} ".format(name, surname, age))
print("Mi nimbre es %s %s y mi edad es %d " %(name, surname, age))

print(f"Mi nimbre es {name} {surname} y mi edad es {age} ")

#Desenpaquetado de caracteres
language = "python"
a, b, c, d, e, f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#Division

language_slice = language[1:3]
print(language_slice)

#Reverse
reverse_language = language[::-1]
print(reverse_language)

# Funciones

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.lower().isupper())
print(language.startswith("y"))
