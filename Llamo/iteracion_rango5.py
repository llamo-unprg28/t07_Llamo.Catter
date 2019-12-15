#determinar si de 12 alumnos da examen sustituto

for i in range(4):
    prom=float(input("ingrese promedio: "))
    if(prom>8 and prom<10.5):
        print("examen sustituto")
    else:
        print("no da examen sustituto")
