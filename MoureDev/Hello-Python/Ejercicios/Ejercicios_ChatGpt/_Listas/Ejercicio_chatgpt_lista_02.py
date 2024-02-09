from Ejercicio_chatgpt_lista_01 import mi_lista
from Ejercicio_chatgpt_lista_01 import mi_lista_1
from Ejercicio_chatgpt_lista_01 import mi_lista_2
from Ejercicio_chatgpt_lista_01 import mi_lista_3
from Ejercicio_chatgpt_lista_01 import nombres



print(' ---- # 11 Extiende la lista lista1 con la lista lista2. ----')
print(mi_lista_1)
mi_lista_1 += mi_lista_2
print(mi_lista_1)
print('\n')


print(' ---- #12 Ordena la lista nombres alfabéticamente. ----')
nombres.sort()
print(nombres)
print('\n')


print(' ---- #13 Encuentra el índice del elemento "Python" en la lista . ----')
skills = ['Java', 'C++', 'Python', 'JavaScript']
print(skills.index("Python"))
print('\n')

print(' ---- #14 Elimina todos los elementos de la lista lista2. ----')
mi_lista_2.clear()
print(mi_lista_2)
print('\n')

print(' ---- #15 Crea una lista llamada numeros con los números del 1 al 5. ----')
numbers_1_5 = [1, 2, 3, 4, 5]
print(numbers_1_5)
print('\n')




print(' ---- # 16 NO SE PUDO HACER - Multiplica cada elemento de la lista numeros por 2 ----')
#################
''' Se requiere funciones y loops'''
#################
#################
#################
#################
print('\n')


print(' ---- #17 Encuentra la suma de todos los elementos en la lista numeros. ----')
suma = sum(mi_lista_1)
print(suma)
print('\n')


print(' ---- #18  Crea una lista llamada pares con los números pares del 2 al 10. ----')
numeros_pares = [2, 4, 6, 8, 10]
print(numeros_pares)
print('\n')

print(' ---- #19 Combina las listas nombres y pares en una nueva lista llamada combinacion. ----')
combinacion = nombres + numeros_pares
print(combinacion)
print('\n')

print(' ---- #20 Convierte la lista combinacion a una tupla llamada combinacion_tupla. ----')
combinacion_tupla = tuple(combinacion)
print(combinacion_tupla)
print('\n')