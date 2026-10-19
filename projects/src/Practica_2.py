"""
   Ejercicio

   Realizar un programa que determine el costo
   de un boleto a partit de las siguentes condiciones:

   -costo para una persona menor o igual a 4 años: gratis
   -costo para cuuya pesona cuya edad es mayor a 4 años
   pero menor o igual a 18: $200
   -costo para uan persona cuya edad se mayor a 18: $500
"""

age = input(" Ingresa tu edad ")
# print(type(age)) # str
age = int(age)
# print(type(age)) # int casos normales y casos borde

print("\n \t Esto se realiza con el if normal ")

if age <= 4:
    cost = 0

if age > 4 and age <= 18:
    cost = 200

if age > 18:
    cost = 500

# print(f"El costo de tu boeto es {cost}")

# if-elif-else

if age <=4:
    cost_ = 0
elif age > 4 and age <=18:
    cost = 200
elif age > 18 and age <=90:
    cost = 500
elif age >=90:
    print(f"{cost} Ya estas bien ruco")
else:
    cost = 0
# cual el elif tiene 0 el else no se contempla
print(f"Costo (if-elif-else): {cost}")