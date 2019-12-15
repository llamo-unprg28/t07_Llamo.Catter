#SI COMPRAN MAS DE 10 CHOCOTEJAS SE LLEVA DOS DE REGALO
#MOSTRAR EN PANTALLA DOS CHOCOTEJAS GRATIS
cant_chocotejas=0
cant_chocotejas_invalidas=(cant_chocotejas<10)

while(cant_chocotejas_invalidas):
    cant_chocotejas=int(input("ingresar cant chocotejas:"))
    cant_chocotejas_invalidas=(cant_chocotejas<10)
#fin_while
print("dos chocotejas gratis")
