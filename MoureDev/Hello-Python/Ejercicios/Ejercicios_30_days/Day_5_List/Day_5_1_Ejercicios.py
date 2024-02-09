print("---- End with a substring Coding? ----")
print("\n")

# 1 - Declare an empty list
print("---- Declare an empty list ----")
list_empty = []
print(list_empty)
print("\n")

# 2 - Declare a list with more than 5 items
print("---- Declare a list with more than 5 items ----")
my_list_8_item = [ 1 , 2 , 3 , 4 , 5, 6 , 7 , 8]
print(my_list_8_item)
print("\n")

# 3 - Find the length of your list
print("---- Find the length of your list ----")
print(len(my_list_8_item))
print("\n")

# 4 - Get the first item, the middle item and the last item of the list
print("---- Get the first item, the middle item and the last item of the list ----")
first_item = my_list_8_item[0]
last_item = my_list_8_item[-1]
middle_item = my_list_8_item[len(my_list_8_item)//2]
print(first_item, middle_item, last_item)
print("\n")

# 5 - Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
print("---- Declare a list (name, age, height, marital status, address) ----")
mixed_data_types = ["Carlos", 33, 1.68, "casado", "Argentina"]
print(mixed_data_types)
print("\n")

# 6 - Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
print("----  list named it_companies values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon. ----")
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)
print("\n")

# 7 - Print the list using print()
print("---- Print the list using print() ----")
print(it_companies)
print("\n")


# 8 - Print the number of companies in the list
print("---- Print the number of companies in the list ----")
print(f"Son {len(it_companies)} companies")
print("\n")


# 9 - Print the first, middle and last company#  - 
print("---- Print the first, middle and last company#  ----")
first_company = it_companies[0]
last_company = it_companies[-1]
middle_company = it_companies[len(it_companies)//2]
print(first_company, middle_company, last_company)
print("\n")


# 10 - Print the list after modifying one of the companies
print("---- Print the list after modifying one of the companies  ----")
print(it_companies)
it_companies[-1] = "Boldt"
print(it_companies)
print("\n") 


# 11 - Add an IT company to it_companies
print("---- Add an IT company to it_companies ----")
it_companies.append("Samsung")
print(it_companies)
print("\n")

# 12 - Insert an IT company in the middle of the companies list
print("---- Insert an IT company in the middle of the companies list ----")
middle_company = it_companies[len(it_companies)//2] #Esto me entrega es elnombre de la company del medio. 
medio_index = len(it_companies) // 2 #Esto me entrega es el index del medio de it_company
print(medio_index)
it_companies.insert(medio_index, "ASUS")
print(it_companies)
print("\n")

# 13 - Change one of the it_companies names to uppercase (IBM excluded!)
print("---- Change one of the it_companies names to uppercase (IBM excluded!) ----")
it_companies[0] = it_companies[0].upper()
it_companies[1] = it_companies[1].upper()
it_companies[2] = it_companies[2].upper()
it_companies[3] = it_companies[3].upper()
it_companies[4] = it_companies[4].upper()
it_companies[5] = it_companies[5].upper()
it_companies[7] = it_companies[7].upper()
it_companies[8] = it_companies[8].upper()
print(it_companies)
print("\n")

# 14 - Join the it_companies with a string '#;  '0
print("---- Join the it_companies with a string '#; ----")
it_companies_separada = "#; ".join(it_companies)
print(it_companies_separada)
print("\n")

# 15 - Check if a certain company exists in the it_companies list.
print("---- Check if a certain company exists in the it_companies list. ----")
it_companies_exist = "IBM" in it_companies
print(it_companies_exist)
print("\n")

# 16 - Sort the list using sort() method
print("---- Sort the list using sort() method. ----")
it_companies.sort()
print(it_companies)
print("\n")

# 17 - Reverse the list in descending order using reverse() method
print("---- Reverse the list in descending order using reverse() method ----")
it_companies.reverse()
print(it_companies)
print("\n")

# 18 - Slice out the first 3 companies from the list
print("---- Slice out the first 3 companies from the list ----")
it_companies_slice = it_companies[0:3] #Excluye el elemento del indice 3. 
print(it_companies_slice)
print("\n")

# 19 - Slice out the last 3 companies from the list
print("---- Slice out the last 3 companies from the list ----")
it_companies_slice = it_companies[(len(it_companies)-3):(len(it_companies))] #Excluye el elemento del indice 3. 
print(it_companies_slice)
print("\n")

# 20 - Slice out the middle IT company or companies from the list
print("---- Slice out the middle IT company or companies from the list ----")
medio_index = len(it_companies) // 2
print(medio_index)
print(it_companies)
del it_companies[medio_index]
print(it_companies)
print("\n")

# 21 - Remove the first IT company from the list
print("---- Remove the first IT company from the list ----")
del it_companies[0]
print(it_companies)

print("\n")

# 22 - Remove the middle IT company or companies from the list
print("---- Remove the middle IT company or companies from the list ----")
medio_index = len(it_companies) // 2
print(medio_index)
print(it_companies)
del it_companies[medio_index]
print(it_companies)
print("\n")


# 23 - Remove the last IT company from the list
print("---- Remove the last IT company from the list ----")
del it_companies[-1]
print(it_companies)
print("\n")

# 24 - Remove all IT companies from the list
print("---- Remove all IT companies from the list ----")
it_companies.clear()
print(it_companies)
print("\n")

# 25 - Destroy the IT companies list
print("---- Destroy the IT companies list ----")
del it_companies
#print(it_companies)
print("\n")


# 26 - Join the following lists:
print("---- Join the following lists: ----")
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)
print("\n")

# 27 - After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
print("---- Copy the joined list and assign it to a variable full_stack ----")
full_stack = front_end + back_end
full_stack.insert(5, "Python")
print(full_stack)
full_stack.insert(6, "SQL")
print(full_stack)
print("\n")

