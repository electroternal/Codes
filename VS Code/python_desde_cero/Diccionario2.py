
paciente1 = {"nombre":"Juan", "edad":50, "peso":85.4, "fuma":False}
paciente2 = {"nombre":"Pepito", "edad":30, "peso":90.5, "fuma":True}
paciente3 = {"nombre":"Maria", "edad":23, "peso":75.2, "fuma":False}

pacientes = [paciente1, paciente2, paciente3]

for x in range(len(pacientes)):
    print("")
    print("################################################")
    print("################# Paciente #", x+1, "#################")
    print("################################################")

    for Clave, Valor in pacientes[x].items():
        notacion = ""
        if Clave == "edad" and Valor < 35:
            notacion = "👍"
        print("Clave => ", Clave, " \t | \t Valor =>", Valor, notacion)
