class SelectionSort
{
    void sort(int arr[])
    {
        int size = arr.length;
        for (int i = 0; i < size-1; i++)
        {
            int min_idx = i;
            for (int j = i+1; j < size; j++)
                if (arr[j] < arr[min_idx])
                    min_idx = j;
            int temp = arr[min_idx];
            arr[min_idx] = arr[i];
            arr[i] = temp;
        }
    }
    void printArray(int arr[])
    {
        int size = arr.length;
        for (int i=0; i<size; ++i)
            System.out.print(arr[i]+" ");
        System.out.println();
    }
 
    // Driver code to test above
    public static void main(String args[])
    {
        SelectionSort Selection = new SelectionSort();
        int arr[] = {64,25,12,22,11};
        Selection.sort(arr);
        System.out.println("Sorted array using Selection Sort");
        Selection.printArray(arr);
    }
}