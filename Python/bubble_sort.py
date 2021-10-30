# example
array_example = [5, 1, 4, 2, 0, 10, 15, 66, 2, 4]

# bubble sort algo


def bubble_sort(array):
    # suppose haven't a sorted array
    ordered = False
    while not ordered:
        # here we suppose the array is sorted
        ordered = True
        # mapping all elements of array except the last one because we dont have the next element to compare with
        for i in range(0, len(array) - 1):
            # compare the element with the next element of the array
            # if the element is bigger than the next elemnt we will swap between them
            if array[i] > array[i+1]:
                # if we will turn the ordered variable to false because we need another loop to check again
                if ordered:
                    ordered = False
                # save the next element
                next_variable = array[i+1]
                # save the element in the next place
                array[i+1] = array[i]
                # save the next element in the current place
                array[i] = next_variable
    return array


sorted_array = bubble_sort(array_example)
print(sorted_array)
