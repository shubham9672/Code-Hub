#include <iostream> 
using namespace std; 
void use(int b[], int n, int i) 
{ 
	int lg = i; 
	int l = 2*i + 1; 
	int r = 2*i + 2; 
	if (l < n && b[l] > b[lg]) 
	{
		lg = l; 
	}
	if (r < n && b[r] > b[lg]) 
	{
		lg = r; 
	}
	if (lg != i) 
	{ 
		swap(b[i], b[lg]); 
		use(b, n, lg); 
	} 
} 
void hSort(int b[], int n) 
{ 
	for (int i = n / 2 - 1; i >= 0; i--) 
	{
		use(b, n, i); 
	}
	for (int i=n-1; i>0; i--) 
	{ 
		swap(b[0], b[i]); 
		use(b, i, 0); 
	} 
} 
void print(int b[], int n) 
{ 
	for (int i=0; i<n; ++i) 
	{
		cout << b[i] << " "; 
	}
	cout << "\n"; 
} 
int main() 
{ 
	int b[] = { 4, 9, 1, 8, 3, 5 }; 
	int n = sizeof(b)/sizeof(b[0]); 
	hSort(b, n); 
	print(b, n); 
	return 0;
} 
