print(' ---- Ejercicios Condicionales ----')
print('\n')

########################################################
print(' ---- Here we have a person dictionary. Feel free to modify it! ----')

person = {
'first_name': 'Asabeneh',
'last_name': 'Yetayeh',
'age': 250,
'country': 'Finland',
'is_marred': True,
'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
'address': {
    'street': 'Space street',
    'zipcode': '02210'
    }
}

# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if "skills" in person:
    print(f"The middle skill in the skills list is: { person['skills'][(len(person['skills'])//2)] }")


# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if "skills" in person:
    if "Python" in person['skills']:
        print("Dentro de las Skills si esta Python")
    else:
        print("Python no esta dentro de las Skills")



if set(["JavaScript", "React"]).issubset(person['skills']):
    print('He is a front end developer')
elif set(["Node", "Python", "MongoDB"]).issubset(person['skills']):
    print('He is a backend developer')
elif set(["React", "Node", "MongoDB"]).issubset(person['skills']):
    print('He is a fullstack developer')
else: 
    print('unknown title')


'''



 * If the person is married and if he lives in Finland, print the information in the following format:
'''
person = {
'first_name': 'Asabeneh',
'last_name': 'Yetayeh',
'age': 250,
'country': 'Finland',
'is_marred': True,
'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
'address': {
    'street': 'Space street',
    'zipcode': '02210'
    }
}

if (person['is_marred']) and person['country'] == "Finland":
    print( f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married."   )




print('\n')