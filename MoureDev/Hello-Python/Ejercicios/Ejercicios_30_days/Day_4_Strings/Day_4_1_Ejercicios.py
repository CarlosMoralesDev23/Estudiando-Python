import math
#Day 4: 30 Days of python programming'

# 1- Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
thirty_days_of_python = "Thirty " + "Days " + "Of " + "Python"

# 2- Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
coding_for_all = "Coding " + "For " + "All"

# 3- Declare a variable named company and assign it to an initial value "Coding For All".
company = thirty_days_of_python

# 4- Print the variable company using print().
#print(company)

# 5- Print the length of the company string using len() method and print().
#print(len(company))

# 6 - Change all the characters to uppercase letters using upper() method.
print(company.upper())

# 7 - Change all the characters to lowercase letters using lower() method.
print(company.lower())

# 8 - Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())

# 9 - Cut(slice) out the first word of Coding For All string.
print(coding_for_all[:6])

# 10 - Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(coding_for_all.find("Coding"))   #Da 0 cero, porque si esta, y esta en el index cero.  Sino daria -1. 

# 11 -Replace the word coding in the string 'Coding For All' to Python.
#coding_to_python = coding_capitalize.replace("Coding", "Python")
python_for_all = coding_for_all.replace("Coding", "Python")
#print(python_for_all)

# 12 - Change Python for Everyone to Python for All using the replace method or other methods.
everyone_for_all = python_for_all.replace("All", "Everyone")
#print(everyone_for_all)

# 13 -Split the string 'Coding For All' using space as the separator (split()) .
print("--- #13 - Split a coding_for_all ----")
print(coding_for_all)
print(coding_for_all.split())

# 14 -  split the string at the comma.
print("--- Split a companies ----")
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(", "))

# 15 - What is the character at index 0 in the string Coding For All.
sub_string = coding_for_all[:6]
print(coding_for_all.index(sub_string))

