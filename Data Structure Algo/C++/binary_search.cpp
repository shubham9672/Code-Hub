#include<iostream>
 
using namespace std;


int binarySearch(int a[],int n,int x){
    int start=0;
    int end=n-1;
    int mid;
    while(start<=end){
        mid=(start+end)/2;
        if (a[mid]==x)
            return mid;
        else if(x<a[mid])
            end=mid-1;
        else
            start=mid+1;
        
    }
    return -1;
}

void input(int a[],int n){
    for(int i=0;i<n;++i)
        cin>>a[i];
}

int main(){
    int a[100];
    int n,x;
    cin>>n;
    input(a,n);
    cin>>x;
    cout<<binarySearch(a,n,x);
    return 0;
}


