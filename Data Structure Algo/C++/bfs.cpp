#include<bits/stdc++.h>
using namespace std;

class Solution
{
    public:
   
	vector<int>bfsOfGraph(int V, vector<int> adj[])
	{
	    
	    bool visited[V]={0};
	    queue<int>q;
	    vector<int>v;
	    q.push(0);
	    while(!q.empty()){
	        int t=q.front();
	        q.pop();
	        v.push_back(t);
	        for(auto i=adj[t].begin();i!=adj[t].end();i++){
	            if(visited[*i]==0){
	                visited[*i]=1;
	                q.push(*i);
	            }
	        }
	    }
	    return v;
	}
};


int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int V, E;
    	cin >> V >> E;

    	vector<int> adj[V];

    	for(int i = 0; i < E; i++)
    	{
    		int u, v;
    		cin >> u >> v;
    		adj[u].push_back(v);
    
    	}
        
        Solution obj;
        vector<int>ans=obj.bfsOfGraph(V, adj);
        for(int i=0;i<ans.size();i++){
        	cout<<ans[i]<<" ";
        }
        cout<<endl;
	}
	return 0;
}  