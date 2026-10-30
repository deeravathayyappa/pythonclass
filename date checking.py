year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

if month < 1 or month > 12:
    print("Invalid date")

else:
    if month == 2:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            days = 29
        else:
            days = 28

    elif month == 4 or month == 6 or month == 9 or month == 11:
        days = 30

    else:
        days = 31

    if day >= 1 and day <= days:
        print("Valid date")
    else:
        print("Invalid date")


#output:
Enter year: 2026
Enter month: 11
Enter day: 20
Valid date

