/* This program compares the equality of three numbers given by the user */

#include<iostream>
using namespace std;

int main()
{
    system("cls");
    int a,b,c,count = 1;
    cout<<"Enter three values: ";
    cin>>a>>b>>c;
    if(a==b && b==c)
        count = 3;
    else
        if(a==b || b==c)
            count = 2;
        else
         count = 0;
    cout<<"\nTotal number of equal values is "<<count<<endl;
    system("pause");
}
