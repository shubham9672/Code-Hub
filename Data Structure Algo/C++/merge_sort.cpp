#include<iostream>
 
using namespace std;

void input(int a[],int n){
    for(int i=0;i<n;++i)
        cin>>a[i];
}

void output(int a[],int n){
    for(int i=0;i<n;++i)
        cout<<a[i]<<" ";
    cout<<endl;
}


void merge(int a[],int si,int ei){
    int mid=(si+ei)/2;
    int i=0;
    int j=mid+1;
    int b[ei+1];
    int k=0;

    for(;i<=mid && j<=ei;){
        if(a[i]<a[j]){
            b[k]=a[i];
            k++;
            i++;
        }else{
            b[k]=a[j];
            j++;
            k++;
        }
    }
    if(i<=mid){
        for(;i<=mid;++i,++k)
            b[k]=a[i];
    }else if(j<=ei){
        for(;j<=ei;++j,++k)
            b[k]=a[j];
    }
    
    for(k=0;k<=ei;++k)
    a[k]=b[k];
    
}


void mergeSort(int a[],int si,int ei){
    if(si>=ei)
        return;
    int mid=(si+ei)/2;
    mergeSort(a,si,mid);
    mergeSort(a,mid+1,ei);
    merge(a,si,ei);
}



int main(){
    int a[100];
    int n;
    cin>>n;
    input(a,n);
    mergeSort(a,0,n-1);
    output(a,n);  
    return 0;
}