# Input - Sirve para realizar entradas de usuario
"""
   Metodo build-in input
   input(argumento) - argumento (str): mensaje al usuario

   input retorna un string

"""

wercolme = """s

"""


firstname = input("escribe tu nombre")
middlename = input("Escribe tu segudno nombre")
lastname = input("Esribe tu apellido (paterno y materno")

fullname = f"{firstname}, {middlename}, {lastname}"
print(fullname.title())
