print('----- Mas funciones -----')
print('\n')

######################    enumerate()    ########################## 
print('--- enumerate() ---')  
print('--- Obtener un listado de Indice y valor, enumerate() ---')  
frutas = ['Manzana', 'Banana', 'Cereza']
for indice, fruta in enumerate(frutas, start = 1):
    print(f'Indice {indice}: {fruta}')
print('\n')


######################    filter()    ########################## 
print('--- filter() ---')  
print('--- filtrar segun un criterio, filter() ---')  

def es_par(numero):
    return numero % 2 == 0

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = filter(es_par, numeros) #Pasa la función y la lista, regresa una lista
print(list(numeros_pares))
print('\n')


######################    float()    ########################## 
print('--- float() ---')  
print('--- convierte enteros y string en Float,  float() ---')  

print(type(float(42)))
print(type(float("3.14")))
print('\n')


######################    format()    ########################## 
print('--- format() ---')  
print('--- Permite convinar string junto a variables, format() ---')
nombre = 'Carlos'
edad = 33
pi = 3.1415926535899793

print('Ejemplo 1')
mensaje_1 = 'Hola, soy {} y tengo {} años.'.format(nombre, edad)
print(mensaje_1)

print('Ejemplo 2')
mensaje_2 = 'Hola, soy {0} y tengo {1} años. Me llamo {0}'.format(nombre, edad)
print(mensaje_2)

print('Ejemplo 3')
mensaje_pi = "El valor de pi es: {:.2f}".format(pi)
print(mensaje_pi)
print('\n')
############################################################3


######################    frozenset()    ########################## 
print('--- frozenset() ---')  
print('--- Crea un set inmutable, no se modifica ni con add, remove, discard; frozenset() ---')  

lista_numeros_fset = frozenset([1, 2, 3, 4, 5])
print("frozenset:", lista_numeros_fset)
print("Tipo de datos:", type(lista_numeros_fset))
print('\n')








'''
Pendientes
aiter()
anext()
ascii()
bytearray()
bytes()
callable()
classmethod()
compile()
delattr()
dir()
eval()
exec()
'''



