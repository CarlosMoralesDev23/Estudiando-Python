print(' ---- Calculos ----')
print('\len_lista')

lista_to_calcular = [1, 5, 4, 6, 2, 3, 7, 4, 9, 6, 6, 8]

print(' ---- Media / mean ----')
def media(lista):
    suma = 0
    for element in lista:
        suma += element
    media = suma / len(lista)
    return print(media)
media(lista_to_calcular)
print('\n')



lista_to_calcular = [1, 9, 4, 11, 2, 3, 7, 4, 9, 15, 6, 8]

print(' ---- Mediana / median ----')
def calcular_mediana(lista):
    lista_ordenada = sorted(lista)   # Ordenar la lista, es necesario
    len_lista = len(lista_ordenada)  # Obtener la length, para saber si es par o impar

    if len_lista % 2 == 0:
        # Si la longitud es par, tomar el promedio de los dos valores centrales
        mediana = (lista_ordenada[len_lista // 2 - 1] + lista_ordenada[len_lista // 2]) / 2
    else:
        # Si la longitud es impar, tomar el valor central
        mediana = lista_ordenada[len_lista // 2]
    return mediana

mediana_resultado = calcular_mediana(lista_to_calcular)
print("Lista ordenada:", sorted(lista_to_calcular))
print("Mediana:", mediana_resultado)
print('\n')





'''

Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).

'''