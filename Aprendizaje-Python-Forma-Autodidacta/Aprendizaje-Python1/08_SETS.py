### Sets ###

my_Set = set()
my_other_Set = {}

print(type(my_Set))
print(type(my_other_Set))

my_other_Set = {"Andres", "Montes", 19}
print(type(my_other_Set))

print(len(my_other_Set))

my_other_Set.add("Indil04")
print(my_other_Set)

my_other_Set.add("Indil04")
print(my_other_Set)
#Sintaxis para comprovar si algo existe en un set
print("Andres" in my_other_Set)
print("Andrei" in my_other_Set)

my_other_Set.remove("Indil04")
print(my_other_Set)

my_other_Set.clear()
print(len(my_other_Set))
#Esto elimina el set del todo
#del my_other_Set
#print(my_other_Set)

my_Set = {"Andres", "Montes", 19}
my_list = list(my_Set)
print(my_list)
print(my_list[0])

my_other_Set = {"Kitlin", "swift", "Python"}

my_new_set = my_Set.union(my_other_Set)
print(my_new_set.union(my_new_set).union({"Java", "C++"}))

print(my_new_set.difference(my_Set))