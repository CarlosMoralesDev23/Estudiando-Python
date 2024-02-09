import math
#Day 4: 30 Days of python programming'
thirty_days_of_python = "Thirty " + "Days " + "Of " + "Python"
coding_for_all = "Coding For All"
company = coding_for_all
python_for_all = coding_for_all.replace("Coding", "Python")

everyone_for_all = python_for_all.replace("All", "Everyone")

# 21 - Use index to determine the position of the first occurrence of C in Coding For All.
print("---- first occurrence C ----")
print(coding_for_all)
print(coding_for_all.find("C"))
print("\n")


# 22 - Use index to determine the position of the first occurrence of F in Coding For All.
print("---- first occurrence F ----")
print(coding_for_all)
print(coding_for_all.find("F"))
print("\n")

# 23 - Use rfind to determine the position of the last occurrence of l in Coding For All People.
print("---- Last occurrence l ----") 
coding_for_all_people = "Coding For All People"
print(coding_for_all_people)
print(coding_for_all_people.rfind("l"))
print("\n")

# 24 - Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print("---- First Concurrence word because ----") 
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.find("because"))
print("\n")

# 25 - Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print("---- Slice de las 3 because ----") 
comienza_because = sentence.find("because")
fin_because = sentence.rfind("because") + len("because")
print(sentence[comienza_because:fin_because])
print("\n")


# 26 - Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print("---- index of first because ----") 
comienza_because = sentence.find("because")
print(comienza_because)
print("\n")

# 27 - Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
#Does ''Coding For All' start with a substring Coding?
print("---- start with a substring Coding? ----") 
start_with_coding = coding_for_all.startswith("Coding")
print(start_with_coding)
print("\n")
#Does 'Coding For All' end with a substring coding?
print("---- End with a substring Coding? ----")
ends_with_coding = coding_for_all.endswith("Coding")
print(ends_with_coding)
print("\n")





#'   Coding For All      '  , remove the left and right trailing spaces in the given string.
#Which one of the following variables return True when we use the method isidentifier():
    #30DaysOfPython
    #thirty_days_of_python