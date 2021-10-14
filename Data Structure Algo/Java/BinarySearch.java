package binary_search;

public class BinarySearch {
    
    public static int binarySearch(int arr[], int lowerBound, int upperBound, int x) {
        if (upperBound >= lowerBound) {
            int mid = (lowerBound + upperBound) / 2;

            if (x == arr[mid]) {
                return mid;
                
            }else if (x < arr[mid]) {
                return binarySearch(arr, lowerBound, mid - 1, x);
                
            }else{
                return binarySearch(arr, mid + 1, upperBound, x);
            }
        }

        return -1;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 8, 9};
        
        int uppperBound = arr.length;
        int lowerBound = 0;
        
        int x = 1;
        
        int result = binarySearch(arr, lowerBound, uppperBound - 1, x);
        
        if (result == -1) {
            System.out.println("Element not found.");
        }else {
            System.out.println("Element found at index " + result);
        }
    }
    
}