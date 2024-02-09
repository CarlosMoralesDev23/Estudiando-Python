print(' ---- 1. Crea un conjunto vacío llamado `set_vacio`. ----')
set_vacio = set()
print(f"Asi podemos crear un set vacio.  {type(set_vacio)}")
print('\n')

print(' ---- 2. Crea un conjunto llamado `colores` con tres colores que te gusten. ----')
colores_set = { "Azul", "Negro", "Celeste" }
print(f"Set de colores: {colores_set}")
print('\n')

print(' ---- 3. Agrega un nuevo color al conjunto `colores`. ----')
colores_set |= {"Blanco"}
print(colores_set)
colores_set.add("Verde")
print(colores_set)
colores_set.update(["Amarillo"])
print(colores_set)
print('\n')

print(' ---- 4. Crea un conjunto llamado `numeros` con los primeros cinco números primos. ----')
numeros_primos = {2, 3, 5, 7, 11}
print(f"Set de numeros primos: {numeros_primos}")
print('\n')


print(' ---- 5. Combina los conjuntos `colores` y `numeros` en un nuevo conjunto llamado `combinacion`. ----')
combinacion = colores_set | numeros_primos
print(f"Set combinado: {combinacion}")
print('\n')


print(' ---- 6. Encuentra la intersección entre los conjuntos `colores` y `numeros`. ----')
interseccion = colores_set & numeros_primos
print(f"Set de interseccion: {interseccion}")
print('\n')


print(' ---- 7. Elimina un color del conjunto `colores`. ----')
colores_set.remove("Amarillo")
print(colores_set)
colores_set.discard("Verde")
print(colores_set)
print('\n')


print(' ---- 8. Crea un conjunto llamado `frutas` con tres frutas que te gusten. ----')
frutas_set = { "Manzana", "Banana", "Cereza" }
print(f"Set de frutas: {frutas_set}")
print('\n')

print(' ---- 9. Agrega una nueva fruta al conjunto `frutas`. ----')
print(frutas_set)
frutas_set.update(["Fresa"])
frutas_set.add("Durazno")
print(frutas_set)
print('\n')


print(' ---- 10. Encuentra la diferencia entre los conjuntos `colores` y `frutas`. ----')
print(colores_set.difference(frutas_set))
print(frutas_set.difference(colores_set))
print('\n')



'''

Entendido, aquí tienes 20 ejercicios básicos relacionados con conjuntos (sets) en Python. Estos ejercicios se centran en diversas funciones y operaciones que puedes realizar con conjuntos, sin utilizar bucles, funciones definidas por el usuario ni condicionales en el código principal:



10. Encuentra la diferencia entre los conjuntos `frutas` y `colores`.
11. Crea un conjunto llamado `vocales` con las vocales del alfabeto.
12. Encuentra la unión entre los conjuntos `colores` y `vocales`.
13. Elimina una vocal del conjunto `vocales`.
14. Crea un conjunto llamado `pares` con números pares del 2 al 10.
15. Encuentra la diferencia simétrica entre los conjuntos `pares` y `numeros`.
16. Combina los conjuntos `frutas` y `pares` en un nuevo conjunto llamado `combinacion_total`.
17. Encuentra el número máximo en el conjunto `pares`.
18. Encuentra el número mínimo en el conjunto `numeros`.
19. Crea un conjunto llamado `ciudades` con tres ciudades que te gusten.
20. Encuentra la diferencia simétrica entre los conjuntos `ciudades` y `colores`.

Estos ejercicios te proporcionarán práctica con diversas operaciones de conjuntos en Python. ¡Espero que te resulten útiles!

'''