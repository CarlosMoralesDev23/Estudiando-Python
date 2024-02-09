import math
#Day 3: 30 Days of python programming'

# 18 - Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print("---- floor division of 7 by 3 is equal? ----")
print(f"7//3  y int(2.7) son iguales: {(7 // 3) == (int(2.7))}")
print("\n")

# 19 - Check if type of '10' is equal to type of 10
print("---- type of '10' is equal to type of 10 ----")
print(type(10) == type("10"))
print("\n")

# 20 - Check if int('9.8') is equal to 10
print("---- Checking si int('9.8') is equal to 10 ----")
print( (int (float ('9.8') ) ) == 10)
print("\n")

# 21 -Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
print("---- Calculating pay ----")
horas_trabajadas = int(input("Cuantas horas trabajadas: "))
tarifa = int(input(("Ingrese su tarifa: ")))
print(f"Por semana usted gana: {(horas_trabajadas * tarifa * 7)}")
print("\n")

# 22 -Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
print("---- Calculating seconds live ----")
edad = int(input("Dime tu edad: "))
segundos_por_edad = ((3600*24) * 365) * edad
print(f"Tu has vivido ${segundos_por_edad} segundos")

# 24 - Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
a = 1
b = 2
c = 3
d = 4
e = 5
print(f"{a}  1  {a}  {a**2}  {a**3}")
print(f"{b}  1  {b}  {b**2}  {b**3}")
print(f"{c}  1  {c}  {c**2}  {c**3}")
print(f"{d}  1  {d}  {d**2}  {d**3}")
print(f"{e}  1  {e}  {e**2}  {e**3}")