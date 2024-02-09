############################################
print(' ---- Operadores Aritmeticos ----')
print(f"Suma 3+4 = {3+4}")
print(f"Resta 3-4 = {3-4}")
print(f"Multiplicación 3*4 = {3*4}")
print(f"División 3/4 = {3/4}" )
print(f"Resto 3%4 = {3%4}")
print(f"Elevar 2 a la 3 = {2**3}")
print(f"Dividir 10//3 y acercarse al número entero = {10//3}")
print('\n')

############################################
print(' ---- Operaciones irregulares ----')

print(f"Sumar strings = {'Hola ' + 'Python ' + 'Que tal?'}")

print(f"Sumar string mas int convertido a string = {'Hola ' + str(5)}")

print(f"Multiplicar str con int = {'Hola  ' * 5}")

print(f"Multiplicar str, con int elevadoa la 3 = {'Hola ' * (2**3)}")

my_float = 1.5 * 2
print(f"Multiplicar str con float convertido a entero = {'Hola ' * int(my_float)}")

print('\n')

############################################
### Operadores Comparativos ###
print(3 > 4)
print(3 >= 4)
print(3 < 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)

print('-----------------')
# Operaciones con cadenas de texto
print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa")  # Ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa"))  # Cuenta caracteres
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")

# Operadores Lógicos  02:13:02 #
print('---------------------')

# Basada en el Álgebra de Boole https://es.wikipedia.org/wiki/%C3%81lgebra_de_Boole
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not (3 > 4)) ### Niega la condicion false, y la convierte en TRUE