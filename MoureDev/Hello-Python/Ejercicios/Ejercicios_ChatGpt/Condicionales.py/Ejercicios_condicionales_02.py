print(' ---- 3. **Clasificación de Números:** ----')
import random
numero_aleatorio = random.randint(5, 10)
rango_aleatorio = random.randint(1, 3)
rango_aleatorio_2 = random.randint(1,3)
print(f"El numero esta entre {numero_aleatorio-rango_aleatorio} y {numero_aleatorio+rango_aleatorio_2} adivina cual es?")
mi_numero = int(input("Ingresa tu numero: "))
if numero_aleatorio == mi_numero:
    print(f"Correcto el numero es {numero_aleatorio}")
else:
    print("Fallaste vuelve a intentarlo")
print(f"El numero aleatorio era {numero_aleatorio}")
print('\n')


print(' ---- 4. **Verificación de Contraseña:** ----')
contraseña = "secreto123"
my_contraseña = input("Por favor ingresa tu contraseña: ")

if contraseña == my_contraseña:
    print("Puedes acceder al sistema.")
else:
    print("Contraseña incorrecta")
print('\n')


print(' ---- 5. **Verificación de Números Positivos:** ----')
numero = int(input("Favor ingresa un numero: "))
if numero > 0 and numero %3 == 0:
    print(f"El numero {numero} es positivo y divisible entre 3 ")
elif numero > 0 and numero %3 != 0:
    print(f"El numero {numero} es positivo pero no es divisible entre 3 ")
elif numero < 0 and numero %3 == 0:
    print(f"El numero {numero} es negativo pero es divisible entre 3 ")
elif numero < 0 and numero %3 != 0:
    print(f"El numero {numero} es negativo pero no es divisible entre 3 ")
else:
    print(f"Ingresaste {numero}, no e sun numero")
    


print('\n')


