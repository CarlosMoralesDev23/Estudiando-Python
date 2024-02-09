print('----- Mas funciones -----')

######################    abs()    ########################## 
print('--- Valor absoluto abs(13 y -13) ---')  
print(abs(13))
print(abs(-13))
print('\n')


######################    all()    ########################## 
print('--- Confirmacion de cumplimiento de todas, all(condicion) ---')  ### all()
print('Los estudiantes aprobaron...')
calificaciones = [75, 82, 60, 95, 78]
todos_aprobaron = all(calificacion >= 60 for calificacion in calificaciones)
print(todos_aprobaron)
if todos_aprobaron:
    print("Todos los estudiantes aprobaron")
else:
    print("Al menos un estudiante no aprobo.")
print('\n')


print('-----------------------------------------------------------------------')
print('Ejemplo_2 de all() la longitud de sublistas')

listas = [[1, 2, 3], [4, 5, 6], [7, 8]]
todas_longitudes_validas = all(len(sublista) >= 3 for sublista in listas)
print(todas_longitudes_validas)
if todas_longitudes_validas:
    print("Todas las sublistas tienen al menos longitud 3.")
else:
    print("Al menos una sublista no tiene longitud 3.")
print('\n')


######################    any    ########################## 
print('--- Confirmacion de cumplimiento de alguno, any(condicion) ---')  ### any()
valores = [False, 0, "", None, True, 42, "Hola"]
print(any(valores))
print(not any(valores))
print('\n')


######################    bin    ########################## 
print('--- Obtener valores Binarios, bin() ---')  ### bin()
print(bin(42))
print('\n')

######################    bool    ########################## 
print('--- verificar tipo de booleano, bool() ---')  ### bool()

print(bool(False))
print(bool(0))
print(bool(1))
print(bool(-1))
print(bool(True))
print(bool(42))
print(bool('Hola'))
print('\n')


######################    breakpoint    ########################## 
print('------ breakpoint() ------')
def operacion_complicada(x, y):
    resultado = x + y
    breakpoint()#punto de interrupción aquí
    resultado += x-y
    return resultado
#llamada a la función
resultado_final = operacion_complicada(5, 3)
print('Resultado final:', resultado_final)
print('\n')

'''
Pendientes
aiter()
anext()
ascii()
bytearray()
bytes()


'''