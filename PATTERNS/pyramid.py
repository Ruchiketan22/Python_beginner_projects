#pyramid
col=5
row=5
for r in range(1,row):
    for c in range(row-r):
        print(" ",end="")
    for c in range(2*r-1):
        print("*",end="")
    print()
