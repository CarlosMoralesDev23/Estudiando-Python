print('----- Mas funciones -----')
print('\n')

######################    range()    ########################## 
print('--- range() ---')  
print('--- permite crear una secuencia de numeros, range() ---')  
#range([start,] stop[, step])
print(list(range(10)))
print(list(range(5, 10)))
# Crear una secuencia de números pares del 2 al 10
print(list(range(2, 11, 2)))
print('\n')


######################    reversed()    ########################## 
print('--- reversed() ---')  
print('--- permite poner al reves un orden, reversed() ---')  
# Puede aplicarse a objetos que admiten el protocolo de iteración, como 
#listas, tuplas, cadenas y otros tipos de datos iterables.
print(list(reversed([1, 2, 3, 4, 5])))
print(''.join(reversed('Hola, mundo')))

for elemento in reversed([1, 2, 3, 4, 5]):
    print(elemento)

print('\n')


######################    round()    ########################## 
print('--- round() ---')  
print('--- permite redondear un numero, round() ---') 
print(5.6789)
print(round(5.67)) #Automaticamente al numero entero mas cercano
print(round(5.47)) #Automaticamente al numero entero mas cercano
print(round(5.6789, 2)) #Redondear con 2 decimales
print(round(5.6789, 0)) #imprimira con decimal 0
print('\n')

######################    slice()    ########################## 
print('--- slice() ---')  
print('--- Extraer parte de un objeto, slice() ---') 
#objeto_slice = slice(inicio, fin, paso) #paso es cantidad de ejemplo 2 en 2, sino se dice se asume que es de 1 en 1
mi_slice = slice(1, 5, 2)
print([0, 1, 2, 3, 4, 5, 6, 7, 8, 9][mi_slice])
#imprime[1,3]
print('\n')


######################    sorted()    ########################## 
print('--- sorted() ---')  
print('--- Devuelve una lista ordenada que se puede almacenar, sorted() ---') 
lista_numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
lista_ordenada = sorted(lista_numeros)
print(lista_ordenada)

#Las cadenas de string ordena alfabeticamente
cadena_original = "python"
cadena_ordenada = ''.join(sorted(cadena_original))
print(cadena_ordenada)


lista_palabras = ["manzana", "kiwi", "plátano", "fresa", "uva"]
lista_ordenada_por_longitud = sorted(lista_palabras, key=len)
print(lista_ordenada_por_longitud) #Las ordeno por longuitud de los elementos
print('\n')


######################    sum()    ########################## 
print('--- sum() ---')  
print('--- Suma iterables, sum() ---') 
#resultado_suma = sum(iterable, start=0)

print(sum([1, 2, 3, 4, 5,6,7]))  # Imprimirá 28
print(sum((1, 2, 3, 4, 5), start=10))  # tupla # empieza en 10# Imprimirá 25
print(sum({1, 2, 3, 4, 5, 6}))  # Imprimirá 21

generador_numeros = (x for x in range(1, 6))
suma_generador = sum(generador_numeros)
print(suma_generador)  # Imprimirá 15
print(sum((x for x in range(1, 6))))# Imprimirá 15

######################    zip()    ########################## 
print('--- zip() ---')  
print('--- combinar elementos de dos o mas iterables, zip() ---')
#zipeado = zip(iterable1, iterable2, ...)
print(list(zip([1, 2, 3], ['a', 'b', 'c'])))  # Imprimirá [(1, 'a'), (2, 'b'), (3, 'c')]
print(list(zip([1, 2, 3],['a', 'b', 'c'],['x', 'y', 'z'])))  # Imprimirá [(1, 'a', 'x'), (2, 'b', 'y'), (3, 'c', 'z')]
#Diferentes Longuitudes, se corta con la mas corta
print(list(zip([1, 2, 3], ['a', 'b'])))  # Imprimirá [(1, 'a'), (2, 'b')]

for num, letra in zip([1, 2, 3], ['a', 'b', 'c']):
    print(num, letra)
# Imprimirá:
# 1 a
# 2 b
# 3 c


'''
Pendientes
repr()
setattr()
staticmethod()
super()
vars()
__import__()

'''



