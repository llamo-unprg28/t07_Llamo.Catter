#de un numero de personas cuantas son mayores y menores de edad
num=int(input("ingrese cantidad de personas: "))
for i in range(num):
    edad=int(input("ingrese edad: "))
    if(edad>=18):
        print("mayor de edad")
    else:
        print("menor de edad")
