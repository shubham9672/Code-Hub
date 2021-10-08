#include <stdio.h> 
#include <stdlib.h> 
struct QNode { 
    int key; 
    struct QNode* next; 
}; 
struct Queue { 
    struct QNode *front, *rear; 
}; 
struct QNode* newNode(int k) 
{ 
    struct QNode* temp = (struct QNode*)malloc(sizeof(struct QNode)); 
    temp->key = k; 
    temp->next = NULL; 
    return temp; 
} 
struct Queue* createQueue() 
{ 
    struct Queue* q = (struct Queue*)malloc(sizeof(struct Queue)); 
    q->front = q->rear = NULL; 
    return q; 
} 
void enqueue(struct Queue* q, int k) 
{ 
    struct QNode* temp = newNode(k); 
    if (q->rear == NULL) 
    { 
        q->front = q->rear = temp; 
        return; 
    } 
    q->rear->next = temp; 
    q->rear = temp; 
} 
int dequeue(struct Queue* q) 
{ 
    if (q->front == NULL) 
        return; 
    struct QNode* temp = q->front; 
    q->front = q->front->next; 
    if (q->front == NULL) 
        q->rear = NULL; 
    int data=temp->key;
    free(temp);
    return data;
} 
int main() 
{ 
    int c,item;
    struct Queue* q = createQueue(); 

    do
    {
       printf("\n********QUEUE MENU********\n");
       printf("Enter 1 to enqueue to the queue\n");
       printf("Enter 2 to dequeue to the queue\n");
       printf("Enter 3 for exit\n");
       scanf("%d",&c);
       switch(c)
       {
           case 1:printf("Enter data that you want to push :");
                  scanf("%d",&item);
                  enqueue(q,item);
                break;
           case 2:printf("%d has been dequeued from the queue\n",dequeue(q));             
                break;
           case 3:printf("Exiting queue process\n");
                break;
       }
    }while(c!=3);
	return 0; 
} 