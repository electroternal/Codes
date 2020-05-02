print("Vamos a buscar el promedio de tus notas \n")
exam1 = input("Tu examen # 1 => ")
exam2 = input("Tu examen # 2 => ")
exam3 = input("Tu examen # 3 => ")
exam4 = input("Tu examen # 4 => ")
exam5 = input("Tu examen # 5 => ")

exam1 = int(exam1)
exam2 = int(exam2)
exam3 = int(exam3)
exam4 = int(exam4)
exam5 = int(exam5)

examTotal = exam1 + exam2 + exam3 + exam4 + exam5

examPromedio = examTotal / 5

examPromedio = str(examPromedio)
print(" ")
print("Tienes un promedio de " + examPromedio + " en tus calificaciones \n")
print("cheka tu mismo a ver si estás jodío")