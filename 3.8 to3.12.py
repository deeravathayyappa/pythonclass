n = int(input("Enter N: "))

i = 1
while i <= n:
    print(i)
    i += 1
#output:
Enter N: 5
1
2
3
4
5


num = int(input("Enter a number: "))

temp = abs(num)
sum_digits = 0
count = 0

while temp > 0:
    digit = temp % 10
    sum_digits += digit
    count += 1
    temp //= 10

if count > 0:
    average = sum_digits / count
else:
    average = 0

print("Sum of digits =", sum_digits)
print("Average of digits =", average)

#output:
Enter a number: 3
Sum of digits = 3
Average of digits = 3.0



num = int(input("Enter an integer: "))

temp = abs(num)
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

if num < 0:
    reverse = -reverse

print("Reversed number =", reverse)

#output:
Enter an integer: 20
Reversed number = 2


num = int(input("Enter a number: "))

original = num
temp = abs(num)
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

if abs(original) == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")

#output:
Enter a number: 3
Palindrome


n = int(input("Enter the number of terms: "))

a = 0
b = 1
i = 1

while i <= n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    i += 1

#output:
Enter the number of terms: 3
0 1 1 

