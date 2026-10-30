"""
   while condition:
    acitons           condition TRUE


   while - sentinel 

   while True:
        print("Hola")
   Realizar un programa que capture el 
   importe y que acumule todos estos importes
   en una variable.
"""
sum = 0.0

message = """
    Sistema gestor de acumulacion de valores.
    La creatividad está en tus manos.

    En todo momeento si queires salir del programa 
    puedes tipear q, e, quit, exit

    ingresa un valor:
"""

while True:
    value_txt = input(message)

    if value_txt == 'quit' or \
       value_txt == 'exit' or \
       value_txt == 'e' or value_txt == 'q':
        break


    value = float(value_txt)
    sum += value # Estructura acumulada
print(f"Tu total acumulado es: {value}")

"""
   Tarea - Realizar un programa que 
   apture los importes intriduccidos por usuario

   El programa debe
        a) contabilizar cuantos importes ha intrucido el usaurio
        b) caumular los importes que ha introducido el usuario.
        c) establecer el maximo y el minimo de los valores introduccios
        d) caluclar el promedio de los valores introduccidos

Despues de que el usuario decida terminar el programa se
deben mostrar datos, es decir,

    i)el contador de numeros ingresados
    ii) el acumulado de los numeros ingresados
    iii) el promedio
    i) el minimo valor ingresado 
    v) el maximo valor ingresado
"""