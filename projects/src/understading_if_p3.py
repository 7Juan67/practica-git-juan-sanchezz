guisos = ["salsa verde", 'deshebrada', "nopales"]

if "salsa verde" in guisos:
    print("hay salsa verde")
elif "deshebrada" in guisos:
    print("hay deshebrada")
elif "npales" in guisos:
    print("hay de nopales")

# lista vacia 
guisos_2 = []
if guisos:
    for guiso in guisos_2:
     print(guiso)
else:
    print("no hay guisos")

guisos_disponibles = ["salsa verde", "desehebrada", "picadillo", "asado"]
guisos_a_ordenar = ["barbacoa", "deshebrada", "cabrito"]

for guiso in guisos_a_ordenar:
    if guiso in guisos_disponibles:
        print("si hay de ese guiso")
else:
    print("una disculpa no tenemos de ese guiso")
print("final")