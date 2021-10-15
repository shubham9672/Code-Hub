n = input("Enter value of n : ")

b = input("Enter value of b : ")

r1 = int(n)
r2 = int(b)

t1 = 0
t2 = 1

while r2 > 0:
    q = r1 // r2
    r = r1 - (q * r2)
    r1 = r2
    r2 = r

    t = t1 - (q * t2)
    t1 = t2
    t2 = t

print(r1)
print(r2)
print(t1)
print(t2)

print("The required value is t1 = ", t1)

print("To calculate the actual multiplicative inverse do : {0} mod {1}".format(t1, n))
