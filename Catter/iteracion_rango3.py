#determinar si un numero ingresado es primo o no

cont=0
num=int(input("ingrese numero: "))

for i in range(1,num+1):
    if(num%i==0):
        cont+=1
if(cont>2):
    print("no es primo")
else:
    print("es primo")
