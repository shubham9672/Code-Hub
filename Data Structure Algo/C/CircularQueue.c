#include <stdio.h>
#include<stdlib.h>
#define MAX 3
void insert();
void del();
void display();
int q[MAX];
int rear= -1;
int front= -1;
int val;

int main()
{
    int ch;
    while(1)
    {
        printf("\n Press 1.Insert, 2.Delete, 3.Display, 4.Exit ");
        printf("\n Enter your choice: ");
        scanf("%d", &ch);
        switch(ch)
        {
            case 1: insert();
            break;
            case 2: del();
            break;
            case 3: display();
            break;
            case 4: exit(1);
            default:
           
            printf("Wrong choice \n");
        }
    }
}

void insert()
{
    if(front==0&&rear==MAX-1)
    printf("Circular Queue is full \n");
else if(front==rear+1)
printf("Circular Queue is full \n");
   
    else
    {
        if(rear==MAX-1 && front!=0)
        rear=-1;
        printf("Enter the value to be inserted \n");
        scanf("%d",& val);
        q[++rear]=val;
        printf("Insertion successful \n");
        if(front==-1)
        front=0;
    }
}

void del()
{
    if(front==-1 && rear==-1)
    printf("Circular Queue is empty \n");
    else if(front==rear)
    {
printf("Delete element is %d \n", q[front]);
front=-1;
rear=-1;
}
else
{
printf("Delete element is %d \n", q[front++]);
    if(front==MAX)
    front=0;

}
}

void display()
{
    if(front==-1)
    printf("Circular Queue is empty \n");
    else
    {
        int i=front;
        printf("Circular Queue -> \n");
        if(front<=rear)
        {
            while(i<=rear)
            printf("%d ", q[i++]);
        }

        else
        {
            while(i<=MAX-1)
            printf("%d ", q[i++]);
            i=0;
            while(i<=rear)
            printf("%d ", q[i++]);
        }
    }
}
