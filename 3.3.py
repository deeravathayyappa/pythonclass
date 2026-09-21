a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Not a valid triangle")
elif a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Equilateral Triangle")
    elif a == b or b == c or a == c:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Not a valid triangle")



'''output: Enter first side: 3
Enter second side: 2
Enter third side: 4
Scalene Triangle

Enter first side: 2
Enter second side: 3
Enter third side: 8
Not a valid triangle'''
