# Input section
n = int(input("Enter the number of items: "))
W = int(input("Enter the weight capcity: "))
item = [i+1 for i in range(n)]
weight = [0]
value = [0]
for i in range(n):
    weight.append(int(input("Enter the weight of {0} item: ".format(i+1))))
    value.append(int(input("Enter the value of {0} item: ".format(i+1))))

# Knapsack max value implementation
M = [[0 for i in range(W+1)] for _ in range(n+1)]
for i in range(1,n+1):
    for w in range(1,W+1):
        if weight[i] > w:
            M[i][w] = M[i-1][w]
        else:
            M[i][w] = max(M[i-1][w], value[i] + M[i-1][w-weight[i]])
print("Max value: ", M[n][W])

# Find the items included in knapsack
i = n
k = W
knapsackItems = []
while i>0 and k>0:
    if M[i][k] != M[i-1][k]:
        knapsackItems.append(i)
        k = k - weight[i]
        i = i - 1
    else:
        i = i - 1
print("Items in knapsack are: " ,knapsackItems)
