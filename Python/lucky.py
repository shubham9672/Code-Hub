#Python program to check lucky number

def lucky(n):

    if lucky.counter > n:
        return 1
    if n % lucky.counter == 0:
        return 0

    next_position = n - (n/lucky.counter)
    lucky.counter = lucky.counter + 1

    return lucky(next_position)

#driver
lucky.counter = 2
x = 5
if lucky(x):
    print(x, "is lucky")
else:
    print(x,"no lucky")
