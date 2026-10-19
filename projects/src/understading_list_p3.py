# Trabajando en listas
print("\n \t El dia de hoy aprender a trabajar en listas".title())

magicians = ['harry', 'ron', 'hermione', 'snape']
print(magicians)

# Imprinir solo el contenido escojido de la lista
print(magicians[0], magicians[2])

# ciclo for
for magician in magicians:
    print(magician)

# A esto se le conoce como looping
# Ahora vamos a imprimir un mensaje para cada mago
for magician in magicians:
    print(f"{magician.title()} ese fue un gran echiso")
    print(f"No puedo esperar a ver el siguente hechizo, {magician.upper()}")
print("Gracias a todos, fue un gran espectaculo")

# Indentaciopn
"""
   Pyton utiliza la identacion para determinar 
   cuando una linea de codigo esta conectada a la
   lnea de codigo anterior

   basicamente, se utiliza 4 espacios en blanco para 
   obligarnos a escribir codigo ordenado y estructurado
"""

# print("\n \t no olivdemos identar - Traceback Identation Error ")

magicians = ["alice", "david", 'caroline']
# for magician in magicians:
# print(magician) # Identacion error

# Error de logica - logic error . IdentationError
for magician in magicians:
    print(magician)
print(f"No puedo esperar a ver el siguente truco {magician}")

# Identacion incesesaia 
message = "Hello pythhon world!"
    # print(message)

# No olvidar los dos puntos - Syntax Error
# for magician in magicians
    # print(magician)