"""
   Realizar un programa que calcule
   el total de un ticket, tomando
   en cuenta el iva y la propina.
"""
subtotal_txt = input("SUbtotal (MXM):")
iva_txt = input("IVA (%) ejemplo: 16: ")
tip_txt = input("Propina (%) Ej: 10: (negativo para doña tota): ")

try:
    subtotal = float(subtotal_txt)
    iva = float(iva_txt)/100
    tip = float(tip_txt)/100
except:
    print("No te pases de lansa morro 6767676767676767")
    raise SystemExit(1)

iva_account = subtotal*iva
tip_account = subtotal*tip
total = subtotal + iva_account + tip_account

print("subtotal:", subtotal)
print("Propina:", tip)
print("Iva:", iva)
print("Total:", total)

