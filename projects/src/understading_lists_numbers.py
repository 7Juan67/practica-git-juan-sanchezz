# Listas de numero 
"""
   Las listas tambien pueden almacenar numero, Python
   ofrece vaias heramientas que ayudan a trabajar
   eficientemente con listas de numeros.
"""
# Metodo build-in range()
"""
   El metodos range() nos ayuda a crear facilmente
   series de numeros.
"""
for value in range(1,5):
    print(value)

# Crear lista de numeros utilizando range
numbers = list(range(1,500,200))
print(numbers)

# lista de numeros pares
even_number = list(range(-10,10,15))
print(even_number)

even_number = list(range(0,10,-2))
print(even_number)