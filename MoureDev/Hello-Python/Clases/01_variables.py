print(' ---- Variables ----')
print('\n')

######################
print(' ---- String ----')
my_string_variable = 'My String variable...'
print(my_string_variable)
print(type(my_string_variable))
print('\n')

######################
print(' ---- Booleano ----')
my_bool_variable = False
print(my_bool_variable)
print(type(my_bool_variable))
print('\n')

######################
print(' ---- Int ----')
my_int_variable = 5
print(my_int_variable)
print(type(my_int_variable))
print('\n')

######################
print(' ---- Concatenar Variables ----')
print(my_string_variable, my_int_variable, my_bool_variable)
print('Este es el valor de:', my_bool_variable)
print('\n')

######################
print(' ---- Convertir de Int a String ----')
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))
print('\n')

######################
print(' ---- Len ----')
print(my_string_variable)
print(len(my_string_variable))
print('\n')

######################
print(' ---- Variables en una sola linea ----')
name, surname, alias, age = 'Carlos', 'Morales', 'Carlitos', 33
print('Me llamo:', name, surname, '. Mi edad:', age, '. Mi alias:', alias)
print('\n')

######################
print(' ---- El nombre de la variable no define el tipo de dato ----')
name = 35
print(name)
print(type(name))
age = 'Carlitos'
print(age)
print(type(age))
print('\n')

######################
print(' ---- ¿Forzamos el tipo?  ----')
address: str = "Mi dirección"
address = True
address = 5
address = 1.2
print(type(address))
print('\n')

######################
print(' ---- Inputs ----')
name_new = input('¿Cuál es tu nombre? ')
age_new = input('¿Cuántos años tienes? ')
print(name_new)
print(age_new)
print('\n')