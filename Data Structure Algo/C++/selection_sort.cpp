#include<iostream>
using namespace std;

//array traversal code

void traversal(int size,int *a){
    for(int j=0;j<size;j++){
        cout<<a[j]<<" ";
    }
    cout<<endl;
}

//function for sorting 
void selectionsort(int n,int *a){
    int min,temp;
    for(int i=0;i<n;i++){
        min=i;
        for(int j=i+1;j<n;j++){
            if(a[j]<a[min]){
                min=j;
            }
        }
        temp=a[i];
        a[i]=a[min];
        a[min]=temp;
    }
}

int main(){
    int n;
    cout<<"Enter the number of elements of array:"<<endl;
    cin>>n;
    int arr[n];
    cout<<"Enter the elements of array:"<<endl;
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    cout<<"Before sorting:"<<endl;
    traversal(n,arr);
    selectionsort(n,arr);
    cout<<"After sorting:"<<endl;
    traversal(n,arr);
    return 0;
}