// Coin Change Problem
// Input :
// 3
// 5
// 1 2 3
// Output :
// 2

#include <bits/stdc++.h>
using namespace std;

int coinchange(vector<int>& a, int sum, int n,
			vector<vector<int> >& dp)
{
	if (sum == 0)
		return dp[n][sum] = 1;
	if (n == 0)
		return 0;
	if (dp[n][sum] != -1)
		return dp[n][sum];
	if (a[n - 1] <= sum) {
		// Either Pick this coin or not
		return dp[n][sum] = coinchange(a, sum - a[n - 1], n, dp)
						+ coinchange(a, sum, n - 1, dp);
	}
	else // We have no option but to leave this coin
		return dp[n][sum] = coinchange(a, sum, n - 1, dp);
}

int32_t main()
{
	int tc = 1;
	//cin >> tc;
	while (tc--) {
		int n, sum;
		// Input the no of coins
		cin >> n;
		// Input the sum to get
		cin >> sum;
		// Input Coins denominations
		vector<int> a(n);
		for(int i=0; i<n; i++) 	cin >> a[i];
		vector<vector<int> > dp(n + 1,
								vector<int>(sum + 1, -1));
		int res = coinchange(a, sum, n, dp);
		cout << res << endl;
	}
}
