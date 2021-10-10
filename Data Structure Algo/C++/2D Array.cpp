#include <iostream>
using namespace std;

int matrix_search(arr[][], int n, int m, int key) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (arr[i][j] == key) {
                return 1;
            }
        }
    }
    return 0;
}

int main() {
    int n;
    int m;
    cin >> n >> m;
    int arr[n][m];

    for (int i = 0; i<n; i++) {
        
        for (int j = 0; j < m; j++) {
            cin >> arr[i][j];
        }
    }
    //----------------printing a matrix------------------
    for (int i = 0; i<n; i++) {
        for (int j = 0; j < m; j++) {
            cout << arr[i][j] << " ";
        }
        cout << "\n";
    }
    //----------------------------------------------------



    //----------------searching in a matrix----------------------
    int key;
    cin >> key;
    if (matrix_search(arr, n, m, key) == 1) {
        cout << "Found!";
    }
    else {
        cout << "Not found.";
    }

    //---------------------spiral traversal-------------------- 
    int start_row, end_row, start_column, end_column;
    start_row = 0;
    end_row = n-1;
    start_column = 0;
    end_column = m-1;
    while (start_row <= end_row && start_column <= end_column) {
        //print start row;
        for (int i = start_column; i <= end_column; i++) {
            cout << arr[start_row][i] << " ";
        }
        start_row++;
        //print end_column;
        for (int i = start_row; i<= end_row; i++) {
            cout << arr[i][end_column] << " ";
        }
        end_column--;
        //print end_row;
        for (int i = end_column; i >= start_column; i--) {
            cout << arr[end_row][i] << " ";
        }
        end_row--;
        //print start_column;
        for (int i = end_row; i >= start_row; i--) {
            cout << arr[i][start_column] << " ";
        }
        start_column++;
    }
    //---------------------------------------------------------



    return 0;
}
