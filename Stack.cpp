#include <iostream>
using namespace std;

#define n 50

class stack{
    int* arr;
    int top;
    
    public:
    stack()
    {
        arr=new int[n];
        top=-1;
    }
    
    void push(int x)
    {
        if(top==n-1)
        {
            cout<<" stack overflow "<<endl;
            return;
        }
        top++;
        arr[top]=x;
    }
    
    void pop()
    {
        if(top==-1)
        {
            cout<<"no element to pop"<<endl;
        }
        top--;
    }
    
    int Top()
    {
        if(top==-1)
        {
            cout<<"no element in stack"<<endl;
            return -1;
        }
        return arr[top];
    }
    
    bool empty(){
        return top==-1;
    }
};
