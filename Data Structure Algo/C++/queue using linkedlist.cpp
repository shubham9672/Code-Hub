#include<bits/stdc++.h>
using namespace std;
struct node{
	int data;
	node* next;
	
};
node* rear=NULL;
node* front=NULL;
void enqueue(int x){
	node* temp=new node();
	temp->data=x;
	temp->next=NULL;
	if(rear=NULL){
		rear=temp;
		return;
	} 
	rear->next=temp;
	rear=temp;
	return;
}
void dequeue(){
	if(front=NULL){
		cout<<"underflow";
		return;
	}
	node* temp=front;
	front=temp->next;
	free(temp);
}
void print(){
	node* temp=front;
	while(temp!=NULL){
		cout<<temp->data<<" ";
		temp=temp->next;
	}
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
