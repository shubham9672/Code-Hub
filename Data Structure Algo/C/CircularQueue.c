#include<stdio.h>
#include<stdlib.h>
struct queue{
    int *a;
    int size;
    int f;
    int r;
};
int isFull(struct queue *q)
{
if((q->r+1)%q->size==q->f) 
{
    return 1;
}

}
int isEmpty(struct queue *q)
{
    if(q->r==q->f)
    {
        return 1;
    }
    
}
void enqueue(struct queue *q, int val)
{
    if(isFull(q)){
        printf("Full!");
    }
    else{
     q->r=(q->r+1)%q->size; 
     q->a[q->r]=val;
     printf("Enter the Elements-%d \n",val);
    }
}
int dequeue(struct queue *q){
    int a=-1;
    if(isEmpty(q))
    {
         printf("Empty!");
    }
    else{ 
        q->f=(q->f+1)%q->size;
        return q->a[q->f];
    }
}

int main()
{
    struct queue q;
    q.size=20;
    q.f=q.r=0; 
    q.a=(int*)malloc(q.size *sizeof(int));
    enqueue(&q,3);
    enqueue(&q,23);
    enqueue(&q,6);
    enqueue(&q,7);
    enqueue(&q,1);
    enqueue(&q,45);
    enqueue(&q,65);
    enqueue(&q,90);
    printf("dequeue element is - %d \n",dequeue(&q));
   
 
    
}

    

    
