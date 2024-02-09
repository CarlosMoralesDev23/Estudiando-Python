print(' ---- Importando modulo completo ----')
import my_module

my_module.suma_values(1,2,3)
my_module.print_value("Hola Carlitos")
print('\n')


print(' ---- Importando funciones de un modulo ----')
from my_module import suma_values
from my_module import print_value

my_module.suma_values(3,4,5)
my_module.print_value("Hola Sofia")
print('\n')


print(' ---- Modulos del sistema ----')

import math

print(math.pi)
print(math.pow(2, 5)) #Exponencial

from math import pi as print_value

print(print_value)




print('\n')


