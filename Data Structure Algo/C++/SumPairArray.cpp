#include <iostream>
using namespace std;

// Returns number of pairs in arr[0..n-1] with sum equal
// to 'sum'
int findPair(int arr[], int n, int sum)
{
    int count = 0; // Initialize result

    // Consider all possible pairs and check their sums
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)
            if (arr[i] + arr[j] == sum)
                count++;

    return count;
}

// Driver function to test the above function
int main()
{
    int n,sum;
    cout<<"Enter number of elements: ";
    cin>>n;
    int arr[n];
    cout<<"Enter Elemements of array:"<<endl;
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];
    }
    cout<<"Enter value of sum: ";
    cin>>sum;
    
    cout << "Count of pairs is "
         << findPair(arr, n, sum);
    return 0;
}
