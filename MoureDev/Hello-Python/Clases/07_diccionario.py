# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc

### Dictionaries ###

# Definición

my_dict = dict()  
my_other_dict = {} #Se crea con la misma sintaxis que Set,  pero el dict va tener key and value


print(' ---- Dict Vacios ----')
print(type(my_dict))
print(type(my_other_dict))
print('\n')

print(' ---- Dict con Datos ----')
my_other_dict = {"Nombre": "Brais",
                "Apellido": "Moure", "Edad": 35, 1: "Python"}

my_dict = {
    "Nombre": "Brais",
    "Apellido": "Moure",
    "Edad": 35,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.77
}

print(my_other_dict)
print(my_dict)
print('\n')


print(' ---- Dict Length ----')
print(len(my_other_dict))
print(len(my_dict))
print('\n')


print(' ---- Dict Imprimir Values por medio del indice o nombre del elemento ----')
print(my_dict[1])
print(my_dict["Nombre"])
print('\n')


print(' ---- Dict Verificar si hay los siguientes values ----')
print("Moure" in my_dict)
print("Apellido" in my_dict)
print('\n')



# Inserción
print(' ---- Dict Insertar valores ----')
my_dict["Calle"] = "Calle MoureDev" ##  Si el elemento  Calle existiese antes, entonces cambiaria su valor. 
print(my_dict)
print('\n')


# Actualización
print(' ---- Dict Cambiar valores ----')
my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])
print('\n')


# Eliminación
print(' ---- Dict Eliminar Key Calle ----')
del my_dict["Calle"]
print(my_dict)
print('\n')


# Otras operaciones
print(' ---- Dict Obtener Items Listado de key, values ----')
print(my_dict.items())
print('\n')


print(' ---- Dict Obtener Keys - Values ----')
print(my_dict.keys())
print(my_dict.values())
print('\n')



my_list = ["Nombre", 1, "Piso"]
my_new_dict = dict.fromkeys((my_list))
#print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
#print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict)
#print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict, "MoureDev")
#print((my_new_dict))

my_values = my_new_dict.values()
#print(type(my_values))

#print(my_new_dict.values())
#print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
#print(tuple(my_new_dict))
#print(set(my_new_dict))