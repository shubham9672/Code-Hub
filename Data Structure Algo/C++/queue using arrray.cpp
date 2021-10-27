#include<bits/stdc++.h>
using namespace std;
int a[51];
int front =-1;
int rear =-1;
void enqueue(int x){
	if(rear==51){
		cout<<"underflow";
		return;
	}
	if(front==-1) front++;
	a[++rear]=x;
}
void dequeue(){
	if(front==-1 && rear==-1){
		cout<<"underflow";
		return;
	}
	if(front==rear){
		front=-1;
		rear=-1;
		return;
	}
	front++;
}
bool isEmpty(){
	if(rear==-1 && front==-1) return true;
	return false;
}
void print(){
	for(int i=front;i<=rear;i++){
		cout<<a[i]<<" ";
	}
	cout<<endl;
}
int main(){
	int n,x;
	cout<<"Enter n: ";
	cin>>n;
	while(n--){
		cout<<"Enter x: ";
		cin>>x;
		enqueue(x);
	}
	print();
	dequeue();
	print();
}
