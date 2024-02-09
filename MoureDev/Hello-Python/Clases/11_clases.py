print(' ---- Empty Class ----')

class MyEmptyPerson:  # class Name does with camelcase
    pass #pass does a by pass to permit a error

print(MyEmptyPerson)
print(MyEmptyPerson())

print('\n')






print(' ---- class ----')

class Person:
    def __init__(self, name, surname, alias = "camodev") -> None:
        self.__name = name # Private property
        self.surname = surname
        self.hobby = "Ver anime" # This property was created into de Person
        self.full_name = f"{name} {surname} ({alias})"
        self.alias = alias

    def walk(self): # is necessary to specificity self 
        print(f"{self.full_name} is walking")
    
    def get_name(self):  # Private Property
        return self.__name

myPerson = Person( "Carlos", "Morales")
print(myPerson) # that form only to accede where is.
myPerson.get_name()
print(f"{myPerson.get_name()}  {myPerson.surname}")
print(myPerson.hobby)
print(myPerson.full_name)
myPerson.walk()
print(myPerson.alias)


print(' ---- Titulo to Modify ----')
my_other_person = Person("Carlitos", "Morales", "CarlitosDev")
print(my_other_person.full_name)
my_other_person.walk()
print(my_other_person.alias)
print('\n')

my_other_person.full_name = "Jose Edgardo"
print(my_other_person.full_name)



print('\n')