
class PancakeSort
{
    static void flip(final int[] arr, int i) {
        for (int start = 0; start < i; ++start, --i) {
            final int temp = arr[start];
            arr[start] = arr[i];
            arr[i] = temp;
        }
    }
    
    static int findMax(final int[] arr, final int n) {
        int mi = 0;
        for (int i = 0; i < n; ++i) {
            if (arr[i] > arr[mi]) {
                mi = i;
            }
        }
        return mi;
    }
    
    static int pancakeSort(final int[] arr, final int n) {
        for (int curr_size = n; curr_size > 1; --curr_size) {
            final int mi = findMax(arr, curr_size);
            if (mi != curr_size - 1) {
                flip(arr, mi);
                flip(arr, curr_size - 1);
            }
        }
        return 0;
    }
    
    static void printArray(final int[] arr, final int arr_size) {
        for (int i = 0; i < arr_size; ++i) {
            System.out.print(String.valueOf(arr[i]) + " ");
        }
        System.out.println("");
    }
    
    public static void main(final String[] args) {
        final int[] arr = { 23, 10, 20, 11, 12, 6, 7 };
        final int n = arr.length;
        pancakeSort(arr, n);
        System.out.println("Sorted Array: ");
        printArray(arr, n);
    }
}
