#include<bits/stdc++.h>
using namespace std;
int p=51;
int Stack[50];
int top=-1;
void push(int x){
	if(top==50){
		cout<<"stack iis full";
		return;
	}
	Stack[++top]=x;
}
void pop(){
	if(top==-1){
		cout<<"stack is empty";
		return;
	}
	top--;
}
void print(){
	for(int i=0;i<=top;i++){
		cout<<Stack[i]<<" ";
	}
}
void Top(){
	cout<<Stack[top];
}
bool isEmpty(){
	if(top==-1) return true;
	return false;
}
int main(){
	int n,x;
	cout<<"Enter how many numbers to enter: ";
	cin>>n;
	for(int i=0;i<n;i++){
		cout<<"Enter no to push in stack: ";
		cin>>x;
		push(x);
	}
	pop();
	print();
}
