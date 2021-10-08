// Count of subsets with the given sum
// Input : 
// 6
// 2 3 5 6 8 10
// 10
// Output :
// 3

#include<iostream>
using namespace std;
int subset_sum(int arr[],int sum,int n)
{
    int t[n+1][sum+1];
    for(int i=0;i<n+1;i++)
    {
        for(int j=0;j<sum+1;j++)
        {
            if(i==0)
            t[i][j]=0;
            if(j==0)
            t[i][j]=1;
        }
    }
     for(int i=1;i<n+1;i++)
    {
        for(int j=1;j<sum+1;j++)
        {
            if(arr[i-1]<=j)
            t[i][j]=t[i-1][j-arr[i-1]]+t[i-1][j];
            else
            t[i][j]=t[i-1][j];
        }
    }
    return t[n][sum];
}
int main()
{
    // Input the array
    int n; cin >> n;
    int arr[n];
    for(int i=0; i<n; i++)  cin>> arr[i];
    // Input the sum
    int sum; cin >> sum;
    cout<<subset_sum(arr,sum,n);
}
    
    
