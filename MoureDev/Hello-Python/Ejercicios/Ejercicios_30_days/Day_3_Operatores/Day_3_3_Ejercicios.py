import math
#Day 3: 30 Days of python programming'

# 11 - Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
    # x = -3
    # y = (x**2) + (6 * x) + 9
    # print(f"El valor de x es: ${y}")

    # x_1 = -2
    # y_2 = (x_1**2) + (6 * x_1) + 9
    # print(f"El valor de x es: ${y_2}")


# 12 - Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(f"Python y Dragon tienen la misma longuitud : ${((len("python")) == ((len("dragon"))))}")


# 13 - Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("on" in "python" and "on" in "dragon")

# 14 - a hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print("jargon" in "a hope this course is not full of jargon.")

# 15 - There is no 'on' in both dragon and python
print("no" in "python" and "on" in "dragon")

# 16 - Find the length of the text python and convert the value to float and convert it to string
print(type(str(float(len("python")))))

# 17 - Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
numero = int(input("numero : "))
print(f"El numero ${numero} es divisible entre 2: {(numero % 2) == 0}" )