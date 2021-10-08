#include <bits/stdc++.h>
using namespace std; 

void s(int* a, int* b)  { 
    int t = *a; 
    *a = *b; 
    *b = t; 
} 
  
int partition (int arr[], int low, int high) { 
    int pivot = arr[high];
    int i = (low - 1); 
  
    for (int j = low; j <= high - 1; j++) {  
        if (arr[j] < pivot)  { 
            i++; 
            s(&arr[i], &arr[j]); 
        } 
    } 
    s(&arr[i + 1], &arr[high]); 
    return (i + 1); 
} 

void qSort(int arr[], int low, int high) { 
    if (low < high) { 
        int pi = partition(arr, low, high); 
        qSort(arr, low, pi - 1); 
        qSort(arr, pi + 1, high); 
    } 
} 
  
void print(int arr[], int size) { 
    int i; 
    for (i = 0; i < size; i++) {
        cout << arr[i] << " "; 
    }
    cout << endl; 
} 
  
int main() 
{ 
    int arr[] = {10, 20, 30, 1, 2, 3}; 
    int n = sizeof(arr) / sizeof(arr[0]); 
    qSort(arr, 0, n - 1); 
    cout << "Sorted array: \n"; 
    print(arr, n); 
    return 0; 
} 