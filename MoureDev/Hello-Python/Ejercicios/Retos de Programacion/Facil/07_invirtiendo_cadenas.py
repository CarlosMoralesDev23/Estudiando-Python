def  cadena_reves(cadena):
    nueva_cadena = ""

    for e in range(len(cadena)-1, -1, -1):
        nueva_cadena += cadena [e]

    return nueva_cadena

cadena = "Hola mundo"
print(cadena_reves(cadena))


'''

    for e in range(length -1, -1, -1):
        indice_e = cadena.index(e)
        print(indice_e)


        Quiero hacer la resta del length con el indice actual de cada elemento de cadena.

        Ejemplo
        Hola mundo
        aca el lenght es 9.
        en el incide 0 esta la H. 
        Si resto len(9) - indice(0) me da 9.
        y proceder a ubicar esa H en en indice 9. 

        cuando le toque a la ó
        esta en la posicion 1
        leng 9 menos posicion 1 da 8, posicionarlo ahora en el indice 8. 
        '''






'''

#7
INVIRTIENDO CADENAS
/*
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 */

'''