//Program to implement quick sort

#include<iostream>
using namespace std;

void quick(int arr[], int low, int high);
int partition(int arr[], int low, int high);
void swap(int &x, int &y);

int main()
{
    int n;
    cout<<"Enter the number of elements in the array:\n";
    cin>>n;
    int array[n];
    cout<<"Enter the elements of the array:\n";
    for(int i=0;i<n;i++)
    {
        cin>>array[i];
    }
    quick(array, 0, n-1);
    cout<<"The sorted array is:\n";
    for(int i=0;i<n;i++)
    {
        cout<<array[i]<<" ";
    }
    return 0;
}

void quick(int arr[], int low, int high)
{
    if(low < high)
    {
        int pivot = partition(arr, low, high);
        quick(arr, low, pivot-1);
        quick(arr, pivot+1, high);
    }
}

int partition(int arr[], int low, int high)
{
    int i = low, j = high + 1, pivot = arr[low];
    while(i<=j)
    {
        do
        {
            i++;
        } while (pivot >= arr[i]);
        do
        {
            j--;
        } while (pivot < arr[j]);
        if(i<j)
        {
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[low], arr[j]);
    return j;
}

void swap(int &x, int &y)
{
    int temp = x;
    x = y;
    y = temp;
}