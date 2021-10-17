def printPattern(n):
    k = 0
    for i in range(1,n+1):
        for j in range(i,n):
            print(' ', end='')
        while (k != (2 * i - 1)):
            if (k == 0 or k == 2 * i - 2):
                print('*', end='')
            else:
                print(' ', end ='')
            k = k + 1
        k = 0
        print ("")
    for i in range(0, 2 * n -1):
        print ('*', end = '')


n = int(input())
printPattern(n)


