def bubbleSort(arr):
	n = len(arr)
	for i in range(n-1):
		for j in range(0, n-i-1):
			if arr[j] > arr[j + 1] :
				arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [50, 32, 12, 12, 28, 75, 90]

bubbleSort(arr)

print ("Sorted array is:")
for i in range(len(arr)):
	print ("% d" % arr[i])
