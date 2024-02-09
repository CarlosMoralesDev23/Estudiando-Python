print(' ---- Loops ----')
print('\n')


#######################################################################################
print(' ---- Iterate 0 to 10 using for loop, do the same using while loop. ----')

lista = [1,2,3,4,5,6,7,8,9,10]

for element in lista:
    print(element)

print('\n')


#######################################################################################
print(' ---- Iterate 10 to 0 using for loop, do the same using while loop. ----')

index = 0

while index < len(lista) and lista[index]<11:
    print(lista[index])
    index += 1

print('\n')


#######################################################################################
print(' ---- Write a loop that makes seven calls to print(), so we get on the output the following triangle: ----')

triangle = 7
simbolo = '#'

for i in range(1,8):
    print('#' * i)
    i += 1

print('\n')

#######################################################################################
print(' ---- Use nested loops to create un cuadrado de 8x8 con * ----')

for i in range(8):
    for j in range(8):
        print('*', end = " ")
    print("")

print('\n')


#######################################################################################
print(' ---- Titulo to Modify ----')
for i in range (11):
    print(f"{i} x {i} = {i * i}")
    
print('\n')


#######################################################################################
print(' ---- Iterate through the list, using a for loop and print out the items. ----')

skills = ['Python', 'Numpy','Pandas','Django', 'Flask']

for element in skills:
    print(element)

print('\n')


#######################################################################################
print(' ---- Use for loop to iterate from 0 to 100 and print only even numbers ----')
for i in range(101):
    if i % 2 == 0:
        print(i)

print('\n')


#######################################################################################
print(' ---- Use for loop to iterate from 0 to 100 and print only odd numbers ----')
for i in range(100):
    if i % 2 !=0:
        print(i)
print('\n')


#######################################################################################
print(' ---- Use for loop to iterate from 0 to 100 and print only odd numbers ----')
suma = 0

for i in range(101):
    suma += i
    if i == 100:
        print(f"The sum is {suma}")
print('\n')




#######################################################################################
print(' ---- Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds. ----')
suma_pares = 0
suma_impares = 0

for i in range (101):
    if i % 2 == 0:
        suma_pares += i
    elif i % 2 != 0:
        suma_impares += i

print(f"La suma de los pares es = {suma_pares}")
print(f"La suma de los impares es = {suma_impares}")
print('\n')




#######################################################################################
print(' ---- Loop through the countries and extract all the countries containing the word land. ----')

from countrys_data import countries

for i in countries:
    if len(i) < 5:
        print(i)
print('\n')
