#program that works out whether if a given year is a leap year.
# it is a leap year if a particular year is evenly divisible by 4 EXCEPT every year is evenly divisible by 100 UNLESS is also evenly divisible by 400
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0 and year % 400 == 0:
        print("Leap year")
    elif year % 100 != 0:
        print("Leap year.")
    elif year % 100 == 0:
        print("Not leap year.")
    elif year % 400 == 0:
        print("Leap year.")
    else:
        print("Not leap year.")
else:
    print("Not leap year.")


