#include<iostream>
 
using namespace std;


int linearSearch(int a[],int n,int x){
    for(int i=0;i<n;++i){
        if(a[i]==x)
            return i;
    }
    return -1;
}

void input(int a[],int n){
    for(int i=0;i<n;++i)
        cin>>a[i];
}
void output(int a[],int n){
    for(int i=0;i<n;++i)
        cout<<a[i]<<" ";
}

int main(){
    int a[100];
    int n,x;
    cin>>n;
    input(a,n);
    cin>>x;
    cout<<linearSearch(a,n,x);
    return 0;
}