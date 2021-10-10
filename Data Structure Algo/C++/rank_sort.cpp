//Program to implement Rank Sort

#include<iostream>
using namespace std;

void rank_sort(int arr[], int size);

int main()
{
    int n;
    cout<<"Enter the number of elements of the array:\n";
    cin>>n;
    int array[n];
    cout<<"Enter the elements of the array:\n";
    for(int i=0;i<n;i++)
    {
        cin>>array[i];
    }
    cout<<"The sorted array is:\n";
    rank_sort(array, n);
    return 0;
}

void rank_sort(int arr[], int size)
{
    int rank[size] = {0}, sorted[size] = {0};
    for(int i=1;i<size;i++)
    {
        for(int j=0;j<i;j++)
        {
            if(arr[j] <= arr[i])
                rank[i]++;
            else
                rank[j]++;
        }
    }
    for(int i=0;i<size;i++)
    {
        sorted[rank[i]] = arr[i];
    }
    for(int i=0;i<size;i++)
    {
        cout<<sorted[i]<<" ";
    }
}