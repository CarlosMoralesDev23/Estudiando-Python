print(' ---- Dictionaries ----')
print('\n')

####################################################################################
print(' ---- Create an empty dictionary called dog ----')
dog = {}
print(type(dog))
print(dog)
print('\n')


####################################################################################
print(' ---- Add name, color, breed, legs, age to the dog dictionary ----')
dog["name"] = "Danco"
dog["color"] = "Marron"
dog["breed"] = "Pastor Aleman"
dog["legs"] = 4
dog["age"] = 8
print(dog)
print('\n')

####################################################################################
print(' ---- Create student dictionary add first_name, last_name, gender, age, marital status, skills, country, city and address ----')
student = {}
student["first_name"] = "Carlos"
student["Last_name"] = "Morales"
student["gender"] = "Masculino"
student["age"] = 33
student["married"] = True
student["skills"] = ["Javascrip", "Python", "HTML", "CSS"]
student["country"] = "Argentina"
student["city"] = "Buenos Aires"
student["address"] = "Balvanera"
print(student)
print('\n')


####################################################################################
print(' ---- Get the length of the student dictionary ----')
print(f"El largo del dict Student es de {len(student)} elementos")
print('\n')


####################################################################################
print(' ---- Get the value of skills and check the data type, it should be a list ----')
print(type(student["skills"]))
print('\n')


####################################################################################
print(' ---- Modify the skills values by adding one or two skills ----')
student["first_name"] = "Alberto"
student["skills"].append("React")
student["skills"].append("Node")
print(student)
print('\n')


####################################################################################
print(' ---- Get the dictionary keys as a list ----')
key_list = list(student.keys())
print(key_list)
print('\n')


####################################################################################
print(' ---- Get the dictionary values as a list ----')
values_list = list(student.values())
print(values_list)
print('\n')


####################################################################################
print(' ---- Change the dictionary to a list of tuples using items() method ----')

student_tuple = tuple(student.items())
print(student_tuple)
print('\n')



####################################################################################
print(' ---- Delete one of the items in the dictionary ----')
print(student)
del student["skills"]
print(student)
print('\n')


####################################################################################
print(' ---- Delete one of the dictionaries ----')
del student
print(student)
print('\n')


'''


'''