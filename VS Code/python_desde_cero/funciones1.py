
def calcula(numero1, numero2, opIngresado):
    if opIngresado == "sumar" or opIngresado == "suma":
        resultado = numero1 + numero2
    elif opIngresado == "restar" or opIngresado == "resta":
        resultado = numero1 - numero2
    elif opIngresado == "multiplicar" or opIngresado == "multiplica":
        resultado = numero1 * numero2
    elif opIngresado == "dividir" or opIngresado == "divide":
        if numero2 == 0:
            resultado = "Error"
        else: 
            resultado = numero1 / numero2
    # lo importante es poner el return para hacer que calcula se convierta en lo que se calculó en el resultado
    return resultado

opIngresado = input("¿Que quieres hacer? \n ¿Sumar, Restar, Multiplicar o Dividir? \n Escribe aquí => ")
opIngresado = opIngresado.lower()
numero1 = float(input("Escribe aquí tu primer numero => "))
numero2 = float(input("Escribe aquí tu segundo numero => "))

# para llamar la función y para que te devuelva el resultado tienes que completar todas las partes de la funcion
# para poder darle los datos a calcular, si es un dato uno si son 3 son 3
el_calculo = calcula(numero1, numero2, opIngresado)

print(el_calculo)
    



