#Control Statements

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print(num1, "is rester than" , num2)
elif num2 > num1:
    print(num2, "is greater than", num1)
else:
    print("Both numberd sre equal")