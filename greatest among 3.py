num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 == num2 == num3:
    print("All three numbers are equal.")
elif num1 == num2:
    print("The numbers", num1, "and", num2, "are equal.")
elif num1 == num3:
    print("The numbers", num1, "and", num3, "are equal.")
elif num2 == num3:
    print("The numbers", num2, "and", num3, "are equal.")
elif num1 > num2 and num1 > num3:
    print("The greatest number is:", num1)
elif num2 > num1 and num2 > num3:
    print("The greatest number is:", num2)
else:
    print("The greatest number is:", num3)