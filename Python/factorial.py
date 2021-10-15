def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


n = int(input("Enter the number whoes factorial you want to find\n"))
if n < 0:
    print("Not possible you have entered negative number")
elif n == 0:
    print("0")
else:
    result = fact(n)
    print(result)
