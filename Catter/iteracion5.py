#PROGRAMA PARA MOSTRAR EN PATALLA LOS DECODIFICADORES "TENGO MUCHA HAMBRE"
msg=""
import os

msg=str(os.sys.argv[1])

for letra in msg:
    if (letra=="?"):
        print("TENGO")
    if(letra=="="):
        print("MUCHA")
    if(letra=="!"):
        print("HAMBRE")
    #fin_if
#fin_for
