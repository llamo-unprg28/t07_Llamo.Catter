# si al ingresar la contraseña incorrecta a tu celular no te permitira avanzar.
# si es correcta sera vienvenido a su sistema
contraseña=""
contraseña_invalida=(contraseña!= "4321")

while (contraseña_invalida):
    print("vuelva a intentarlo")
    contraseña=input("ingrese contraseña:")
    contraseña_invalida=(contraseña!="4321")
#fin_while
print("bienvenido a su sistema ")



