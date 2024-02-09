import math
#Day 3: 30 Days of python programming'

# 1 - Declare your age as integer variable 
age = 33
# 2 - Declare your height as a float variable
height = 1.70
# 3 -Declare a variable that store a complex number
number_complex = 3 + 5j

# 4 - Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
print("---- Calculating area of triangle ----")
base = float(input("Base del triangulo: "))
height_triangle = float(input("Height del triangulo: "))
print(f"Area of triangle: {((0.5 * base) * height_triangle)}")

# 5 - Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
print("---- Calculating perimeter of triangle ----")
side_a = int(input("Side A: "))
side_b = int(input("Side B: "))
side_c = int(input("Side C: "))
print(f"El perimetro del triangulo es: ${side_a + side_b + side_c}")

# 6 - Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
print("---- Calculating Area and Perimeter of rectangle ----")
length_rectangle = int(input("Length: "))
width_rectangle = int(input("Width: "))
print(f"El area del rectangle es: ${length_rectangle * width_rectangle} y su perimetro es: ${(2 * (length_rectangle + width_rectangle))}")

# 7 - Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
    # radio = int(input("Radio: "))
    # pi = 3.14
    # area_circle = pi * (radio**2)
    # print(f"El area del cirulo es: ${area_circle}")

# 8 -Calculate the slope, x-intercept and y-intercept of y = 2x -2
    # x_intercept = int(input("X-Intercept: "))
    # y_intercept = (2 * x_intercept) - 2
    # print(f"El slope y es: ${y_intercept}")


# 9 - Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
    # y_2 = 6
    # y_1 = 2
    # x_2 = 10
    # x_1 = 2

    # m = (y_2 - y_1) / (x_2 - x_1)

    # print(f"La distancia entre los dos puntos es: ${m}")



# 10 - Compare the slopes in tasks 8 and 9.
