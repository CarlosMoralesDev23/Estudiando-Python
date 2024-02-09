from Ejercicio_chatgpt_set_01 import colores_set
from Ejercicio_chatgpt_set_01 import numeros_primos
from Ejercicio_chatgpt_set_01 import frutas_set

print(' ---- 8. Crea un conjunto llamado `colores` con tres colores que te gusten. ----')
colores_set = { "Azul", "Negro", "Celeste" }
print(f"Set de colores: {colores_set}")
print('\n')

print(' ---- 9. Crea un conjunto llamado `numeros` con los primeros cinco números primos. ----')
numeros_set = { 2, 3, 5, 7, 11 }
print(f"Set de numeros primos: {numeros_set}")
print('\n')


print(' ---- 10. Encuentra la diferencia entre los conjuntos `colores` y `numeros`. ----')
print(colores_set.difference(numeros_set))
print(numeros_set.difference(colores_set))
print('\n')


print(' ---- 11. Crea un conjunto llamado `vocales` con las vocales del alfabeto. ----')
vocales_set = { "a", "e", "i", "o", "u" }
print(f"Set de vocales: {vocales_set}")
print('\n')


print(' ---- 12. Encuentra la unión entre los conjuntos `colores` y `vocales`. ----')
print(colores_set.union(vocales_set))
print('\n')

print(' ---- 13. Elimina una vocal del conjunto `vocales`. ----')
vocales_set.remove('a')
vocales_set.discard('e')
print(vocales_set)
print('\n')


print(' ---- 14. Crea un conjunto llamado `pares` con números pares del 2 al 10. ----')
pares_set = { 2, 4, 6, 8, 10 }
print(f"Set de pares: {pares_set}")
print('\n')

print(' ---- 15. Encuentra la diferencia simétrica entre los conjuntos `pares` y `numeros`. ----')
print(pares_set.symmetric_difference(numeros_primos))
print('\n')


print(' ---- 16. Combina los conjuntos `frutas` y `pares` en un nuevo conjunto llamado `combinacion_total`. ----')
combinacion_total = frutas_set.union(pares_set)
print(combinacion_total)
print('\n')

print(' ---- 17. Encuentra el número máximo en el conjunto `pares`. ----')
print(max(pares_set))
print('\n')


print(' ---- 18. Encuentra el número mínimo en el conjunto `numeros`. ----')
print(min(numeros_set))
print('\n')


print(' ---- 19. Crea un conjunto llamado `ciudades` con tres ciudades que te gusten. ----')
ciudades_set = { "Madrid", "Barcelona", "Valencia" }
print(f"Set de ciudades: {ciudades_set}")
print('\n')


print(' ---- 20. Encuentra la diferencia simétrica entre los conjuntos `ciudades` y `colores`. ----')
print(ciudades_set.symmetric_difference(colores_set))
print('\n')