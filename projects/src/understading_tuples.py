"""
   TUPLAS 
   
   Las tuplas son listas de elementos que no cambian de tamaño
   Las uplas son listas inmutables

   Sé utiliza los parentsis () para definir una tupla.

   Ejemplo:
       si tenemos un rectangulo (laroh, ancho) que siempre va
       a tener cierto tamaño, podemos asefurar que si dimensiones 
       no va a cambiar si colocamos sus valores en una tupla
"""

dimensiones = (200, 50) # 200 de largo x 50 de ancho
print(dimensiones)

# vamos a imprimir elementos de una tupla 
# Se realiza de la misma forma que con una 
print(dimensiones[0])
print(dimensiones[1])

# print(dir(dimensiones))

# Vamos a modificar el valor de una lista
names = ["Carlos", "charly", "juan", "wendy"]
print(names)
names[0] = "mercury"
print(names)

# dimensiones[0] = 500 Esta operacion no esta permitida

# looping throgh a tuple
for dimension in dimensiones:
    print(dimension)

"""
   No podemos modificar una tupla
   lo que si podemos hacer es cambiar
   la asignacion de una variable que 
   almacena una tupla
"""

dimensiones = (500, 1000)
print("TUpla original", dimensiones)

# lista
# dimensiones_2 = [200, 50]
# print(dir(dimensiones_2))

# dimensiones_3 = "charly"
# print(dir(dimensiones_3))

# age = 18
# print(dir(age))

# Tipos de datos booleanos
answer = True
print(answer)
# print(dir(answer))

# zl, regulador de voltaje, bateria de 12v, 