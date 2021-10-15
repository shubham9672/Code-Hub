n = int(input())
cnt = 0
while n:
    n = n & (n - 1)
    cnt += 1
print(cnt)
