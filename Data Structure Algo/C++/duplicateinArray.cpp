#include <iostream>
#include <math.h>
using namespace std;

void Duplicate(int arr[], int size)
{
    int i;
    cout << "The Duplicate elements are:" << endl;
    for (i = 0; i < size; i++)
    {
        if (arr[abs(arr[i])] >= 0)
            arr[abs(arr[i])] = -arr[abs(arr[i])];
        else
            cout << abs(arr[i]) << " ";
    }
}

// Driver Code
int main()
{
    int n;
    cout << "Enter number of elements in array: ";
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    Duplicate(arr, n);
    return 0;
}
