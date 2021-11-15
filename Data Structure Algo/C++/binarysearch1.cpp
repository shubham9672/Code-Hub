// This is the program for binary search.

#include <iostream>
using namespace std;

int binarysearch(int a[], int n, int key)
{
    int s = 0, e = n - 1;
    int mid;

    while (s <= e)
    {
        mid = (s + e) / 2;
        if (a[mid] == key)
        {
            // found
            return mid;
        }
        else if (a[mid] > key)
        {
            e = mid - 1;
        }
        else
            e = mid + 1;
    }
    return -1;
}


int main()
{
    int a[] = {1, 3, 5, 10, 12, 15, 17};
    int n = sizeof(a) / sizeof(int);
    int key; //key means which element is to find.
    cin >> key;

    int searchindex = binarysearch(a, n, key);
    if (searchindex == -1)
    {
        cout << key << " Element not found" << endl;
    }
    else
    {
        cout << key << " Element found at index " << searchindex << endl;
    }

    return 0;
}