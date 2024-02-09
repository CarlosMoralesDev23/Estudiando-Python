print('----- Mas funciones -----')
print('\n')

######################    help()    ########################## 
print('--- help permite obtener infoarm() ---')  
print('--- permite obtener informacion de un def, de cualquier codigo, help() ---')  

def saludar(nombre):
    print(f"Hola, {nombre}!")

help(saludar)
print('\n')


######################    hex()    ########################## 
print('--- hex() ---')  
print('--- Permite convetir un entero a hexadecimal, hex() ---')
numero = 255 
texto = '0xff'
print(f"Número entero: {numero}")
print(f"Número hexadecimal: {hex(numero)}")
print(f"Número hexadecimal: {int(texto, 16)}") #16 para indicar que sera formato hexadecimal
print('\n')


######################    id()    ########################## 
print('--- id() ---')  
print('--- Permite asignarle un id a objetos, id() ---')

objeto = [1, 2, 3]
identificador = id(objeto)

print(f"Objeto: {objeto}")
print(f"Identificación única: {identificador}")
print('\n')


######################    input()    ########################## 
print('--- input() ---')  
print('--- Permite obtener info del usuario, input() ---')

nombre_usuario = input("Por favor, ingresa tu nombre: ")
print(f"Hola, {nombre_usuario}!")
print('\n')

######################    int()    ########################## 
print('--- int() ---')  
print('--- Permite convertir elementos a int, int() ---')
print(f"Número entero desde cadena: {type(int("123"))}")
print(f"Número entero desde flotante: {type(int(3.14))}")
print(f"Número entero desde hexadecimal: {type(int("1a", 16))}")
print('\n')

######################    len()    ########################## 
print('--- len() ---')  
print('--- Saber la cantidad de elementos que continee, len() ---')

print(f"Longitud de la lista: {len([1, 2, 3, 4, 5])}")
print(f"Longitud de la cadena: {len("Hola, mundo!")}")
print(f"Longitud del diccionario: {len({"a": 1, "b": 2, "c": 3})}")




'''
Pendientes

getattr()
globals()
hasattr()
hash()
isinstance()
issubclass()
locals()


'''



