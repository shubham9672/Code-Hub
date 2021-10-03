# Creating a bubble sort function
def bubble_sort(local):
    # Outer loop for traverse the entire list
    for i in range(0, len(local) - 1):
        for j in range(len(local) - 1):
            if (local[j] > local[j + 1]):
                temp = local[j]
                local[j] = local[j + 1]
                local[j + 1] = temp
    return local


array = [5, 3, 8, 6, 7, 2]
print("The unsorted list is: ", array)
# Calling the bubble sort function
print("The sorted list is: ", bubble_sort(array))

#Output
#The unsorted list is:  [5, 3, 8, 6, 7, 2]
#The sorted list is:  [2, 3, 5, 6, 7, 8]

