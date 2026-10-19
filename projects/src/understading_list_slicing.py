players = ["charly", "juan", "iancarlo", "lizandro"]
print("lista original", players)

# slicing 
print(players[0:2]) # ["charly", "juan"] 

# El slicing me permite trabajar con un grupo
# especifico de una lista: al resultado se le conoce como
# "un slice"

print("1:4", players[1:4]) # ["juan", "iancarlo", "lizandro"]
print(":3", players[:4]) # ["charly", juan", "iancarlo"]
print("2:", players[2:]) # ["iancarlo", "lizandro"]
print("[-3:]", players[-3:]) # ["juan", "iancarlo", "lizandro"]

# players = ["charly", "juan", "iancarlo", "lizandro"]
print("Casos especiales: ")
print(players[1:6]) # ["juan", "iancarlo", "lizandro"]
print(players[6:1])
print(players[:0])

# Loping through a slice3
print("looping throung a slice")
student = ["raul", "juan", "iancarlo", "lizandro"]

# slicing [:]

for student in student [2:4]:
    print(f"El estudiante {student}, va a pasar la materia")

print(student)

# ¿Cómo podemos copiar una lista?
my_food = ["pizza", "tacos", "flautas"]
my_food_friends = my_food # Manera erronea e copiar una lista

# tres maneras de cpiar una lista
# metodo 1 - usando slicing
my_food_friends_2 = my_food[:]
# metodo 2 - utilizando el metodo de las listas .copy
my_food_friends_3 = my_food.copy()
# metodo 3 utilizando el metodo build-in list()
my_food_friends_4 = list(my_food)
