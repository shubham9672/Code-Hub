#include<bits/stdc++.h>
using namespace std;
int Knpsck(vector<int> wt,vector<int> pr,int W)
{
	int dp[wt.size()+1][W+1];
	for(int i=0;i<=wt.size();i++)
	{
		for(int j=0;j<=W;j++)
		{
			if(i==0||j==0)
				dp[i][j]=0;
			else if(wt[i-1]>j)
				dp[i][j]=dp[i-1][j];
			else
				dp[i][j]=max(pr[i-1]+dp[i-1][j-wt[i-1]],dp[i-1][j]);
		}
	}
	return dp[wt.size()][W];
}
int main()
{
	vector<int> wt={3,4,6,5};
	vector<int> pr={2,3,1,4};
	int W=8;
	cout<<Knpsck(wt,pr,W);
	return 0;
}
