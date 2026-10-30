"""
   Vamos a realizar un programa que pregunte 
   el nombre de una persona y su edad
"""
name = input("¿Comó te llamas? ")
age_txt = input("¿Cual es tu edad?")


try:
    age = int(age_txt)
    print(f"hola {name}, Tienes {age_txt} años.")
    print("En corea tendrias,", age+1)
except:
    print("La edade que introduciste no e sun numero entero")



