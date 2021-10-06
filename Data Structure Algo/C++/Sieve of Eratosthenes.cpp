#include <bits/stdc++.h>
#include<algorithm>
#include<vector>
#include<map>
#define ll long long
using namespace std;
void SieveOfEratosthenes(int n)
{	bool prime[n + 1];
  for(int i=0;i<n+1;i++)
  prime[i]=true;

	for (int i = 2; i * i <= n; i++)
	{	if (prime[i] == true)
		{	for (int j = i * i; j <= n; j += i)
				prime[j] = false;
		}
	}
	for (int i= 2; i<= n; i++)
		if (prime[i])
			cout << i << " ";
}
int main()
{
	int n;
	cout<<"Enter the number";
	cin>>n;
	cout << "All Prime numbers smaller than or equal to n are " << n << endl;
	SieveOfEratosthenes(n);
	return 0;
}

