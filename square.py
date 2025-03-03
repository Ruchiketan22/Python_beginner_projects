def Pattern_Print(M, P):
    for i in range(1, M+1):
        for j in range(1, P+1):
            if i == 1 or i == M or j == 1 or j == P:
                print("*", end="")
            else:
                print(" ", end="")    
        print()

Rows = int(input("Enter Numbers Of Rows => "))
Columns = int(input("Enter Numbers Of Columns => "))

Pattern_Print(Rows, Columns)
