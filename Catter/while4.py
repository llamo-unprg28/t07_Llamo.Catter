#LAS PERSONAS QUE TENGAN LA EDAD DE ENTRE 15 Y 22 AÑOS
#MOSTRAR EN PANTALLA GRACIAS POR SU VISITA
# PUEDES INCRIBIRTE EN EL FUTBOL-CLUBFC
edad=0
edad_invalida=(edad<15 or edad>22)
while(edad_invalida):
    edad=int(input("ingresar edad:"))
    edad_invalida=(edad<15 or edad>22)
#fin_while
print("gracias por su visita")
print("puedes incribirte en el futbol-clubFC ")

