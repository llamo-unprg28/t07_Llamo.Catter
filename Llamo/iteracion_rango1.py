#dada una cantidad ingresada de clientes registrar su compra y calcular el pago si es mayor o igual a 100
#dscto del 10%

n=int(input("ingrese cantidad de clientes: "))

for i in range(n):
    compra=float(input("ingrese compra: "))
    if(compra>=100):
        pago=compra-compra*0.10
        print("el monto a pagar es: ",pago)
    else:
        print("el monto a pagar es: ",compra)
