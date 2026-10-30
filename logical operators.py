percentage = float(input("Enter percentage: "))
attendance = float(input("Enter attendance %: "))
eligible = percentage > 75 and attendance > 90
print("Eligible for scholarship:", eligible)


#output:
Enter percentage: 100
Enter attendance %: 80
Eligible for scholarship: False
