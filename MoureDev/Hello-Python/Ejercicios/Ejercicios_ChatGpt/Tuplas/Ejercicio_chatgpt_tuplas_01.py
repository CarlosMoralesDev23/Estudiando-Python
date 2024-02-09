print(' ---- #1 Crea una tupla vacía llamada mi_tupla. ----')
my_tuple = tuple()
print(my_tuple)
print('\n')

print(' ---- #2 Crea una tupla llamada numeros con cinco números enteros. ----')
numbers_5 = (2, 5, 6, 7, 9)
print(numbers_5)
print('\n')

print(' ---- #3 Concatena dos tuplas llamadas tupla1 y tupla2. ----')
tupla_1 = ( 10, 13, 17, 19)
tupla_2 = ( 21, 24, 27, 39)
tupla_1_y_2 = tupla_1 + tupla_2
print(tupla_1_y_2)
print('\n')

print(' ---- #4 Repite la tupla tupla1 tres veces. ----')
tupla_1 = tupla_1 *3
print(tupla_1)
print('\n')


print(' ---- #5 Encuentra la longitud de la tupla tupla2. ----')
print(f"El lenght de la tupla_2 es: {len(tupla_2)}")
print('\n')


print(' ---- #6 Accede al tercer elemento de la tupla numeros. ----')
print(f"El elemento de la posición 3 es: {(numbers_5[2])}")
print('\n')


print(' ---- #7 Invierte el orden de los elementos en la tupla tupla1. ----')
print(tupla_1)
tupla_1_inverted = tupla_1[::-1] 
print(tupla_1_inverted)
print('\n')


print(' ---- #8 Crea una lista llamada frutas con tus tres frutas favoritas. ----')
frutas = ['Sandia', 'Banana', 'Fresa']
print(frutas)
print('\n')

print(' ---- #9 Convierte la lista frutas en una tupla llamada frutas_tupla. ----')
frutas = tuple(frutas)
print(frutas, type(frutas))
print('\n')


print(' ---- #10 Combina las tuplas tupla1 y tupla2 en una nueva tupla llamada combinacion. ----')
tupla_1 = ( 10, 13, 17, 19)
tupla_2 = ( 21, 24, 27, 39)
combinacion = tupla_1 + tupla_2
print(combinacion)
print('\n')