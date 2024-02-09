print(' ---- ÁREA DE UN POLÍGONO ----')

def area_poligono(tipo_poligono, *args):
    print(args)
    print(tipo_poligono)

    lista_args = list(args)
    print(lista_args)


base= 0
altura = 0
lado = 0



area_triangulo = (base * altura)/2
area_rectangulo = lado * altura
area_cuadrado = lado * lado



area_poligono("Triangulo", 1,2,3)
print('\n')



'''



/*
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */

'''