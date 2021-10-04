#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct Node
{
    char name[20];
    int roll;
    struct Node *next;
}*first=NULL;

int count(struct Node *p)
{
    int l = 0;
    while (p)
    {
        l++;
        p = p->next;
    }
    return l;
}

void Insert(struct Node *p, int index, int x, char arr[])
{
    struct Node *t;
    int i;
    if (index < 0 || index > count(p))
    {
        printf("\nPlease Enter A Valid Index..!!");
        return;
    }
    t = (struct Node *)malloc(sizeof(struct Node));
    t->roll = x;
    strcpy(t->name, arr);

    if (index == 0)
    {
        t->next = first;
        first = t;
    }
    else
    {
        for (i = 0; i < index - 1; i++)
        {
             p = p->next;
        }
        t->next = p->next;
        p->next = t;
    }
}

int Delete(struct Node *p, int index)
{
    struct Node *q = NULL;
    int x = -1, i;
    if (index < 1 || index > count(p))
    {
        return -1;
    }
    if (index == 1)
    {
        q = first;
        x = first->roll;
        first = first->next;
        free(q);
        return x;
    }
    else
    {
        for (i = 0; i < index - 1; i++)
        {
            q = p;
            p = p->next;
        }
        q->next = p->next;
        x = p->roll;
        free(p);
        return x;
    }
}

void display_list(struct Node *p)
{
    printf("Current Class Database Is:\n");
    while (p != NULL)
    {
        printf("\n%d %s", p->roll, p->name);
        p = p->next;
    }
}

int main()
{
    int roll, retry=0, command, index;
    char name[20];
    printf("*****CLASS DATABASE*****\n");
    do
    {
        printf("What Do You Want To Do..??\n1.Add Student Info\n2.Delete Student Info\n\nEnter Command Code:");
        scanf("%d", &command);

        if(command==1)
        {
            printf("Enter Student's Name:");
            scanf("%s", name);
            printf("Enter Student's Roll Number:");
            scanf("%d", &roll);
            printf("Enter Index At Which You Want To Insert:");
            scanf("%d", &index);
            Insert(first, index, roll, name);
            if (index < 0 || index > count(first))
            {
                return 0;
            }
            printf("\n\nData Inserted...!!\n\n");
        }
        else if(command==2)
        {
            printf("Enter Index Which You Want To Delete:");
            scanf("%d", &index);
            Delete(first, index+1);
            printf("\n\nData Deleted...!!\n\n");
        }

        display_list(first);
        printf("\n\nDo you want to perform more operations...??\n1.YES..!!\n2.NO..!!\nEnter Command Code:");
        scanf("%d", &retry);

        if(retry==2)
        {
            printf("Thank You, Bbyee..!!");
        }
        
    }while(retry==1);
    return 0;
}