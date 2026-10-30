name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Hello {name}, you will turn {age + 1} next year.")


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Quotient:", num1 / num2)


name = "naik"
marks = 85

# 1. Comma-separated print()
print("Name:", name, "Marks:", marks)

# 2. str.format()
print("Name: {}, Marks: {}".format(name, marks))

# 3. f-string
print(f"Name: {name}, Marks: {marks}")

numbers = input("Enter numbers separated by spaces: ")

numbers = numbers.split()

numbers = [int(num) for num in numbers]

total = sum(numbers)

print("Sum:", total)

#output:
Enter your name: naik3
2
289
