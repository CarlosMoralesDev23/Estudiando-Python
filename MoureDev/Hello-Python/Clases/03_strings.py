print(' ---- Strings ----')
print('\n')
my_strings = "Mi string"
my_other_strings = "Mi otro string"


print(' ---- Largo del String ----')
print(len(my_strings))
print(len(my_other_strings))
print('\n')


print(' ---- Concatenar Strings ----')
print(my_strings + ' ' + my_other_strings)
print('\n')


print(' ---- Este es un string \ncon salto de línea ----')
my_new_line_string = 'Este es un string \ncon salto de línea'
print(my_new_line_string)
print('\n')


print(' ---- Este es un string con tabulación ----')
my_tab_string = '\tEste es un string con tabulación'
print(my_tab_string)
print('\n')


print(' ---- Este es un string con tabulación y salto ----')
my_scape_string = '\tEste es un string \n escapado'
print(my_scape_string)
print('\n')


print(' ---- Combinación de String con Variables ----')
name, surname, age = 'Carlos', 'Morales', 33
print("Mi nombre es {} {} y mi edad es {}" .format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")
print('\n')


print(' ---- Desempaqueado de caracteres ----')
language = "python"
a, b, c, d, e, f = language
print(a)
print(e)
print('\n')


print(' ---- División - slice de Strings ----')
language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)
print('\n')


print(' ---- Reverse de Strings ----')
reversed_language = language[::-1]
print(reversed_language)
print('\n')


print(' ---- Funciones del lenguaje ----')
print(language.capitalize())
print(language.upper())
print(language.count("p"))  #Cuantas veces aparece esa letra
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.lower().isupper())
print(language.startswith("Py"))
print("Py" == "py")  # No es lo mismo
print('\n')
