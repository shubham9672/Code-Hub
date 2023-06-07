#include <bits/stdc++.h>
using namespace std; 
  
void swap(int* a, int* b) 
{ 
    int t = *a; 
    *a = *b; 
    *b = t; 
} 
  
int partition(vector<int> arr, int low, int high) 
{ 
    int pivot = arr[high]; 
    int i = (low - 1); // Index of smaller element and indicates the right position of pivot found so far
  
    for (int j = low; j <= high - 1; j++) 
    { 
        if (arr[j] < pivot) 
        { 
            i++; // increment index of smaller element 
            swap(&arr[i], &arr[j]); 
        } 
    } 
    swap(&arr[i + 1], &arr[high]); 
    return (i + 1); 
} 

void quickSort(vector<int> arr, int low, int high) 
{ 
    if (low < high) 
    { 
        int pi = partition(arr, low, high); 
        quickSort(arr, low, pi - 1); 
        quickSort(arr, pi + 1, high); 
    } 
} 
  
// Driver Code
int main() 
{ 
    vector<int> arr;
    int a,n;
    cin>>n;
    for (int i = 0; i < n; i++) {
        cin>>a;
        arr.push_back(a);
    } 
    quickSort(arr, 0, n - 1); 
    cout << "Sorted array: \n"; 
    for (int i = 0; i < n; i++) 
        cout << arr[i] << " "; 
    cout << endl;  
    return 0; 
} 