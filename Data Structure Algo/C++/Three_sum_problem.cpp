 #include<bits/stdc++.h>
    using namespace std;
    int main()
    {
        int n=6;
        //cin>>n;
        int target=24;
        //cin>>target;
        bool found=false;
        vector<int> a={12,3,6,9,34,25};
        /*for(auto &i:a)
        {
            cin>>i;
        }*/

        sort(a.begin(),a.end());
       
        for(int i=0;i<n;i++)
        {
            int low=i+1; int high= (n-1);
            while(low<high)
            {
                   int current=a[i]+a[low]+a[high];
                   if(current==target)
                   {
                       found=true;
                       break;
                   }
                   else if(current>target)
                   {
                       high--;
                   }
                   else if(current<target)
                   {
                       low++;
                   }
            }
           
        }
        if(found)
        {
            cout<<"True";
        }
        else{
            cout<<"False";
        }
    }
