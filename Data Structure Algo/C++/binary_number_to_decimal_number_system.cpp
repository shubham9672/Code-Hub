//C++ program to convert a binary number to decimal number system
#include <bits/stdc++.h>
using namespace std;

// Function to convert a binary number to decimal number system
int convertBinaryToDecimal(int n)
{
    int decimalNumber=0,i=0,remainder;
    while (n!=0)
    {
        remainder = n%10;
        n /= 10;
        decimalNumber += remainder*pow(2,i);
        i++;
    }
    return decimalNumber;
}

// Driven Program to check above
int main()
{
    int n;
    cout <<"Enter a binary number: ";
    cin >> n;
    cout << n << " in binary = " << convertBinaryToDecimal(n) <<" in decimal";
    return 0;
}
