#POR LA COMPRA DE BALON DE GAS, SERA PREMIADO
#MOSTRAR EN PANTALLA SE LLEVA UN PLATO SOPERO
cant_bgas=0
cant_bgas_invalidas=(cant_bgas<4)

while(cant_bgas_invalidas):
    cant_bgas=int(input("ingresar cant balones de gas:"))
    cant_bgas_invalidas=(cant_bgas<4)
#fin_while
print("premiado")
print("tiene de regalo un plato sopero")
