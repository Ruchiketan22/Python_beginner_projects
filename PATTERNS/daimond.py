#daimond
col=5
row=5
for r in range(row):
    for c in range(row-r):
        print(" ",end="")
    for c in range(r*2-1):
        print("*",end="")
    print()
for r in range(1,row):
    for c in range(r):
        print(" ",end="")
    for c in range(1,col*2-2):
        print("*",end="")
    print()
    col=col-1
