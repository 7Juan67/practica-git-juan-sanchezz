# Diccionarios simple
alien_0 = {"color": "green", 'points': 5}

# Diccionario vacio
alien_1 = {}

# El diccionario mas simple
alien_2 = {"color": "verde"}

# Accedar a los elementos de un diccionario
print(f"tu alien es de color: {alien_0['color']}")
print(f"si desvives al alien 0 se te otorga: {alien_0['points']-2}")

# Agregar elementos a un diccionaio
alien_0["x_position"] = 25
alien_1["y_position"] = 0

print(alien_0)


# Modificando un valor en un diccionario
alien_0["y_position"] = 80
print(alien_0)

# eliminando un elemento de un diccionario
del alien_0["points"]
print(alien_0)

# Dioccionarios para objetos (elementos) similares
favorite_lenguages = {"jen": "python", "sara": "c", "eduard": "ruby", "pill": "python"}

# Looping thoug all key-values pairs
# Looping a traves de todos los pares llave-valor
user_0 = {
    "username": "Carly",
    'firstname': "Tovar",
    "lastname": "Garcia",
    'age': 34,
    "birthday": '6-feb'
}

print(" looping a traves de los pares llave, valor")
for key, value in user_0.items():
    print("key:", key)
    print("value:", value)

print(" looping a traves de las llaves")
for key in user_0.keys():
    print("key:", key)

print(" looping a traves de los valores")
for key in user_0.keys():
    print("values:", value)