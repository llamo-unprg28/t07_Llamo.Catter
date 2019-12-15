#PROGRAMA PARA MOSTRAR EN PATALLA LOS DECODIFICADORES "NOS VEMOS EN EL PARQUE"
msg=""
import os

msg=str(os.sys.argv[1])

for letra in msg:
    if (letra=="0"):
        print("NOS VEMOS")
    if(letra=="1"):
        print("EN EL")
    if(letra=="2"):
        print("PARQUE")
    #fin_if
#fin_for
