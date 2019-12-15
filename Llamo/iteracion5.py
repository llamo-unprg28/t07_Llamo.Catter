#PROGRAMA PARA MOSTRAR EN PATALLA LOS DECODIFICADORES "APROBE LEP 2"
msg=""
import os

msg=str(os.sys.argv[1])

for letra in msg:
    if (letra=="*"):
        print("APROBE")
    if(letra=="$"):
        print("LEP")
    if(letra=="/"):
        print("2")
    #fin_if
#fin_for
