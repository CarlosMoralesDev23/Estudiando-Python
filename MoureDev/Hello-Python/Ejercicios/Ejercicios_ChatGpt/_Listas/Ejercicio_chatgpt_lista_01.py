print(' ---- #1 Crea una lista vacía llamada mi_lista. ----')
mi_lista = list()
print(type(mi_lista))
print('\n')

print(' ---- #2  Agrega tres elementos de tipo entero a la lista mi_lista.----')
mi_lista.append(4)
mi_lista.append(6)
mi_lista.append(10)
print(mi_lista)
print('\n')

print(' ---- #3 Concatena dos listas llamadas lista1 y lista2. ----')
mi_lista_1 = [1, 5, 7]
mi_lista_2 = [6, 8, 15]
mi_lista_3 = mi_lista_1 + mi_lista_2
print(mi_lista_3)
print('\n')

print(' ----#4 Repite la lista lista1 tres veces. ----')
mi_lista_1_3_veces = mi_lista_1 * 3
print(mi_lista_1_3_veces)
print('\n')

print(' ---- #5 Encuentra la longitud de la lista lista2. ----')
mi_lista_2_len = len(mi_lista_2)
print(mi_lista_2_len)
print('\n')

print(' ---- #6  Elimina el segundo elemento de la lista mi_lista. ----')
print(mi_lista)
del mi_lista[1]
print(mi_lista)
print('\n')

print(' ---- #7  Invierte el orden de los elementos en la lista lista1. ----')
print(mi_lista_1)
mi_lista_1.reverse()
print(mi_lista_1)
print('\n')

print(' ---- #8 Crea una lista llamada nombres con tus tres nombres. ----')
nombres = list()
nombres.append("Carlos")
nombres.append("Alberto")
nombres.append("Jose")
print(nombres)
print('\n')

print(' ---- #9 Añade tu apellido a la lista nombres. ----')
nombres.append("Morales")
print(nombres)
print('\n')

print(' ---- #10 Copia la lista nombres en una nueva lista llamada nombres_copia. ----')
nombres_copia= nombres.copy()
print(nombres_copia)
print('\n')

