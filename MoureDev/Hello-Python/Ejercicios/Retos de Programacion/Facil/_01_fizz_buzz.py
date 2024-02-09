print(' ---- Titulo to Modify ----')

# /*
#  * Escribe un programa que muestre por consola (con un print) los
#  * números de 1 a 100 (ambos incluidos y con un salto de línea entre
#  * cada impresión), sustituyendo los siguientes:
#  * - Múltiplos de 3 por la palabra "fizz".
#  * - Múltiplos de 5 por la palabra "buzz".
#  * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
#  */

print('\n')

print(' ---- fizz buzz ----')
for i in range(1,101):
    if i%3 ==0 and i%5 == 0:
        print(f"FizzBuzz   {i/3}, {i/5} ")
    elif i %3 ==0:
        print(f"Fizz       {i/3}")
    elif i %5 == 0:
        print(f"buzz       {i/5}")
    else:
        print(i)
print('\n')