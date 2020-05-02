# import matplotlib as plt
# import numpy as np
# from scipy import misc
# import matplotlib.pyplot as plt
# import urllib.request
# from PIL import Image

# from stl import mesh
# from python_utils import converters

import time

t = time.process_time()

fibo_start_1, fibo_start_2 = input("ingrese dos numeros separados por un espacio => ").split()
num = int(input("ingrese el numero de operaciones a calcular => "))

# print(type(num), type(fibo_start_1), type(fibo_start_2))
fibo_start_1 = int(fibo_start_1)
fibo_start_2 = int(fibo_start_2)

fibo_list = [fibo_start_1, fibo_start_2]

end_loop = False
end_num = 1


while end_loop == False:
    
    if end_loop == False and end_num <= num:
        suma_1 = fibo_list[-1]
        suma_2 = fibo_list[-2]
        resultado = suma_1 + suma_2
        fibo_list.append(resultado)
        end_num += 1
    else:
        end_loop = True

print(fibo_list[-1])
elapsed_time = time.process_time() - t
print(elapsed_time)
#print(fibo_list)