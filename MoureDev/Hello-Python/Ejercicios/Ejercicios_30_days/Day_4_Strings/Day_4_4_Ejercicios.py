import math
#Day 4: 30 Days of python programming'
thirty_days_of_python = "Thirty " + "Days " + "Of " + "Python"
coding_for_all = "Coding For All"
company = coding_for_all
python_for_all = coding_for_all.replace("Coding", "Python")

everyone_for_all = python_for_all.replace("All", "Everyone")


# 32 - The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
print("---- Separar librerias # ----")
list_libraries = ["Django", "Flask", "Pyramid", "Falcon"]
list_separados = (' # ').join(list_libraries)
print(list_separados)
print('\n')

# 33 - Use the new line escape sequence to separate the following sentences.
print("---- Hacer scape para bajar la linea # ----")
oracion_2 = " I am enjoying this challenge. \n I just wonder what is next."
print(oracion_2)
print('\n')


# 34 - Use a tab escape sequence to write the following lines.
#Name      Age     Country   City
#Asabeneh  250     Finland   Helsinki
print("---- Has la tabla con tabulacion y scape ----")
linea = "Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"
print(linea)
print('\n')

# 35 - Make the following using string formatting methods:

# Operaciones matemáticas
suma = 8 + 6
resta = 8 - 6
multiplicacion = 8 * 6
division = 8 / 6
modulo = 8 % 6
division_entera = 8 // 6
potencia = 8 ** 6

# Utilizar el formato de cadena para mostrar los resultados
resultado_suma = "{} + {} = {}".format(8, 6, suma)
resultado_resta = "{} - {} = {}".format(8, 6, resta)
resultado_multiplicacion = "{} * {} = {}".format(8, 6, multiplicacion)
resultado_division = "{} / {} = {:.2f}".format(8, 6, division)
resultado_modulo = "{} % {} = {}".format(8, 6, modulo)
resultado_division_entera = "{} // {} = {}".format(8, 6, division_entera)
resultado_potencia = "{} ** {} = {}".format(8, 6, potencia)

# Imprimir los resultados
print(resultado_suma)
print(resultado_resta)
print(resultado_multiplicacion)
print(resultado_division)
print(resultado_modulo)
print(resultado_division_entera)
print(resultado_potencia)