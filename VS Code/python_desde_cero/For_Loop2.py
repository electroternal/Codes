import os

print("***Inicio de Programa para ingresar participantes de la maratón***")
print("")
num_max_users = input("Ingrese la cantidad maxima de participantes => ")
print("")
print("****************************************************************")
print("**Gracias, la cantidad maxima de participantes está almacenada**")
print("****************************************************************")
print("")
anykey = input("Enter para continuar")
os.system('cls')

for x in range(int(num_max_users)):
    print("Para participar en la maratón complete lo siguiente:")
    print("")
    name = input("Ingrese su nombre => ")
    email = input("Ingrese su email => ")
    print("")
    print("Gracias ",name, ", su email es ",email)
    print("Escriba SI o NO para inscribirse al maratón")
    respuesta = input()
    respuesta = respuesta.lower()

    if respuesta == "si":
        print("")
        print("****************************************")
        print("**Gracias su inscripción está guardada**")
        print("****************************************")
        print("")
        print(x)
        anykey = input("Enter para continuar")
        os.system('cls')

    else:
        print("")
        print("***********************")
        print("**Operación cancelada**")
        print("***********************")
        print("")
        anykey = input("Enter para continuar")
        os.system('cls')


print("Usuarios Maximos Alcanzados")
anykey = input("Enter para continuar")
os.system('cls')