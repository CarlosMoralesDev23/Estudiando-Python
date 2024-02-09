print("---- Exercises: Level 2 ----")
print("\n")

print ("---- The following is a list of 10 students ages ----")
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(ages)
print("\n")


# 1 - Sort the list and find the min and max age
print(' ---- Sort the list and find the min and max age ----')
ages.sort()
print(ages)
print(ages[-1])
print('\n')

# 2 - Add the min age and the max age again to the list
print(' ---- Add the min age and the max age again to the list ----')
min_age = ages[0]
max_age = ages[-1]
ages.append(min_age)
ages.append(max_age)
ages.sort()
print(ages)
print('\n')

# 3 - Find the median age (one middle item or two middle items divided by two)
print(' ---- Find the median age (one middle item or two middle items divided by two) ----')
ages_sin_repetir = list(set(ages))
print(ages_sin_repetir)
median_age = ages_sin_repetir[(len(ages_sin_repetir))//2]
print(median_age)
print('\n')


# 4 - Find the average age (sum of all items divided by their number )
print(' ----  Find the average age (sum of all items divided by their number ) ----')
sum_ages = sum(ages)
promedio_ages = sum_ages / (len(ages))
print(promedio_ages)
print('\n')


# 5 - Find the range of the ages (max minus min)
print(' ---- Titulo to Modify ----')
print('\n')
print(f"El rango de las edades va desde {min_age} hasta {max_age}")



# 6 - Compare the value of (min - average) and (max - average), use abs() method
print(' ---- Compare the value of (min - average) and (max - average), use abs() method ----')
min_minus_avg = min_age - promedio_ages
max_minus_avg = max_age - promedio_ages
print( abs(min_minus_avg) )
print( abs(max_minus_avg))
print('\n')
