#ingresar 3 notas y hallar su promedio si el promedio es mayor o igual a 12 mostrar aprobado
#sino mostrar desaprobado
suma=0
for i in range(1,4):
    nota=int(input("ingrese notas: "))
    suma+=nota
prom=suma/3
if(prom>=12):
    print(prom,"aprobado")
else:
    print(prom,"desaprobado")
