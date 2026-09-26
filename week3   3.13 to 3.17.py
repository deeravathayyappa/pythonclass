num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

#output:
Enter a number: 9
9 x 1 = 9
9 x 2 = 18
9 x 3 = 27
9 x 4 = 36
9 x 5 = 45
9 x 6 = 54
9 x 7 = 63
9 x 8 = 72
9 x 9 = 81
9 x 10 = 90



num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print("Factorial of", num, "=", factorial)


#output:
Enter a number: 3
Factorial of 3 = 6


text = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
spaces = 0

for ch in text:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)

#output:Enter a string: naik
Vowels: 2
Consonants: 2
Digits: 0
Spaces: 0

num = int(input("Enter a number: "))

if num < 2:
    print("Not a prime number")
else:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")

#output:Enter a number: 20
Not a prime number


start = int(input("Enter the starting limit: "))
end = int(input("Enter the ending limit: "))

print("Prime numbers between", start, "and", end, ":")

for num in range(start, end + 1):
    if num < 2:
        continue

    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")

#output:
Enter the starting limit: 2
Enter the ending limit: 10
Prime numbers between 2 and 10 :
2 3 5 7 

