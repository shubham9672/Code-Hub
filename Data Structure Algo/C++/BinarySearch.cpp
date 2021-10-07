// Author : Sashank Agarwal
// Github Profile : https://github.com/sasagarw

/* C++ implementation of Binary Search using Recursive method.
   The idea here is to find if the element to be searched lies to the left
   or right of mid element and reduce our searching array.
   Assumption: Array elements are in sorted order. */

#include <bits/stdc++.h>
using namespace std; 

// define array globally
const int N = 10; // size of array

int array[N];

// elememt to be searched in array
int k;

// checkIfLess checks if the element to be searched is less/greater than mid element
// returns 1 if less, otherwise 0.
bool checkIfLess(int mid)
{
	// element at mid position in array
	int ele = array[mid];

    // if k is less than element at mid position 
    // then we need to bring our higher index to mid 
    // otherwise move our lower index to mid 
    // and then continue further
    int isLess = (k <= ele) ? 1 : 0;

    return isLess
}

// binarySearch is the actual recursive implementation of the Binary Search Algorithm.
void binarySearch(int low,int high)
{
	while(low < high)
	{
		int mid = (low + high) / 2;

		if(checkIfLess(mid))
			high = mid;
		else
			low = mid + 1;
	}

	// if array[low] is k then we have found it in our array
	if(array[low] == k)
		cout << "Element found at index " << low; // 0 based indexing
	else
		cout << "Element doesn't exist in array"; // element was not found in our array
}

int main()
{
    cout << "Enter the array elements: " << endl;
    for(int i=0; i<N; i++)
    {
        cin >> array[i];
    }

    cout << "Enter the element to be searched: ";
    cin >> k;

    // k is possible to lie only between 0 and length of array
    // i.e., 0 <= k < N
    binarySearch(0, N);

	return 0;
}
