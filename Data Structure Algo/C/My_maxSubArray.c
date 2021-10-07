#include<stdio.h>
int Maximum(int a,int b,int c)
{
    if(a >= b && a>=c )
        return a;
    else if( b>=a && b>=c)
        return b;
    else
        return c;
}

int crossSum(int a[],int l,int mid,int r)
{
    int i,left,right,t1,t2,t3,t4;

    if( l == mid)
        return (a[l]+a[r]);
    t2 = t1 = a[mid];
    for(i = mid-1 ; i >=l;i--)
    {
        t1 = t1 + a[i];
        if(t1 > t2)
            t2 = t1;
    }
   t4 = t3 = a[mid+1];
    for(i=mid+2;i<=r;i++)
    {
        t3 =t3 + a[i];
        if(t3 > t4 )
            t4 =t3;
    }
    return (t2 + t4);
}
int maxSumArray(int a[],int l,int r)
{
    if(l == r)
        return a[l];
    int mid = (l + r)/2;
    int left,right,cross,max;
    left = maxSumArray(a,l,mid);
    right = maxSumArray(a,mid+1,r);
    cross = crossSum(a,l,mid,r);
    max = Maximum(left,right,cross);
    return max;
}
int main()
{
int a[] = {2,-3,4,-5,-7};
int size = sizeof(a)/sizeof(a[0]);
int n,maxSum;
maxSum = maxSumArray(a,0,size-1);
printf("Maximum subarray sum : %d ",maxSum);
return 0;
}

