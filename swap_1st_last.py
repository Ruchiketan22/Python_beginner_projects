l1=input("enter the list and seperate it with comma").split(",")
n=l1.__len__()-1
l1[0],l1[n]=l1[n],l1[0]
print(l1)

