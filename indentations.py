#1.Incosistent indentation error

age = int(input("Enter your age: "))

"""if age >= 18:
    print("You are eligible to vote.")
   else:
    print("You are not eligible to vote.")"""

#unindent doent match the outer indentation level

#fixed version is
    
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
    

#2.nested structure
#even or odd program

for i in range(10):
    if i%2==0:
        print(f"{i}is Even")
    else:
        print(f"{i}is odd")


#3.correct python indentation
        
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


#4.challenge


for i in range(1, 6):
    if i > 0:
        for j in range(1, i + 1):
            print("*",end="")
        print()
