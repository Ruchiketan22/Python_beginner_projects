#hollow square
col=5
row=5
for r in range(row):
    for c in range(col):
        if r==0 or r==row - 1 or c==0 or c==col-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
