def inserionSort(array):
    for i in range(1, len(array)):
        j = i
        while array[j-1] > array[j] and j > 0:
            array[j-1], array[j] = array[j], array[j-1]
            j-=1

#array which needs to be sorted using insetion sort
array = [45,78,65,12,56,75,95]
print(array)
inserionSort(array)
print(array)
