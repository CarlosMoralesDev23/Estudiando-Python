# 1 - Create an empty tuple
print(' ---- Create an empty tuple ----')
my_tupla = tuple()
print(my_tupla)
print('\n')

# 2 - Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
print(' ---- Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine) ----')
my_sisters = ("Yamailet", "Karla", "Francis", "Yauri", "Peggy", "Yaicy")
my_brothers = ("Rafael", "Cristian", "Felipe", "Machado")
print(my_sisters)
print('\n')

# 3 - Join brothers and sisters tuples and assign it to siblings
print(' ---- Join brothers and sisters tuples and assign it to siblings ----')
my_siblings = my_sisters + my_brothers
print(my_siblings)
print('\n')


# 4 - How many siblings do you have?
print(' ---- How many siblings do you have? ----')
print(f"Tengo {len(my_siblings)} Siblings")
print('\n')

# 5 - Modify the siblings tuple and add the name of your father and mother and assign it to family_members
print(' ---- Modify the siblings tuple and add the name of your father and mother and assign it to family_members ----')
my_family = list(my_siblings)
my_family.append("Ana")
my_family.append("Carlos")
my_family = tuple(my_family)
print(my_family)
print('\n')

print(' -------- Exercises: Level 2 --------')
print('\n')

# 6 - Unpack siblings and parents from family_members
print(' ---- Unpack siblings and parents from family_members ----')
my_fathers = my_family[10:12]
my_siblings = my_family[0:10]
print(my_fathers)
print(my_siblings)
print('\n')

# 7 - Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
print(' ---- join the three tuples and assign it to a variable called food_stuff_tp. ----')
fruits = ("Naranja", "Manzana", "Pera")
vegetables = ("Papa", "Zanahoria", "Batata")
animals= ("Perro", "Gato", "Conejo")
food_stuff_tp = fruits + vegetables + animals 
print(food_stuff_tp)
print(type(food_stuff_tp))
print('\n')

# 8 - Change the about food_stuff_tp tuple to a food_stuff_lt list
print(' ---- Change the about food_stuff_tp tuple to a food_stuff_lt list ----')
food_stuff_tl = list(food_stuff_tp)
print(type(food_stuff_tp))
print(type(food_stuff_tl))
print('\n')

# 9 - Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print(' ---- Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list. ----')
middle_index = len(food_stuff_tp) // 2

# Seleccionar el elemento o elementos del medio
middle_item = food_stuff_tp[middle_index]  # Para una longitud impar
#middle_items = food_stuff_tp[middle_index - 1:middle_index + 1]  # Para una longitud par
print("Elemento del medio:", middle_item)
#print("Elementos del medio:", middle_items)
print('\n')



# 10 - Slice out the first three items and the last three items from food_staff_lt list
print(' ---- Slice out the first three items and the last three items from food_staff_lt list ----')
print(f"La tupla completa es {food_stuff_tp}")

#primeros 3
three_first = food_stuff_tp[0:3]
print(f"Los primeros 3 elementos son {three_first}")

#ultimos 3
three_last = food_stuff_tp[(len(food_stuff_tp)-3):len(food_stuff_tp)]
print(f"Los ultimos 3 elementos son {three_last}")
print('\n')

# 11 - Delete the food_staff_tp tuple completely
print(' ---- Delete the food_staff_tp tuple completely ----')
del food_stuff_tp
#print(food_stuff_tp)
print('\n')

# 12 -Check if an item exists in tuple:
print(' ---- Check if an item exists in tuple: ----')
#Check if 'Estonia' is a nordic country
#Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
print('\n')

