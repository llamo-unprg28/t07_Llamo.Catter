#PROGRAMA PARA MOSTRAR EN PATALLA LOS DECODIFICADORES "VEN ESTOY TRISTE"
msg=""
import os

msg=str(os.sys.argv[1])

for letra in msg:
    if (letra=="1"):
        print("VEN")
    if(letra=="2"):
        print("ESTOY")
    if(letra=="3"):
        print("TRISTE")
    #fin_if
#fin_for
