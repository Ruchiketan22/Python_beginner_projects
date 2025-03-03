var1=input("enter the word:")

var2=var1[::-1]

if var1==var2:
    print(f"{var1} is a palindrome")
else:
    print(f"{var1} is not an palindrome")