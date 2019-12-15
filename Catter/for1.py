#mostrar en la pantalla si el correo eletronico es correcto sino sera incorrecto en el estrin
#verificando que el email este escrito

email=False
miEmail=input("introduce tu direccion de email: ")
for i in (miEmail):
    if(i=="@"):
        email=True
if email==True:
    print("email es correcto")
else:
    print(" email incorrecto")
    #fin_if
#fin_for
