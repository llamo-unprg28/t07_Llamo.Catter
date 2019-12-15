#se registra un monto mensual hallar el mayor y menor monto
menor=100000
mayor=0
for i in range(12):
    monto=float(input("ingrese monto: "))
    if(monto>mayor):
        mayor=monto
    if(monto<menor):
        menor=monto
print("mayor monto: ",mayor)
print("menor monto: ",menor)
