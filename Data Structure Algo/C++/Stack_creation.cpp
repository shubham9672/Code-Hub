#include <iostream>

using namespace std;
 # define max 10

class STACK{
    public:
     int top;
     int stack[max];
     STACK();                  
     void push(int);
     void pop();
     void display();
     
};
 
STACK S;

STACK::STACK(){  
    top=-1;
}

void STACK :: push(int n)
{
    if(top==max-1)
    printf("overflow");
    else
    {
     ++top;
     stack[top]=n;
 
    }
}

void STACK :: pop()
{
    if(top==-1)
    printf("underflow");
    else
    {
        printf("\nelement deleted is %d",S.stack[top]);
        top--;
    }
}

void STACK :: display()
{
    int i;
    if(top==-1)
    printf("empty");
    else
    {
        for(i=top;i>=0;i--)
        printf("%d\n",S.stack[i]);
    }
}



  int main()
{
    while(1)
    {
        
   
    int ch,n,temp;
    cout<<"\n***MENU***"<<endl;
   cout<<"1.push\n2.pop\n3.display\n"<<endl;
   cout<<"choice:";
    cin>>ch;
    
    switch(ch)
    {
        case 1:cout<<"enter an element"<<endl;
               cin>>n;
               
                S.push(n);
               
               break;
        case 2:S.pop();
                break;
        case 3:S.display();
                break;
        case 4:exit(0);
    }
 }
}



