#option 1
a=[10,20]
print(f"before swap",a)

a[0],a[1]=a[1],a[0]

print(f"After swap",a)

#option 2
a = int(input("Enter first number: "))  
b = int(input("Enter second number: "))

print(f"Before swap: a = {a}, b = {b}")

a, b = b, a  # Swapping without temp variable

print(f"After swap: a = {a}, b = {b}")
