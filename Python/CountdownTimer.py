import time
n=int(input("Enter seconds: "))
print("Countdown begins...\n0...")
for i in range(n):
    time.sleep(1)
    print(i+1,"...")
print("Time's up Man")
