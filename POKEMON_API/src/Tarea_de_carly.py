#-----------------------------------#
# Sistema gestor de acumulaciones
#-----------------------------------#

suma = 0.0
contador = 0
maximo = None
minimo = None

message = """
    ==========================================
       SISTEMA GESTOR DE ACUMULACION DE VALORES
    ==========================================

    Introduce los importes que quieras acumular.

    Para terminar el programa escribe:
    quit, exit o e
    ==========================================
"""

print(message)

while True:
    value = input("Ingresa un valor: ")

    if value == 'quit' or value == 'exit' or value == 'e':
        break

    value = float(value)

    # Acumulador
    suma += value

    # Contador
    contador += 1

    # Maximo y minimo
    if maximo is None or value > maximo:
        maximo = value

    if minimo is None or value < minimo:
        minimo = value

# Mostrar resultados
print("\n========== RESULTADOS ==========")

print(f"Cantidad de importes ingresados: {contador}")
print(f"Importe acumulado: {suma}")

if contador > 0:
    promedio = suma / contador

    print(f"Promedio: {promedio}")
    print(f"Valor minimo: {minimo}")
    print(f"Valor maximo: {maximo}")
else:
    print("No se ingresaron valores.")

print("================================")
print("Programa terminado.")