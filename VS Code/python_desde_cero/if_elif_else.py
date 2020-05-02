
deseos = str(input("¿que quieres para comer? = > "))

inventario = int(input("cuantas " + deseos + "s quieres? => "))

if deseos == "manzana":
    if inventario == 1:
        print("ok, ya mismo te entrgan la manzana.")
    elif 1 < inventario <= 5:
        # hay que cambiar el inventario de int a string para que no de error cuando se concatena en el siguiente print
        inventario = str(inventario)
        print("ok, ya mismo te entrgan las " + inventario + " manzanas.")
    else:
        print("No es posible entregar esa cantidad de manzanas")

elif deseos == "pera":
    if inventario == 1:
        print("ok, ya mismo te entrgan la pera.")
    elif 1 < inventario <= 5:
        # hay que cambiar el inventario de int a string para que no de error cuando se concatena en el siguiente print
        inventario = str(inventario)
        print("ok, ya mismo te entrgan las " + inventario + " peras.")
    else:
        print("No es posible entregar esa cantidad de peras")

else:
    print("lo sentimos, pero no hay de eso que quieres")