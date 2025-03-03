#pyramid of numbers
col=5
row=5
for i in range(row):
    for j in range(row-i):
        print(" ",end="")
    for j in range(1,i+1):
        print(j,end="")
    for j in range(i-1,0,-1):
        print(j,end="")
    print()
