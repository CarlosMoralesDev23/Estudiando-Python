print(' ---- 1. Crea un diccionario vacío llamado `mi_dict`. ----')
mi_dict = {}
print(f"Diccionario vacío: {mi_dict}")
print('\n')

print(' ---- 2. Crea un diccionario llamado `edades` con tres personas y sus edades. ----')
edades_dict = {
    "Carlos": 33,
    "Alberto": 34,
    "Morales": 35
}
print(edades_dict)
print('\n')


print(' ---- 3. Agrega una nueva persona y edad al diccionario `edades`. ----')
edades_dict["Juan"] = 36
print(edades_dict)
print('\n')


print(' ---- 4. Accede a la edad de una persona en el diccionario `edades`. ----')
print(edades_dict['Carlos'])
print('\n')


print(' ---- 5. Elimina una persona del diccionario `edades`. ----')
del edades_dict["Alberto"]
print(edades_dict)
print('\n')

print(' ---- 6. Comprueba si una persona específica está en el diccionario `edades`. ----')
print("Carlos" in edades_dict)
print('\n')

print(' ---- 7. Imprime todas las claves (nombres) en el diccionario `edades`. ----')
print(edades_dict.keys())
print('\n')

print(' ---- 8. Imprime todos los valores (edades) en el diccionario `edades`. ----')
print(edades_dict.values())
print('\n')


print(' ---- 9. Imprime todos los elementos (pares clave-valor) en el diccionario `edades`. ----')
print(edades_dict.items())
print('\n')


print(' ---- 10. Crea un segundo diccionario llamado `alturas` con información de la altura de las mismas personas. ----')
alturas = {
    "Carlos" : 1.68,
    "Luis" : 1.65,
    "Carlitos" : 1.10
}
print(alturas)
print('\n')


print(' ---- 11. Combina los diccionarios `edades` y `alturas` en un nuevo diccionario llamado `datos_personales`. ----')
datos_personales = edades_dict.copy()
datos_personales.update(alturas)
print(datos_personales)
print('\n')



print(' ---- 12. Actualiza la edad de una persona en el diccionario `datos_personales`. ----')
edades_dict['Morales']= "40"
print(edades_dict)
print('\n')


print(' ---- 13. Elimina una persona y su información del diccionario `datos_personales`. ----')
del edades_dict['Juan']
print(edades_dict)
print('\n')


print(' ---- 14. Imprime la longitud (número de elementos) del diccionario `datos_personales`. ----')
print(len(datos_personales))
print('\n')


print(' ---- 15. Vacía el diccionario `datos_personales`. ----')
datos_personales.clear()
print(datos_personales)
print('\n')


print(' ---- 16. Crea un diccionario llamado `frutas` con nombres de frutas y sus cantidades. ----')
frutas_dict = {
    "Manzana" : 10,
    "Banana" : 45,
    "Cereza" : 23
}
print('\n')


print(' ---- 17. Incrementa la cantidad de una fruta específica en el diccionario `frutas`. ----')
frutas_dict['Manzana'] += 15 
print(frutas_dict)
print('\n')


print(' ---- 18. Imprime las frutas en orden alfabético según sus nombres. ----')
print(sorted(frutas_dict))
print('\n')


print(' ---- T19. Imprime la fruta con la mayor cantidad en el diccionario `frutas`. ----')
fruta_mayor= max(frutas_dict, key=frutas_dict.get)
print(fruta_mayor, frutas_dict[fruta_mayor])
print('\n')


print(' ---- 20. Imprime la suma total de todas las cantidades en el diccionario `frutas`. ----')
suma_frutas = sum(frutas_dict.values())
print(suma_frutas)
print('\n')


