ch = input("Enter a character: ")

if ch.isalpha():
    if ch.lower() in "aeiou":
        print("Vowel")
    else:
        print("Consonant")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Symbol")

'''output:Enter a character: v
Consonant
Enter a character: a
Vowel'''



year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))
day = int(input("Enter day: "))

leap_year = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

days_in_month = [
    31, 29 if leap_year else 28, 31, 30, 31, 30,
    31, 31, 30, 31, 30, 31
]

if month < 1 or month > 12:
    print("Invalid date: month must be between 1 and 12.")
elif day < 1 or day > days_in_month[month - 1]:
    print("Invalid date.")
else:
    print("Valid date.")

'''output:Enter year: 2026
Enter month (1-12): 11
Enter day: 20
Valid date.'''
