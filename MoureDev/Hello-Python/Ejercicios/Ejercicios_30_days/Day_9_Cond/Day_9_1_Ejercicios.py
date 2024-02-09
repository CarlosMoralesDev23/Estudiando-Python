print(' ---- Ejercicios Condicionales ----')
print('\n')

########################################################
print(' ---- #1 - Puede manejar??? ----')

age = int(input("Por favor ingresa tu edad: "))

if age >= 18:
    print("You are old enough to drive.")
elif age > 30: 
    print("You are old enough to learn to drive.")
elif age < 18: 
    print(f"You need {18 - age} more years to learn to drive.")

print('\n')


########################################################
print(' ---- #2 - Who is older (me or you)?  ----')

your_age = 30

my_age = int(input("Por favor dinos tu edad: "))

if your_age == my_age:
    print(f"Tenemos la misma edad: {your_age}")

elif your_age > my_age:
    print(f"You are {your_age - my_age} years older than me.")

else: 
    print(f"I'm {my_age -your_age} years older than you.")
print('\n')


########################################################
print(' ---- #3 - What number is greater ----')

a = int(input("Por favor ingrese el numero A: "))
b = int(input("Por favor ingrese el numero B: "))

if a == b:
    print("Los numeros son iguales")
elif a > b:
    print(f"El numero {a} es mayor que el numero {b}")
else:
    print(f"El numero {b} es mayor que el numero {a}")
print('\n')