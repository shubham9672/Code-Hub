x = int(input("Enter a number:"))


def Fibonacci(x):
    if x < 0:
        print("Incorrect input")

    elif x == 0:
        return 0

    elif x == 1:
        return 1
    else:
        return Fibonacci(x - 1) + Fibonacci(x - 2)


print(str(x) + "th Fibonacci number is:" + str(Fibonacci(x)))
