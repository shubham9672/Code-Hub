#include<bits/stdc++.h>
using namespace std;

bool isSafe(int chess[8][8], int row, int col){

    if(row<0 || row>=8)
        return false;
    if(col<0 || col>=8)
        return false;
    if(chess[row][col] != -1)
        return false;
    
    return true;
}

bool knight(int chess[8][8], int row, int col, int n, vector<int> &x, vector<int> &y){
    
    if(n == 64)
        return true;

    for(int i=0; i<8; i++){
        if(isSafe(chess, row + x[i], col + y[i])){
            chess[row + x[i]][col + y[i]] = n;

            if(knight(chess, row + x[i], col + y[i], n+1, x, y))
                return true;
            else    
                chess[row + x[i]][col + y[i]] = -1;
        }
    }

    return false;
}

void print(int chess[8][8]){

    for(int i=0; i<8; i++){
        for(int j=0; j<8; j++){
            cout<<chess[i][j]<<" ";
        }
        cout<<endl;
    }

}

int main(){

    int chess[8][8];
    memset(chess, -1, sizeof(chess));
    vector<int> x {-2, -2, -1, -1, 1, 1, 2, 2};
    vector<int> y {1, -1, 2, -2, 2, -2, 1, -1};
    chess[0][0] = 0;
    if(knight(chess, 0, 0, 1, x, y))
        print(chess);

    return 0;
}