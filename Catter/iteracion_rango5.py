#factorial de un numero ingresado
factorial=1
num=int(input("ingresa un numero: "))
for i in range(1,num+1):
    if(num>0):
        factorial*=i
if(num<=0):
    print("numero no valido")
else:
    print(factorial)
