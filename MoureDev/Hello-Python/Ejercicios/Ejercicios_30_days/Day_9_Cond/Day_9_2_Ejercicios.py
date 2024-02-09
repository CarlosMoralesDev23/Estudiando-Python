print(' ---- Ejercicios Condicionales ----')
print('\n')

########################################################
print(' ---- #4 - Write a code which gives grade to students according to theirs scores ----')

score = int(input("Por favor ingresa tu Score: "))

if score >= 80  and score <= 100:
    print("Your grade is A")
elif score >= 70  and score <= 79:
    print("Your grade is B")
elif score >= 60  and score <= 69:
    print("Your grade is C")
elif score >= 50  and score <= 59:
    print("Your grade is C")
elif score >= 0  and score <= 50:
    print("Your grade is C")
else:
    print("Solo puede ingresar valores de 0 a 100")

print('\n')


########################################################
print(' ---- #5 What season is? ----')
month = input("En que mes estamos: ")

if month == "September" or month == "October" or month == "November":
    print("The season is Autum")
elif month == "December" or month == "January" or month == "February":
    print("The season is Winter")
elif month == "March" or month == "April" or month == "May":
    print("The season is Spring")
elif month == "June" or month == "July" or month == "August":
    print("The season is Summer")
print('\n')


########################################################
print(' ----#6 - If a fruit doesnt exist in the lista ----')
fruits = ['banana', 'orange', 'mango', 'lemon']

new_fruit = input("Ingresa una nueva fruta: ")

if new_fruit in fruits:
    print("That fruit already exist in the list")
    print(fruits)
else:
    fruits.append(new_fruit)
    print(fruits)

print('\n')

