#PROGRAMA PARA MOSTRAR EN PATALLA LOS DECODIFICADORES "AYUDAME ESTOY EN  PELIGRO"
msg=""
import os

msg=str(os.sys.argv[1])

for letra in msg:
    if (letra=="A"):
        print("¡AYUDAME!")
    if(letra=="B"):
        print("ESTOY")
    if(letra=="C"):
        print("EN PELIGRO")
    #fin_if
#fin_for
