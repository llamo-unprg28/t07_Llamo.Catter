#PROGRAMA PARA MOSTRAR EN PATALLA LOS DECODIFICADORES "1,3,5"
msg=""
import os

msg=str(os.sys.argv[1])

for letra in msg:
    if (letra=="L"):
        print(1)
    if(letra=="E"):
        print(3)
    if(letra=="P"):
        print(5)
    #fin_if
#fin_for
