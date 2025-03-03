#triangle of numbers
col=5
row=5
num=1
for i in range(row+1):
    for j in range(i):
        print(num," " , end="")
        num+=1
    print()
