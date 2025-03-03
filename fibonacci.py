def fibonacci(a):
    if a==0:
        return 0
    elif a==1:
        return 1
    else:
        return fibonacci(a-1)+fibonacci(a-2)

a=int(input("enter the number:"))

print(fibonacci(a))


