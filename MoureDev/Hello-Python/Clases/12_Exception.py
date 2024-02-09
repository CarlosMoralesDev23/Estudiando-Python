
number_one = 5
number_two = 1
number_three = "1"

print(' ---- Try - except----')

try:
    print(number_one + number_three)
    print(" ***** We do not have errors *****")
except:
    print(" xxxxx---We have a error---xxxxx")

print('\n')


print(' ---- Try - Except - Else ----')

try:
    print(number_one + number_three)
    print(" ***** We do not have errors_try *****")
except:
    # Se ejecuta si se encuentra un erroren el try
    print(" xxxxx---We have a error_except---xxxxx")
else: # Opcional
    #Se ejecuta si en try NO se encuentran errorres
    print("La execution continua correctamente_else")
finally:# Opcional
    #Se ejecuta siempre con error o sin error
    print("La ejecución continua_finally")

#print(number_one + number_three)  # si por fuera cometemos un error la consola ya no lo controla y se rompe el codigo. 
print('\n')


print(' ---- Excepciones por tipo ----')

try:
    print(number_one + number_three)
    print(" ***** We do not have errors_try *****")
except ValueError:
    # Se ejecuta si se encuentra un erroren el try
    print(" xxxxx---We have a error_except  ValueError ---xxxxx")
except TypeError:
        # Se ejecuta si se encuentra un erroren el try
    print(" xxxxx---We have a error_except  TypeError  ---xxxxx")
print('\n')





print(' ---- Captura de la información de la excepción ----')

try:
    print(number_one + number_three)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
except Exception as exception:
    print(exception)
print('\n')