print(' ---- Calculos ----')
print('\len_lista')

lista = [1, 1, 5, 7, 9,6, 6, 6, 4, 5, 4, 6, 2, 3, 7, 4, 9, 6, 6, 8]

print(' ---- Moda ----')

frecuencias = {}

def moda(lista):
    for numero in lista:
        if numero in frecuencias:
            frecuencias[numero] +=1
        else:
            frecuencias[numero] = 1

    moda= max(frecuencias, key=frecuencias.get)

    return moda

print(moda(lista))

print('\n')







'''

Write different functions which take lists. They should, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).

'''