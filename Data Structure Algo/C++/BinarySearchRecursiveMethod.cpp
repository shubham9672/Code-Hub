#include<bits/stdc++.h>
using namespace std;

int binarySearchRecursively(int arr[] , int searchElement , int low , int high){
    if(low <= high){

        int mid = (low + high)/2;

        if(arr[mid] == searchElement)
            return mid;

        if(arr[mid] < searchElement)
           return binarySearchRecursively(arr , searchElement , mid + 1 , high) ;
        
        if(arr[mid] > searchElement)
           return binarySearchRecursively(arr , searchElement , low , mid - 1) ;
        
    }

    return -1;
}

int main(){
    int size;
    cout<<"Enter total number of elements : ";
    cin>>size;

    int arr[size] , low = 0 , high = size ;

    for(int elementIndex = 0 ; elementIndex < size ; elementIndex++)
        cin>>arr[elementIndex];
    
    cout<<"Enter element to be searched: ";
    int searchElement;
    cin>>searchElement;


    if(binarySearchRecursively(arr , searchElement , low , high))
        cout<<"Element found at index "<<binarySearchRecursively(arr , searchElement , low , high);

    else 
        cout<<"Element does not exist"<<endl;

return 0;

}