
\#include<bits/stdc++.h>
using namespace std;
struct node{
	int data;
	node* link;
};
struct node* head;
void Insert_start(int x){
	node* temp = new node();
	temp->data=x;
	temp->link=head;
	head=temp;
	
}
void reverse(){
	node* prev=NULL;
	node* curr=head;
	node* next;
	while(curr!=NULL){
		next=curr->link;
		curr->link=prev;
		prev=curr;
		curr=next;
		//next=next->link;
	}
	head=prev;
}
void Insert_nth(int x, int n){
	node* temp1=head;
	node* temp2 = new node();
	temp2->data=x;
	if(n==1){
		temp2->link=head;
		head=temp2;
		return;
	}
	for(int i=0;i<n-2;i++){
		temp1=temp1->link;
	}
	temp2->link=temp1->link;
	temp1->link=temp2;
}
void Delete(int n){
	node* temp1=head;
	if(n==1){
		head=temp1->link;
		return;
	}
	for(int i=0;i<n-2;i++){
		temp1=temp1->link;
	}
	node* temp2=temp1->link;
	temp1->link=temp2->link;
	free(temp2);
}
void print(){
	node* temp=head;
	while(temp!=NULL){
		printf("%d\t",temp->data);
		temp=temp->link;
	}
	printf("\n");
}
void rec_print_start(node* p){
	//node* temp=head;
	if(p==NULL) return;
	cout<<p->data<<"\t";
	rec_print_start(p->link);
}
void rec_print_end(node* p){
	//node* temp=head;
	if(p==NULL) return;
	rec_print_end(p->link);
	cout<<p->data<<"\t";
}
int main(){
	int i,n,x,y;
	head=NULL;
	printf("How many nos? ");
	scanf("%d",&n);
	for(i=0;i<n;i++){
		printf("Enter no: ");
		scanf("%d%d",&x,&y);
		Insert_nth(x,y);
		print();
	}
	Delete(3);
	print();
	reverse();
	print();
	rec_print_end(head);
	cout<<"\n";
	rec_print_start(head);
	cout<<"\n";
}
