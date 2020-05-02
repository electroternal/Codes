import os
# os.system('cls')

print("╔═══════════════════════════════════════════════════════════╗")
print("║ Bienvenidos al sistema de Registro y gestión de pacientes ║")
print("╚═══════════════════════════════════════════════════════════╝")

input("Press Enter")
os.system("cls")

# **********************
# * Variables Globales *
# **********************

running = True
validated = False
database = list()

def show_menu():
    print("╔═══════════════════════════════════════════════╗")
    print("║ Seleccione una de las opciones a continuacion ║")
    print("╚═══════════════════════════════════════════════╝")
    print("")
    print("\t \t «««« 1 »»»» Cargar paciente")
    print("\t \t «««« 2 »»»» Buscar paciente")
    print("\t \t «««« 3 »»»» Listar pacientes")
    print("\t \t «««« 4 »»»» Salir")
    print("")
    response = input("Escriba aquí => ")
    return response

def response_validate(r):
    validated = False
    num_res = 0
    if response.isdigit():
        num_res = int(response)
        if num_res > 0 and num_res < 5:
            msg = "está en rango"
            validated = True
        else:
            msg = "está fuera de rango"
    else:
        msg = "Entrada en Error"
    return validated,num_res,msg


# ******************
# * Loop Principal *
# ******************

while running:
    response = show_menu()
    validated,num_res,msg = response_validate(response)
    if validated:
        if num_res == 1:
            name = input("Ingrese el Nombre del Paciente => ")
            history = input("Ingrese el historia clínica del paciente => ")
            paciente = {"nombre":name, "historia":history}
            database.append(paciente)
            print("Paciente ingresado")
            print("")
            input("Press Enter")
            os.system("cls")

        elif num_res == 2:
            name = input("Ingrese el Nombre del Paciente => ")
            finder1 = False
            finder2 = False
            for x in range(len(database)):
                    if database[x]["nombre"].lower() == name.lower():
                        print("")
                        print("*****ENCONTRAMOS AL PACIENTE *****")
                        print("El nombre del paciente es => ", database[x]["nombre"], "y su historia es => ", database[x]["historia"])
                        print("")
                        finder1 = True
                        input("Press Enter")
                        os.system("cls")
                    else:
                        finder2 = True

            if finder1 == False and finder2 == True:
                print("")
                print("*****Lo sentimos pero el paciente ingresado no está en el sistema*****")
                print("")
                input("Press Enter")
                os.system("cls")

        elif num_res == 3:

            print("╔═══════════════════════════════════════════╗")
            print("║ LISTA DE PACIENTES POR NOMBRE E HISTORIA  ║")
            print("╚═══════════════════════════════════════════╝")
            print("")
            for x in range(len(database)):
                print("Nombre => ", database[x]["nombre"], "\t | \tHistoria => ", database[x]["historia"])
                end_For = x
            input("Press Enter")
            os.system("cls")
            
        else:
            print("")
            running = False
    else:
        print("╔═════════════════════╗")
        print("║ OPCIÓN INCORRECTA   ║")
        print("╚═════════════════════╝")
        input("Press Enter")
        os.system("cls")

print("╔═════════════════════╗")
print("║ PROGRAMA FINALIZADO ║")
print("╚═════════════════════╝")


