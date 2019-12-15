#PROGRAMA PARA MOSTRAR EN PATALLA LOS DECODIFICADORES "estas aprobado con 11"
msg=""
import os

msg=str(os.sys.argv[1])

for letra in msg:
    if (letra=="="):
        print("estas")
    if(letra=="!"):
        print("aprobado")
    if(letra=="¿"):
        print("con 11")
    #fin_if
#fin_for
