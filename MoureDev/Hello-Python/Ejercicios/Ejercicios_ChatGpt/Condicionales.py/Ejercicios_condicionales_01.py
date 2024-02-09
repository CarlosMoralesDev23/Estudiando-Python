numero_1 = int(input("Ingresa el primer numero: "))
numero_2 = int(input("Ingresa el segundo numero: "))
edad = int(input("Por favor ingresa tu edad: "))


print(' ---- 1. **Comparación de Números:** ----')
if numero_1 > numero_2:
    print(f"El numero {numero_1} es mayor")
elif numero_2 > numero_1:
    print(f"El numero {numero_2} es mayor")
else:
    print(f"Los numeros son iguales")

print('\n')


print(' ---- 2. **Rango de Edades:** ----')
if edad >= 18 and edad <= 65: 
    print("Tienes edad suficiente para Tomar alcohol, votar, y manejar")
elif edad > 65 and edad <= 100:
    print("Puedes votar, y tomar alcohol,  pero para manejar es debes hacerte examenes de la vista")
elif edad > 100:
    print(f"Seguiro que continuas con vida despues de {edad} años???")
else:
    print("No ingresaste una edad correcta")
print('\n')


