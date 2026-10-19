# Agregando elementos a una lista 
motorcycles = ['honda', 'mortalica', 'yamaha']
print(motorcycles) # ['honda', 'mortalica', 'yamaha']

#metodo append - agrega elementos a la lista
motorcycles.append("kawasaki") # ['honda', 'mortalica', 'yamaha', 'kawasaki']

"""
   El metodo append ayuda a crear listas
   facilmente de manera dinamica
"""

motorcycles_2 = [] # Lista vacia
print(motorcycles_2)

motorcycles = "ducati"
motorcycles_2.append(motorcycles) # 1 elemento
motorcycles_2.append("yamaha") # 2 elemento
motorcycles_2.append("suzuki") # 3 elemento
print(motorcycles_2)
motorcycles = "charly"
print(motorcycles_2)
motorcycles_2.append(motorcycles)
print(motorcycles_2)

# EL metodo .insert() nos ayuda a agregar elementos
# a una lista en in indice especifico 
print('\n \t aqui apendi a usar el metodo insert')
motorcycles_3 = ["honda", 'yamaha', "suziki"]
print("\n Lista original")
print(motorcycles_3)
motorcycles_3.insert(0, "ducati")
print("Lista despues del metodo insert")
print(motorcycles_3)

## Metodo .pop() Elimina el ultimo elemento de una lista,
# Pero nos permite utilizar el elemento despues de eliminarlo
motorcycles_4 = ['honda', 'suzuki', 'hd', 'mortalica']
print(motorcycles_4)
deleted_motorcycle = motorcycles_4.pop()
print(f"Tu motocicleta borrada es: {deleted_motorcycle}")
print(motorcycles_4)

# Sé puede eutilizar tambien para eliminar un elemento especifico.
print('\n \t aqui apendi a utilizar el metodo remove')
motorcycles_5 = ['honda', 'suzuki', 'hd', 'mortalica']
print(motorcycles_5)
motorcycles_5.pop(1)
print(motorcycles_5) # lsita sin honda


# Metodo .remove(), permite elliminar elementos por su valor.

motorcycles_6 = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles_6)
motorcycles_6.remove('yamaha')
print(motorcycles_6)

# Ordenar listas 
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() # Ordenar la lista de manera permanente 
# Argumento opcional de .sort(reverse=true)
print(cars)
# Tarea estudiar el emtodo de la slsiats reverse
# estudiar metodos build-in: sorted(), len().
matriz = [["limon", "lizandro"]["juan", "charly"]]
print(matriz[1][1])