#PROGRAMA PARA MOSTRAR EN PATALLA LOS DECODIFICADORES "VAMOS A TOMAR UN PAR DE CHELAS"
msg=""
import os

msg=str(os.sys.argv[1])

for letra in msg:
    if (letra=="X"):
        print("VAMOS")
    if(letra=="Y"):
        print("A TOMAR")
    if(letra=="Z"):
        print("UN PAR")
    if(letra=="1"):
        print("DE CHELAS")
    #fin_if
#fin_for
