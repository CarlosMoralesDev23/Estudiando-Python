# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=16335

### Sets ###

# Definición

my_set = set()
my_other_set = {}  ## Cuando lo declaramos con {} Inicialmente se crea como diccionario cuando esta vacío

print(type(my_set))
print(type(my_other_set))  # Inicialmente es un diccionario

my_other_set = {"Brais", "Moure", 35} 
print(type(my_other_set))

print(len(my_other_set))

# Inserción

my_other_set.add("MoureDev")

print(my_other_set)  # Un set no es una estructura ordenada

my_other_set.add("MoureDev")  # Un set no admite repetidos

print(my_other_set)

# Búsqueda

print("Moure" in my_other_set)
print("Mouri" in my_other_set)

# Eliminación

my_other_set.remove("Moure")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
# print(my_other_set) NameError: name 'my_other_set' is not defined

# Transformación

my_set = {"Brais", "Moure", 35}
my_list = list(my_set)     ## Convertir el set a una lista, asi seria ordenada y mutable.  
print(my_list)
print(my_list[0])

my_other_set = {"Kotlin", "Swift", "Python"}

# Otras operaciones

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))

print(my_new_set.difference(my_set)) ## muestra los elementos que trajo my_set que son diferentes a my_new_set

## 

my_tupla_1_5 = {1, 2, 3, 4, 5, 6}
my_tupla_3_8 = {3, 4, 5, 6, 7, 8}

print(my_tupla_1_5.union(my_tupla_3_8))

'''
print('-----------------')
my_tupla_numeros = my_tupla_3_8 + my_tupla_1_5
print(my_tupla_numeros)
'''  # NO se pueden unir tuplas usando el operador +