print(' ---- 6. **Menú de Opciones:** ----')

print("Elige algunas de las siguientes opciones")
print(1, 2, 3)
opcion = int(input("Cúal opcion eliges: "))

if opcion == 1:
    print("Elegiste la opción 1")
elif opcion == 2:
    print("Elegiste la opción 2")
elif opcion == 3:
    print("Elegiste la opción 3")
else:
    print("Número de opción incorrecta")

print('\n')




print(' ---- 7. **Aprobación de Crédito:** ----')

puntaje_crediticio = int(input("Ingresa tu puntaje crediticio: "))
tiene_deudas = input("Tienes deudas, ingrese True o False: ")

if puntaje_crediticio >= 700 and tiene_deudas.lower() == 'false':
    print("Puedes acceder al credito")
elif puntaje_crediticio < 700 or tiene_deudas.lower() == 'true':
    print("No Puedes acceder al credito")

print('\n')

