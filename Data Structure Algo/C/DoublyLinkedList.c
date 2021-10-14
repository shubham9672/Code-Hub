#include <stdio.h>
#include <stdlib.h>
struct Node
{
    int data;
    struct Node *next;
    struct Node *prev;
};
struct Node *head;
struct Node *tail;
void create()
{
    int val;
    int choice=1;
    while(choice==1)
    {
        struct Node *newnode=(struct Node*)malloc(sizeof(struct Node));
        printf("\nEnter value for a node:");
        scanf("%d",&val);
        newnode->data=val;
        newnode->next=0;
        newnode->prev=0;
        if(head==0)
        {
            head=tail=newnode;
        }
        else
        {
            tail->next=newnode;
            newnode->prev=tail;
            tail=tail->next;
        }
        printf("\nPress 1 to add another node or press 0 to stop.");
        scanf("%d",&choice);
    }
}
void display()
{
    struct Node *n=head;
    if(head==0)
        printf("\nThe doubly linked list is empty!");
    else
    {
        printf("\nDoubly Linked List:");
        while(n!=0)
        {
            printf("\t%d",n->data);
            n=n->next;
        }
    }
}
void insertatbeg(int val)
{
    struct Node *n=(struct Node*)malloc(sizeof(struct Node));
    n->data=val;
    n->prev=0;
    n->next=head;
    head->prev=n;
    head=n;
}
void insertatend(int val)
{
    struct Node *n=(struct Node*)malloc(sizeof(struct Node));
    n->data=val;
    n->prev=tail;
    n->next=0;
    tail->next=n;
    tail=n;
}
int length_return()
{
    struct Node *n=head;
    int length=0;
    while(n!=0)
    {
        length++;
        n=n->next;
    }
    return length;
}
void insertatpos()
{
    int val, index;
    printf("\nEnter the value to append:");
    scanf("%d",&val);
    printf("\nEnter the index to append that value at:");
    scanf("%d",&index);
    int length=length_return();
	if(index==0)
		insertatbeg(val);
	else if(index==length)
		insertatend(val);
	else
    {
        struct Node *n=(struct Node*)malloc(sizeof(struct Node));
        struct Node *temp=head;
        n->data=val;
        for(int i=0;i<index-1;i++)
            temp=temp->next;
        n->next=temp->next;
        n->prev=temp;
        temp->next=n;
        temp=temp->next;
        temp->prev=n;
    }
}
void deleteatbeg()
{
    if(head==0)
        printf("\nThe doubly linked list is empty!");
    else
    {
        printf("\nThe value %d was removed from the start of the linked list.",head->data);
        head=head->next;
        if(head==0)
            tail=0;
        else
            head->prev=0;
    }
}
void deleteatend()
{
    if(tail==0)
        printf("\nThe doubly linked list is empty!");
    else
    {
        printf("\nThe value %d was removed from the start of the linked list.",tail->data);
        tail=tail->prev;
        if(tail==0) //If while removing the last element, the tail becomes null
            head=0; //we make head null as well to make the list empty.
        else
            tail->next=0; //Otherwise, we remove the connection of last node from list.
    }
}
void deleteatpos()
{
    int index;
	printf("\nEnter index you want to remove value from:");
	scanf("%d",&index);
	int length=length_return();
	if(length==0)
		printf("\nCannot delete element! Linked List is empty!");
	else if(index>=length || index<0)
		printf("\nError! Invalid index position entered!");
	else if(index==0)
		deleteatbeg();
	else
	{
		struct Node *n=head;
		for(int i=0;i<index-1;i++)
    		n=n->next;
		struct Node *back=n;
		n=n->next;
		n=n->next;
		struct Node *front=n;
		front->prev=back;
		back->next=front;
	}
}
void length_show()
{
    struct Node *n=head;
    int length=0;
    while(n!=0)
    {
        length++;
        n=n->next;
    }
    printf("\nThe length of the linked list=%d",length);
}
void reverse()
{
	if(head==0)
		printf("\nThe compiler is unable to reverse a list that hasn't been created yet.");
    else
	{
		struct Node *currentnode=head;
		struct Node *nextnode;
		while(currentnode!=0)
		{
			nextnode=currentnode->next;
			currentnode->next=currentnode->prev;
			currentnode->prev=nextnode;
    		currentnode=nextnode;
		}
        currentnode=head;
        head=tail;
        tail=currentnode;
	}
}
void main()
{
    create();
    reverse();
    display();
}
