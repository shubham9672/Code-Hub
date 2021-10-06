# insertion sort algorithm
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


arr = [423, 111, 133, 45, 26]
insertion_sort(arr)
print("The sorted array is:")
for i in range(len(arr)):
    print("{}".format(arr[i]), end=" ")
