### Clases ###

class MyEmptyPerson: 
    pass 

print(MyEmptyPerson())
print(MyEmptyPerson)

class Person:
    def __init__(self, name, surname) :
        self.name = name
        self.surname  = surname

respuesta = Person(surname="Montes", name="Andres")
print(f"{respuesta.name} {respuesta.surname}")

class Person:
    def __init__(self, name, surname, alias = "Sin alias") :
        self.fullname = f"{respuesta.name} {respuesta.surname} {alias}"
        
    def walk(self):
        print(f"{self.fullname} Esta caminado")

respuesta = Person("Montes", "Andres", "DJ Caled")
print(respuesta.fullname)

respuesta.walk()

other_person = Person(name="Andres", surname="Montes")
print(other_person.fullname)
other_person.walk()
