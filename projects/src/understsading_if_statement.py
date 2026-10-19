# if statement
cars = ["audi", " bmw", "subaru", "toyota"]

for car in cars:
    if car == "audi":
        print(car.upper())
    else:
        print(car)

# El condicional o la condition
# EL condicional es el corazon del if 

# Condicional verdarero
# Condicional = True
truck = "ford"
print(truck == 'ford') # Imprme true
print(truck == 'lenovo') # imprime false

print(truck == 'Ford'.lower()) # Imprime true porque el .lower() pone todo en minisculas 

number = 67
print(number == 67)

# Condicional de desigualdad
print(truck!='audi') # true por que pregunta si audi es diferente a la variable 
print(truck!='ford') # false pregunta si truck es diferente a la variale truck y no lo se porque lo tiene la variable 

#  Comparaciones numericas
age = 34
print(age == 34) # true
print(age == 10) # false

answer = 17
if answer != 42:
    print("esa no es la respuesta correcta")

# conector menor que < 
print("conecotres < > <= >=")
age = 19
print(age < 21) # true
print(age <= 21) # true
print(age > 21) #  false
print(age >= 21) # false

# Multiple conditions 
age_0 = 22
age_1 = 18
print("Multiple Conditions")
print("Operacion AND")
print(age_0>=21 and age_1>= 21) # True
print(age_0>=21 and age_1>= 18) # True

print("\n \t Operacion OR")
print(age_0>= 21 or age_1>=21) # true

# ¿Cómo saber si un elemento esta en una lista
food = ["Chilaquiles", 'Flautas', "gorditas", "tamales"]
print("\n nopales esta en la lista de comida")
print("noaples" in food)
print("\n ¿gorditas esat en la lista?")
print("gorditas" in food)

banned_user = ["andrew", "carolina", "david"]
user = "marie"
print(user not in banned_user)