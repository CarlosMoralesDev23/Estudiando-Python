print(' ---- Fibonacci con Variables ----')
numero1 = 0
numero2 = 1
while numero2 <= 1597:
    print(numero1, numero2, end=" ")
    numero1 = numero1+ numero2
    numero2 = numero1 + numero2
print('\n')


print(' ---- Fibonacci con lista ----')
lista_fibonacci = []
while len(lista_fibonacci) <= 15:
    if len(lista_fibonacci) == 0:
        lista_fibonacci.append(0)
        lista_fibonacci.append(1)
    elif len(lista_fibonacci) > 0 :
        lista_fibonacci.append(lista_fibonacci[-2] + lista_fibonacci[-1])
print(lista_fibonacci)
print('\n')


print(' ---- Fibonacci con Funcion y for ----')
def fibonacci(num):
    fib = [0, 1]
    for i in range (2, num):
        fib.append(fib[i-1] + fib[i-2])
    return fib
print(fibonacci(10))
print('\n')
