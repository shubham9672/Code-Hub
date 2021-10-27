#include<bits/stdc++.h>
using namespace std;
struct node{
	int data;
	node* next;
};
node* top=NULL;
void push(int x){
	node* temp=new node();
	temp->data=x;
	temp->next=NULL;
	if(top==NULL){
		top=temp;
		return;
	}
	temp->next=top;
	top=temp;
}
void pop(){
	node* temp=top;
	if(top==NULL){
		cout<<"underflow";
		return;
	}
	top=temp->next;
	free(temp);
}
void print(){
	node* temp=top;
	while(temp!=NULL){
		cout<<temp->data<<" ";
		temp=temp->next;
	}
}
int main(){
	int n,x;
	cout<<"Enter n: ";
	cin>>n;
	for(int i=0;i<n;i++){
		cout<<"Enter x: ";
		cin>>x;
		push(x);
	}
	pop();
	print();
}
