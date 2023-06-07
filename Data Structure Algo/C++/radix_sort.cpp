#include <iostream>
using namespace std;

int Maximum(int arr[], int n)
{
	int max = arr[0];
	for (int i = 1; i < n; i++)
		if (arr[i] > max)
			max = arr[i];
	return max;
}

// Count sort of arr[].
void countSort(int arr[], int n, int exp)
{
	int a[n], count[10] = {0};
	for (int i = 0; i < n; i++)
		count[(arr[i] / exp) % 10]++;
	for (int i = 1; i < 10; i++)
		count[i] += count[i-1];
	for (int i = n - 1; i >= 0; i--)
	{
		a[count[(arr[i] / exp) % 10] - 1] = arr[i];
		count[(arr[i] / exp) % 10]--;
	}
	for (int i = 0; i < n; i++)
		arr[i] = a[i];
}

void radixsort(int arr[], int n)
{
	int exp, m;
	m = Maximum(arr, n);
	for (exp = 1; m/exp > 0; exp *= 10)
		countSort(arr, n, exp);
}

int main()
{
	int n;
	cout<<"\nEnter the number of elements to be sorted";
	cin>>n;

	int arr[n];
	for(int i = 0; i < n; i++)
	{
		cout<<"Enter element "<<i+1<<": ";
		cin>>arr[i];
	}

	radixsort(arr, n);
	cout<<"\n Sorted elements are: ";
	for (int i = 0; i < n; i++)
		cout<<arr[i]<<" ";
	return 0;
}
