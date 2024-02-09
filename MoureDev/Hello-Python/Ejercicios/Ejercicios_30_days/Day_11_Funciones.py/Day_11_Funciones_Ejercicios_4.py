print(' ---- #13 sum_of_numbers ----')
def sum_of_numbers(rango):
    suma= sum(range(1, rango + 1))
    return suma
suma = sum_of_numbers(10)
print(suma)
print('\n')


print(' ---- #14 sum_of_odds ----')
def sum_of_odds(rango2):
    suma_odds = 0
    numeros = list(range(rango2 + 1))
    for i in numeros:
        if i % 2 != 0:
            suma_odds += i
            print(suma_odds)
    return suma_odds
suma_odds = sum_of_odds(10)
print(suma_odds)
print('\n')


print(' ---- Level 2 ----')
print('\n')


print(' ---- #1 evens_and_odds  ----')
def evens_and_odds(rango_3):
    numeros = list(range(rango_3 + 1))
    cuantos_even = 0
    cuantos_odds = 0
    for i in numeros:
        if i %2 == 0:
            cuantos_even += 1
        else:
            cuantos_odds += 1
    return cuantos_even, cuantos_odds
print(evens_and_odds(210))
print('\n')



print(' ---- #2 factorial ----') #Multiplicar todos los numeros compredidos hasta un numero. 
def factorial(factorial):
    resultado = 1
    numeros = list(range(1, factorial + 1))
    numeros.reverse()
    print(numeros)
    for i in numeros:
        resultado *= i 
    return resultado
print(factorial(10))
print('\n')


print(' ---- #3 is_empty ----')
def is_empty(parametro):
    return not bool(parametro)

cadena_vacia = ""
cadena_no_vacia = "Hola, mundo!"
# Verificar si las cadenas están vacías o no
print(is_empty(cadena_vacia))  # Devolverá True
print(is_empty(cadena_no_vacia))  # Devolverá False
print('\n')


