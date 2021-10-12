#include<stdio.h>
#include<stdlib.h>
typedef struct node{
    char data;
    struct node * next;
}NODE;
void printList(NODE* head){
    NODE* ptr=head;
    if(head==NULL)
        return;
    while(ptr!=NULL){
        if(ptr!=head)
            printf(" ");
        printf("%c",ptr->data);
        ptr=ptr->next;
    }
    printf("\n");
}//Fuction used to print the linked list
NODE* createNode(char dt){
    NODE* n=(NODE*)malloc(sizeof(NODE));
    n->data=dt;
    n->next=NULL;
    return n;
}//Function that creates and returns a pointer to a NODE
NODE* input(int n){
    NODE* head=NULL,*tail=NULL,*pt;
    char num;
    for(int i=0;i<n;i++){
        scanf(" %c",&num);
        pt=createNode(num);
        if(head==NULL)
            head=tail=pt;
        else{
            tail->next=pt;
            tail=pt;
        }
    }
    return head;
}//function that takes in the input in the form of a linked list and returns the head
NODE* solve(NODE*,int);
int main(){
    int n,k;
    scanf("%d %d",&n,&k);
    NODE* head=input(n);
    printList(solve(head,k));
    return 0;
}
NODE* solve(NODE* A,int B){
    int k=0;
    NODE *prev=NULL,*p=A,*next=NULL,*q=NULL,*last=NULL,*head=NULL;
    
    while(p){
        q=p;
        prev=NULL;
        while(k<B){
            next = p->next;
            p->next=prev;
            prev=p;
            p=next;
            k++;
        }
        if(k==B){
            if(head==NULL){
                head=prev;
            }
            else{
                last->next=prev;
            }
            k=0;
        }
        last=q;
    }
    return head;
}
