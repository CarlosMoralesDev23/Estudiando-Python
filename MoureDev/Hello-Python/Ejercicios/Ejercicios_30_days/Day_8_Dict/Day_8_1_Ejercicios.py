my_set = {"---- # sets ----"}

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(type(my_set))

print(' ---- Exercises: Level 1 ----')
print('\n')

print(' ---- #1 - Find the length of the set it_companies ----')
print(f"El largo del set es {len(it_companies)}")
print('\n')

print(" ---- #2 - Add 'Twitter' to it_companies ----")
it_companies.add("Twiter")
print(it_companies)
print('\n')

print(' ---- #3 - Insert multiple IT companies at once to the set it_companies ----')
it_companies = it_companies.union({"Samsung", "Boldt", "Tsoft"}) #Sin corchetes no se unen
print(it_companies)
it_companies.update({"Nokia", "Iphone", "Motorola"}) #Sin corchetes se agregan las letras de cada String
print(it_companies)
print('\n')

print(' ---- #4 - Remove one of the companies from the set it_companies ----')
it_companies.remove('Twiter')
print(it_companies)
print('\n')

print(' ---- #5 - What is the difference between remove and discard ----')
#it_companies.remove("Corsa") ### Imprime un KeyError por no encontrar el elemento
it_companies.discard("Ford") ### NOOO imprime un KeyError por no encontrar el elemento, no informa nada, ni imprime nada. 
print('\n')
print('\n')


print(' ---- Exercises: Level 2 ----')
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


print(' ---- #1 Join A and B ----')
join_a_b = A.union(B)
print(join_a_b)
print('\n')



print(' ---- #2 - Find A intersection B ----')
print(A.intersection(B))
print('\n')

print(' ---- #3 - Is A subset of B ----')
print(A.issubset(B))
print('\n')

print(' ---- #4 - Are A and B disjoint sets ----')
print(A.isdisjoint(B))
print('\n')

print(' ---- #5 - Join A with B and B with A ----')
join_b_a = B.union(A)
print(join_a_b)
print(join_b_a)
print('\n')

print(' ---- #6 - What is the symmetric difference between A and B ----')
print(A.symmetric_difference(B))
print('\n')


print(' ---- #7 - Delete the sets completely ----')
del A
del B
del join_a_b
del join_b_a
print('\n')
print('\n')


print(' ---- Exercises: Level 3 ----')
print(' ---- #1 - Convert the ages to a set and compare the length of the list and the set, which one is bigger? ----')
age = [22, 19, 24, 25, 26, 24, 25, 24]
age_set = set(age)
print(f"El largo de la lista es {len(age)}")
print(f"El largo del set es {len(age_set)}")  #El lenght es mas corto porque el set no admite elementos duplicados
print('\n')


print(' ---- #2 - Explain the difference between the following data types: string, list, tuple and set ----')

print('\n')

print(' ---- # 3 - I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and #set to get the unique words. ----')
unique_words = "I am a teacher and I love to inspire and teach people"
unique_words = unique_words.split()
set_unique_words = set(unique_words)
print(set_unique_words)
print(f"La oración solo tiene {len(set_unique_words)} palabras unicas")
print('\n')


