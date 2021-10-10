#include <iostream>
#include <vector>
using namespace std;

void print_vector(vector<int> &v) {      // funtion to print elements of a vector
    for (int i = 0; i < v.size(); i++) { // size() funtion returns size of the vector
        cout << v[i] << " ";
    }
    cout << "\n";
}

int main() {
    
    int size;
    vector<int> myvector;


    //--------------I/O-------------------------
    cout << "Enter the size of vector: ";
    cin >> size;
    int x;
    for (int i = 0; i < size; i++) {
        cin >> x;
        myvector.push_back(x);
    }
    print_vector(myvector);
    //------------------------------------------


    //----------------pop_back()----------------
    cout << "Before pop_back()\n:"
    print_vector(myvector);
    myvector.pop_back();
    cout << "After pop_back()\n";
    print_vector(myvector);
    //------------------------------------------


    //--------------size()----------------------
    cout << "The size of the vector is " << myvector.size();
    //------------------------------------------



    //---------------erase()--------------------
    cout << "before erase()\n";
    print_vector(myvector);
    myvector.erase();
    cout << "after erase()\n";
    print_vector(myvector);
    //------------------------------------------



    return 0;
}
