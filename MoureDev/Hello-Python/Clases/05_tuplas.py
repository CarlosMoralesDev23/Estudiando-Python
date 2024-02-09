print(' ---- Tuples ----')
my_tuple = tuple() # La lista se crea con list()
my_other_tuple = () # La lista se crea con []
my_tuple = (35, 1.77, "Brais", "Moure", "Brais")
my_other_tuple = (35, 60, 30)
print('\n')


print(' ---- Tipo de dato de la tupla ----')
print(my_tuple)
print(type(my_tuple))
print('\n')


print(' ---- Acceder a los elementos de un tupla por su INDICE ----')
print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) IndexError   NO EXISTE EL INDICE
# print(my_tuple[-6]) IndexError  NO EXISTE EL INDICE
print('\n')


print(' ---- Verificar la concurrencia de un elemento ----')
print(my_tuple.count("Brais"))
print('\n')


print(' ---- verificar el indice de un elemento ----')
print(my_tuple.index("Moure"))
print(my_tuple.index("Brais"))
print('\n')


print(' ---- Las tuplas NO SE PUEDEN MODIFICAR ----')
# my_tuple[1] = 1.80 'tuple' object does not support item assignment
print('\n')


print(' ---- Tupla mutable por conversión a lista ----')
my_tuple = list(my_tuple)
print(type(my_tuple))
print('\n')


print(' ---- Concatenación de 2 tuplas ----')
my_tuple = tuple(my_tuple)
my_sum_tuple = my_tuple + my_other_tuple ## Se pueden concatener 2 tuplas y asignarlo a una nueva variable. 
print(my_sum_tuple)
print('\n')


print(' ---- Subtuplas ----')
print(my_sum_tuple[3:6])
print('\n')


print(' ---- Cambiar el elemento mediante el indice ----')
print(f" No se puede cambiar los elemento de una tupla, se debe cambia a una lista y luego cambiarlo")
#my_tuple[4] = "MoureDev"
print('\n')


print(' ---- Insertar elemento  ----')
print(f" No se puede insertar elementos de una tupla, se debe cambia a una lista y luego cambiarlo")
##my_tuple.insert(1, "Azul")
print('\n')


print(' ---- Eliminación d euna tupla ----')
# del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion

del my_tuple
# print(my_tuple) NameError: name 'my_tuple' is not defined

## del no es una funcion de lista y tuplas, es global a todo el sistema - codigo.
print('\n')