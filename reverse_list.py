#option 1
l1=input("enter the list with ").split(",")
l1=(list(map(int,l1)))
print(l1[::-1])


# Option 2 
size = int(input("Define the size of your list: "))
l2 = []

for i in range(size):
    element = int(input(f"Enter element {i+1}: "))  # Convert to int
    l2.append(element)

print("Reversed list:", l2[::-1])  # Fixing print message


#we can also use reverse() instead of append() to reverse the sequence