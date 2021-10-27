#include<bits/stdc++.h>
using namespace std;
struct node{
	int data;
	node* next;
};
struct node* head;
void print(){
	node* temp=head;
	while(temp->next!=NULL){
		cout<<temp->data<<"\t";
		temp=temp->next;
	}
	cout<<"\n";
}
int main(){
	node* prev=NULL;
	node* curr=head;
	node*next;
	while(curr->next!=NULL){
		next=curr->next;
		curr->next=prev;
		prev=curr;
		curr=next;
		next=next->next;
	}
}
