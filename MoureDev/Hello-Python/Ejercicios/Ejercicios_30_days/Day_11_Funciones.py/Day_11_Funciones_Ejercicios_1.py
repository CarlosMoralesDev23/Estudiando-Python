print(' ---- #1 Declare a function add_two_numbers. It takes two parameters and it returns a sum. ----')
def add_two_numbers(number_1, number_2):
    return number_1 + number_2
sum = add_two_numbers( 10, 15)
print(sum)
print('\n')



print(' ---- #2 Area of a circle is calculated as follows:  Write a function that calculates area_of_circle. ----')
def area_of_circle(radio, pi = 3.14):
    area_circle = pi * (radio**2)
    print(area_circle)
area_of_circle(5)
print('\n')


print(' ---- #3 Suma los elementos int de una lista ----')
lista_number = []
lista_number.append(1)
lista_number.append(3)
lista_number.append("Diez")
lista_number.append(5)
lista_number.append(8)

def add_all_nums(lista_number):
    print(lista_number)
    sum = 0
    for num in lista_number:
        if isinstance(num, int):
            sum += num
        else:
            print("No se puede sumar sino es int")
    return print(sum)
add_all_nums(lista_number)
print('\n')