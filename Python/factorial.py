def fact(n):
	if n==1 :
		return 1
	else:
	    return n*fact(n-1)
n=input("Enter the number whose factorial you want to find\n")
try:
	n=int(n)
except:
	print("\nInvalid input. Please enter a number only!")
	exit()

if n<0:
	print("Not possible you have entered negative number")
elif n==0:
	print("0")
else:
    result=fact(n)
    print("\nFactorial value is "+str(result))
