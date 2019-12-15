#ingresar los sueldos de n trabajadores y calcular su sueldo de acuerdo a las horas trabajadas y la
#tarifa de pago que es 20 soles

n=int(input("ingrese cantidad de trabajadores: "))
for i in range(n):
    ht=int(input("ingrese horas trabajadas: "))
    if(ht==0):
        print("sueldo: 0")
    else:
        sueldo=ht*20
        print("su sueldo es: ",sueldo)
