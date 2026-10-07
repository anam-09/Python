year = int(input("ENter a year to check if it is leap year or not"))

if year % 400 == 0:
    print("Its a leap year")
elif year % 4 == 0 and year % 100 != 0:
    print("Its a leap year")
else:
    print("its not a leap year")