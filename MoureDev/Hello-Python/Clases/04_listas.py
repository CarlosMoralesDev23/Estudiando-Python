print(' ---- Lists ----')
my_list = list()  # Se crea una lista vacia
my_other_list = [] #Tambien se puede crear asi
print(my_list)
print(my_other_list)
print(len(my_list))
print('\n')


print(' ---- Imprimir Lista ----')
my_list = [35, 24, 62, 52, 30, 30, 17] # Cargue datos a la lista
print(my_list)
print(len(my_list))
print('\n')
 

print(' ---- Type Lista ----')
my_other_list = [35, 1.77, "Brais", "Moure"] # Cargue datos a otra lista
print(type(my_list))
print(type(my_other_list))
print('\n')


print(' ---- Acceder a elementos ----')
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
# print(my_other_list[4]) Index Error No existe
# print(my_other_list[-5]) Index Error   No existe
print('\n')


print(' ---- Cuenta la concurrencias de un mismo elemento ----')
print(my_list.count(30)) # Cuenta el numero de concurrencias
print('\n')


print(' ---- Destructuras Variales/Elementos ----')
age, height, name, surname = my_other_list #se debe asignar tantas variables como elementos tenga la lista
print(age)
print('\n')


print(' ---- Concatenenar Listas ----')
print(my_list + my_other_list)
#print(my_list - my_other_list)
print('\n')


print(' ---- Agregar elementos con Append ----')
my_other_list.append("MoureDev")
print(my_other_list)
print('\n')


print(' ---- Insertar elementos con Insert ----')
my_other_list.insert(1, "Rojo") ## Inserto en el indice 1, "Rojo"
print(my_other_list)
print('\n')


print(' ---- Cambia elemento por medio del indice ----')
my_other_list[1] = "Azul"  ## Cambio en el indice 1, "Rojo" por "Azul"
print(my_other_list)
print('\n')


print(' ---- Remover elementos ----')
my_other_list.remove("Azul") ## Saco el dato azul de la lista. 
print(my_other_list)
print('\n')


print(' ---- Remover elementos por la primera concurrencia ----')
print(my_list)
my_list.remove(30) ## Remuevo el primer valor 30 que encuentre. 
print(my_list)
print('\n')


print(' ---- Remover el último elemento ----')
print(my_list.pop()) ## Remueve el ultimo que seria el 17
print(my_list)
print('\n')


print(' ---- Remueve un elemento y lo guarda en otra variable ----')
my_pop_element = my_list.pop(2) ## Remuevo el dato de la posición 2 (62)  y lo guardo en una variable
print(my_pop_element)
print(my_list)
print('\n')


print(' ---- Eliminar un elemento por indice ----')
del my_list[2] ## borra el dato del indice 2
print(my_list)
print('\n')


print(' ---- Copiar una lista y guardarla en otra variable ----')
my_new_list = my_list.copy()  ## Hace una copia de la lista y se guarda en una variable
print('\n')


print(' ---- Limpiar/Vaciar la lista ----')
my_list.clear() # Borra todo el contenido de la lista
print(my_list)
print(my_new_list)
print('\n')


print(' ---- Poner al reves el orden de la lista ----')
my_new_list.reverse() #Revierte el orden de los datos de la lista
print(my_new_list)
print('\n')


print(' ---- Ordenar la lista de Menor a Mayor ----')
my_new_list.sort() # Ordena la lista de menor a mayor
print(my_new_list)
print('\n')


print(' ---- Tomar una parte de la Lista ----')
print(my_new_list[1:3]) # toma una parte de la lista
print('\n')


print(' ---- cambio la lista por una cadena de texto ----')
my_list = "Hola Python"
print(my_list)
print(type(my_list))
print('\n')

