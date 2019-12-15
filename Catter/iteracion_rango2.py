#dada una cantidad de alumnos determinar cuantos son mayores a 15 y cuantos son menores
cont=0
cont1=0
num=int(input("ingrese cantidad de alumnos: "))
for i in range(num):
    edad=int(input("ingrese edad 11-17 : "))
    if(edad>=15):
       cont+=1
    else:
        cont1+=1
print("mayores que 15: ",cont)
print("menores que 15: ",cont1)
