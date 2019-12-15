#mostrar en pantalla no eres jhon al ingresar el nombre, si pasa de los 3 intentos mostrar un mensaje
quien=""
i=0
while i < 3:
    i=i+1
    nombre=input("introduce tu nombre:")
    if quien !=nombre:
        print("no eres jhon")
    else:
        print("bienvenida jhon")

else:
    print(" excedio el numero de intentos")

