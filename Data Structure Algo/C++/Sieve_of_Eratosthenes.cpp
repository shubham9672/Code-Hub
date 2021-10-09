#include<iostream>
using namespace std;

int main(){
    int n;
    cin >> n;
    int num_arr[n+1];// creating a number array
    for (int i = 1; i < n+1; i++){
        num_arr[i] = i;
    }

    bool arr[n+1]= {0} ;// another array to mark true or false ,firstly we assume all number are prime
    for (int k = 2; k <= n ; k++){
        if(arr[k] == 0){
            for (int j = k*k; j < n+1; j+=k){
                arr[j] = 1;
            }   
        }  
    }

    for (int z = 1; z < n+1; z++){
        if (arr[z] == 0){
            cout << num_arr[z] << " ";
        } 
    }
}


//Time complexity : n*log(log(n))
