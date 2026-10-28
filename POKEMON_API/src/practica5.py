"""
   Programa para calcular el indice de 
   masa corporal de una persona

   weigth: peso de la persona
   heigth: altura de la persona
"""
weight_txt = input("Peso (KG)")
height_txt = input("Alutra (mts)")

try:
    weight = float(weight_txt)
    height = float(height_txt)
    imc = weight / (height ** 2)
except:
    print("datos lo validos")
    raise SystemExit(1)

print(f"TU indice de masa corporal es {imc}")