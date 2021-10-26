#include <iostream>
using namespace std;

// This is the swap Function for swapping the numbers

void swap(int a[],int i,int j){  
    int temp=a[i];
    a[i]=a[j];
    a[j]=temp;
}

void DNF_Sort(int a[],int n)
{ int low=0,mid=0,high=n-1;  // low and mid start from starting and high from end of array
while(mid<=high)
    { if(a[mid]==0)  // if element at mid is 0 then we swap low and mid and increase low and mid to make array sorted 
        { swap(a,low,mid);
            low++; mid++;
        }
        else if(a[mid]==1){ // if element at mid equal to 1 we simply increase mid
            mid++;
        }
        else
        { swap(a,mid,high); // if element is at mid equal to 2 we have to swap mid and high and decrease high 
        high--;}
    }
}

int main() {
	int a[]={1,0,2,1,0,1,2,1,2};
	DNF_Sort(a,9);
for(int i=0;i<9;i++)
cout<<a[i]<<" ";
	
	return 0;
}
