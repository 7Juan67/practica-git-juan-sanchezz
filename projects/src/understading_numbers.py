# Números
# Enteros - Integers

"""
   Los números enteros los podemos
   Sumar (+), restar (-) , multiplicar(*)
   y dividir (/).
"""
print(2+3)
print(3-2)
print(2*3)
print(3/2)
number_1 = 5
number_2 = 10
print(number_1+number_2)

# Multiplicar *
# Dividir /
# Division entera //
# Potencias **n
print(3**2) # 3 2
print(3**3) # 3 2
print(10**6) # 10 6
print(10%2) # Modulos (mod)
age = 34
print(age)
name = "Charly mercury"
print(name, age)

# Floats
"""
   Python llama floats a cualquier numero 
   con punto decimal
"""
print(0.1+0.1)
print(0.2+0.2)
print(2*0.1)
print(2*0.2)

# Imprimir la edad de alguien
age = 34 # Variable del tipo entero
# message = "Charlytiene" + age + "años." (Error)
message = "Charly tiene " + str(age) + " años."
message_f = f"CHarly tiene llave age llave años."
print(message)

"""
   TYpeError: Python no puede reconocer el tipo
   de informacion que se esta utilizando.

   En etse caso no se puede concatenar
   ints a strigs
"""

print(type(age))
print(type(0.1))
print(type(message_f))