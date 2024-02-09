
from Ejercicio_chatgpt_tuplas_01 import numbers_5
from Ejercicio_chatgpt_tuplas_01 import frutas


print(' ---- #11 Encuentra el número máximo en la tupla numeros.  ----')
print(numbers_5)
print(f"El numero mas grande de la tupla es: {(max(numbers_5))}")
print('\n')


print(' ---- #12 Encuentra el número mínimo en la tupla numeros. ----')
print(numbers_5)
print(f"El numero mas bajo de la tupla es: {(min(numbers_5))}")
print('\n')


print(' ---- #13 Crea una lista llamada pares con números pares del 2 al 10. ----')
list_10 = []
list_10.append(2)
list_10.append(4)
list_10.append(6)
list_10.append(8)
list_10.append(10)
print(list_10)
print('\n')

print(' ---- #14 Convierte la lista pares en una tupla llamada pares_tupla. ----')
pares_tupla = tuple(list_10)
print(pares_tupla)
print('\n')


print(' ---- #15 Combina las tuplas frutas_tupla y pares_tupla en una nueva tupla llamada combinacion_total. ----')
combinacion_total = frutas + pares_tupla
print(combinacion_total)
print('\n')


print(' ---- #16 Calcula la suma de todos los elementos en la tupla numeros. ----')
print(numbers_5)
print(f"La suma de la tupla numeros es: {sum(numbers_5)}")
print('\n')

print(' ---- #17 Encuentra la cantidad de veces que aparece el número 3 en la tupla numeros. ----')
print(f"El numero 3 aparece en la tupla numeros: {numbers_5.count(3)} veces.")
print('\n')

print(' ---- #18 Crea una lista llamada colores con tus tres colores favoritos. ----')
print('\n')

print(' ---- #19 Convierte la lista colores en una tupla llamada colores_tupla. ----')
colores_tupla = ("Azul", "Verde", "Naranja")
print(colores_tupla)
print('\n')

print(' ---- #20 Convierte la tupla numeros a una lista llamada numeros_lista. ----')
print(numbers_5, type(numbers_5))
numbers_5 = list(numbers_5)
print(f"Converti al tupla numeros a una lista: {(type(numbers_5))}")
print('\n')
