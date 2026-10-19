# conbinacion o concatenacion de STRINGS
first_name = 'charly'
last_name = "mercury"
full_name = first_name + " " + last_name # esto es una concatentacion
print(full_name)

print("Hola".title(), "Carlos" + " " + "Tovar", first_name.title()+" "+last_name.title())


message = "¡hola," + full_name.title() + "!"
print(message)

# whiteSpace
"""
   WhiteSpace se refiere a cualquier String
   (caracter) que no se imprime, es decir,
   un espacio (" "), tabuladores (\t) y
   finales de linea (\n).

   Los Whitespace se utiliza comunmente para
   organizar las salidas de texto a usuario 
   de tal manera que sea mas amigable de leer
   o ver para los usuarios
"""

print("Python")
print("\tPytohn")
print("\t\tPython")
print("Lenguajes: \n Pytohn \n C \n JavaScripts")

# f-stirngs
famous_person = "Charly mercury"
message = f"{famous_person} una vez dijo: python es amor"
print(message)

qoute = "Python is in the air"
message_2 = f"{famous_person} una vez dijo {qoute}"
print(message_2)