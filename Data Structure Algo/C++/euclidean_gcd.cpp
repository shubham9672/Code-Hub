#include <bits/stdc++.h>
#define ll long long int
using namespace std;
ll num1, num2;

ll gcd(ll a, ll b){
    if (a==b) return a;
    if (a<b) {
        ll temp = a;
        a = b;
        b = temp;
    }
    while(b!=0 && a!=b){
        b = b%a;
        a = b;
    }
    return a;
}
int main(){
    cout<<"Please Enter 2 numbers to find out their GCD: "<<endl;
    cin>>num1>>num2;
    ll result = gcd(num1, num2);
    cout<<"The GCD of "<<num1<<" and "<<num2<<" is: "<<result<<endl;
    return 0;
}