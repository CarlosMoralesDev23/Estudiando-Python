print('----- Mas funciones -----')
print('\n')

######################    map()    ########################## 
print('--- map() ---')  
print('--- permite obtener una nueva lista, map() ---')  
def cuadrado(x):
    return x ** 2
print(list(map(cuadrado, [1, 2, 3, 4, 5])))
print('\n')


print('Ejemplo mapeando y sumando 2 listas')
def suma(x, y):
    return x + y
print(list(map(suma, [1, 2, 3, 4, 5], [10, 20, 30, 40, 50])))
print('\n')



######################    max()    ########################## 
print('--- max() ---')  
print('--- permite obtener el maximo de una lsita, max() ---')  
print("Máximo número:", max([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))
print('\n')


######################    min()    ########################## 
print('--- min() ---')  
print('--- permite obtener el minimo de una lsita, min() ---')  
print("Minimo número:", min([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))
print('\n')

print('Encontrar el mínimo de una lista de cadenas basado en la longitud')
palabras = ["manzana", "kiwi", "plátano", "fresa", "uva"]
minima_longitud_palabra = min(palabras, key=len)
print("Palabra más corta:", minima_longitud_palabra)
print('\n')

######################    next()    ########################## 
print('--- next() ---')  
print('--- permite iterar la lista, next() ---')
iterador_lista = iter([1,2,3])
print(next(iterador_lista, "Fin")) 
print(next(iterador_lista, "Fin")) 
print(next(iterador_lista, "Fin")) 
print(next(iterador_lista, "Fin")) 
#Cuando se termine la lista imprime Fin
print('\n')


######################    ord()    ########################## 
print('--- ord() ---') 
print('--- Verificar el unicode de un caracter, ord() ---')
print(f"Caracter: {ord('B')}") 
print('\n')

######################    pow()    ########################## 
print('--- pow() ---') 
print('--- Se utiliza para calcular una potencia, pow() ---')
#resultado = pow(base, exponente, [módulo])
# Calcular 2 elevado a la 3ra potencia
print(pow(2, 3))  # Imprime 8
# Calcular 2 elevado a la 3ra potencia, módulo 5
print(pow(2, 3, 5))  # Imprime 3
print('\n')






'''
Pendientes

memoryview()
object()
oct()
open()
property()

'''



