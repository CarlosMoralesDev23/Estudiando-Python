print(' ---- #4 Temperature in °C can be converted to °F  ----')
def c_to_f(centigrados):
    F = (centigrados * 9/5) + 32
    return print(f"Los grados Farenheit son {F}")
c_to_f(1)
print('\n')


print(' ---- #5 check-season ----')

def check_season(month):
    season = ""
    if month == "September" or month == "October" or month == "November":
        season ="The season is Autum"
    elif month == "December" or month == "January" or month == "February":
        season = "The season is Winter"
    elif month == "March" or month == "April" or month == "May":
        season = "The season is Spring"
    elif month == "June" or month == "July" or month == "August":
        season = "The season is Summer"
    return print(f"{season}")
check_season("August")
print('\n')




print(' ---- #6 calculate_slope ----')

def calculate_slope(x1, x2, y1, y2):
    m = (y2 - y1) / (x2 - x1)

    return print(f"El valor de la pendiente es {m}")

y2= int(input("Ingresa y2: "))
y1= int(input("Ingresa y1: "))
x2= int(input("Ingresa x2: "))
x1= int(input("Ingresa x1: "))
calculate_slope(x1, x2, y1, y2)
print('\n')
