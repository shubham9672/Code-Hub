# Selection sort in python in easy way
def bubblesort(arr):
    n = len(arr)
    for i in range(n - 1, -1, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)


bubblesort([45, 1, 878, 23, 0, 15, 8])
