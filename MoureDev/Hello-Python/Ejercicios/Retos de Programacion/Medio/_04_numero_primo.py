print(' ---- ¿ES UN NÚMERO PRIMO? - Medio ----')
#  * Escribe un programa que se encargue de comprobar si un número es o no primo.
#  * Hecho esto, imprime los números primos entre 1 y 100.
#  */

def es_primo(numero):
    if numero < 2  or numero%2 ==0:
        return False  
    if numero == 2 :
        return True
    else:
        for i in range(3, int(numero**0.5) + 1, 2):
            if numero %i == 0:
                return False
        return True
        


def numeros_primos(cantidad):
    for numero in range(2, cantidad+1):
        if es_primo(numero):
            print(numero)

numeros_primos(100)