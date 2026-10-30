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
    print(f"TU indice de masa corporal es {imc}")
except ValueError:
    print("Datos no validos Ej, peso 70.5, altura 1.75")
except ZeroDivisionError:
    print("La altura debe ser diferente de cero")
except Exception:
    print(Exception)

print(f"TU indice de masa corporal es {imc}")