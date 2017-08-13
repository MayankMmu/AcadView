def fact(n):
    if(n <= 1):
        return 1
    else:
        return n * fact(n-1)


n = -10
while (n<=0):
    n = int(raw_input("Enter a positive no"))

print fact(n)