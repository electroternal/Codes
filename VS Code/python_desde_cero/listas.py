
frutas = ["pera", "manzana", "guineo", "china", "melón"]
numero = 0

# .pop es para eliminar algo en una lista
# append es para añadir algo al final
# frutas[2] = "coco"      es para cambiar lo que hay en la posición 2 por coco
frutas.pop(3)
frutas.append("tamarindo")
frutas[3] = "coco"
frutas.remove("manzana")

# para saber cual es la cantidad en esta lista
for x in frutas:
    numero += 1

print(numero)
print(frutas)