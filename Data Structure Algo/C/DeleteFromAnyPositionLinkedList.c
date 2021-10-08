#include<stdio.h>
#include<stdlib.h>
struct node{
	int data;
	struct node* next;
};
struct node* head = NULL;
void insert()
{
	struct node *temp,*temp1;
	temp = (struct node*)malloc(sizeof(struct node));
	printf("ENTER THE DATA : \n");
	scanf("%d",&temp->data);
	temp->next = NULL;
	if(head==NULL)
	{
		head = temp;
	}
	else
	{
		temp1 = head;
		while(temp1->next!=NULL)
		{
			temp1 = temp1->next;
		}
		temp1->next = temp;
	}
}
void display()
{
	struct node* temp;
	temp = head;
	while(temp!=NULL)
	{
		printf("%d ",temp->data);
		temp = temp->next;
	}
	printf("\n");
}
void del()
{
	struct node* temp = head;
	int n,i;
	printf("ENTER THE POSITION TO DELETE : \n");
	scanf("%d",&n);
	if(n==1)
	{
		head = temp->next;
		free(temp);
	}
	else
	{
		for(i = 0; i<n-2; i++)
		{
			temp = temp->next;
		}
		struct node* temp1 = temp->next;
		temp->next = temp1->next;
		free(temp1);
	}
}
int main()
{
	int c;
	while(1)
	{
		printf("PRESS 1 TO ADD ELEMENTS IN THE LINKED LIST\n");
		printf("PRESS 2 TO DISPLAY ELEMENTS IN THE LINKED LIST\n");
		printf("PRESS 3 TO DELETE ELEMENTS FROM THE LINKED LIST\n");
		printf("PRESS 0 TO EXIT THE PROCESS\n");
		scanf("%d",&c);
		switch(c)
		{
			case 1:insert(); break;
			case 2:display();break;
			case 3:del();break;
			case 0:exit(0);break;
		}
	}
	return 0;
}
