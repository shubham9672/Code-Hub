num = input("Enter the number whoes factorial you want to find: ")
def fact(n):
    if n == 1 or n == 0:
       return 1
    elif n < 0:
       return ("NA")
    else:
       return n*fact(n-1)

print (fact(int(num)))
