#include<bits/stdc++.h>
using namespace std;

class Solution
{
    public:
    bool isPair(string x)
    {
        stack<char>st;
        int sum=0;
        for(int i=0;i<x.size();i++){
            if(x[i]=='('||x[i]=='{'||x[i]=='['){
                st.push(x[i]);
                sum++;
            }
            else if(x[i]==')'){
                if(st.empty())     return false;
                if (st.top()!='(') return false;
                else {
                    st.pop();
                    sum--;
                    
                }
            }
            else if(x[i]=='}'){
                if(st.empty()) return false;
                if (st.top()!='{') return false;
                else {
                    st.pop();
                    sum--;
                    
                }
            }
            else if(x[i]==']'){
                if(st.empty())     return false;
                if (st.top()!='[') return false;
                else {
                    st.pop();
                    sum--;
                    
                }
            }
            
        }
        if(sum==0) return true;
        else       return false;
    }

};

int main()
{
   int tc;
   string a;
   cin>>tc;
   while(tc--)
   {
       cin>>a;
       Solution obj;
       if(obj.isPair(a))
        cout<<"balanced"<<endl;
       else
        cout<<"not balanced"<<endl;
   }
}  