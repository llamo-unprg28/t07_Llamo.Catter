#de aula determinar cuantos son hombres y cuantos son mujeres
conth=0
contm=0
n=int(input("ingrese cantidad de alumnos: "))
for i in range(n):
    sexo=int(input("ingrese sexo 1.hombre 2.mujer: "))
    if(sexo==1):
        conth+=1
    else:
        contm+=1
print("cantidad de hombres: ",conth)
print("cantidad de mujeres: ",contm)
