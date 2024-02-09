print(' ---- #8 Print_list ----')
def print_list(lista):
    for element in lista:
        print(element)

print_list(["a", 5, 8, "t", 9])
print('\n')



print(' ---- #9 Reverse_list ----')
def reverse_list(lista):
    lista.reverse()
    print(lista)
reverse_list([1, 2, 3, 4, 5])
print('\n')


print(' ---- #10 capitalize_list_items ----')
def capitalize_list_items(lista):
    lista_capitalizada = [item.capitalize() for item in lista]
    return print(lista_capitalizada)
capitalize_list_items(["caracas", "venezuela", "madrid"])
print('\n')


print(' ---- #11 add_item ----')
def add_item(lista):
    new_item = input("Agrega un nuevo item: ")
    lista.append(new_item)
    return lista
nueva_lista = add_item([1, 2, 3])
print(nueva_lista)
print('\n')


print(' ---- #12 remove_item ----')
def remove_item(lista):
    index_removed = int(input("Cul index quieres remover: "))
    del lista[index_removed]
    return lista
otra_lista = remove_item([1, 2, 3, 4, 6, 8, 10, 15, 22])
print(otra_lista)
print('\n')





'''

It returns a list with the item removed from it.

'''