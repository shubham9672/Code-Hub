#include<bits/stdc++.h>
using namespace std;
#define int long long int

const int INF=1e18;
const int mod=1e9+7; 
const int N=200005;

// binary exponentiation function to find x^n in O(logn)
int fastPow(int x,int n){
    int result=1;
    while(n>0){
        if(n%2==1){
            result=x*result%mod;
        }
        x=x*x%mod;
        n=n/2;
    }
    return result;
}

int fact[200005],invfact[200005];

// precomputing values of factorial and inverse factorial in O(n) 
void calc(){

    fact[0]=1;
    for(int i=1;i<N;i++){
        fact[i]=i*1ll*fact[i-1]%mod;
    }

    invfact[N-1]=fastPow(fact[N-1],mod-2); 
    for(int i=N-2;i>=0;i--){
        invfact[i]=invfact[i+1]*(i+1)%mod;
    }
}

// function returning the required binomial coefficient after doing modulo operation with 10^9+7
int ncr(int n,int r){

    /*
        nCr = n! / (r! * (n-r)!)
            = n! * inverse(r!) * inverse((n-r)!)
    */

    if(r>n || n<0 || r<0){
        return 0;
    }
    return fact[n]*invfact[r]%mod*invfact[n-r]%mod;
}

int32_t main(){
    int t;
    cout<<"Enter number of test cases"<<endl;
    cin>>t;

    calc();

    // now our fact and inv fact arrays are ready

    while(t--){
        int n,r;
        cout<<"Enter values of n and r"<<endl;
        cin>>n>>r;
        int bin_coef=ncr(n,r);
        cout<<"Required binomial coeff is: "<<bin_coef<<endl;
    }
    return 0;
}


/*
    time complexity : O(t*n)  , where t is number of test cases and n is the value provided for nCr
    space complexity : O(n)
*/