#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
struct stack
{
    int index;
    int size;
    int *p;
};
void createStack(struct stack *var, int size)
{
    var->p = malloc(sizeof(int) * size);
    var->index = -1;
    var->size = size;
}
int isFull(struct stack var)
{
    if (var.index == var.size - 1)
        return 1;
    else
        return 0;
}
int isEmpty(struct stack var)
{
    if (var.index == -1)
        return 1;
    else
        return 0;
}
void push(struct stack *var, int value)
{
    var->index++;
    var->p[var->index] = value;
    printf("\nElement Pushed to Stack\n");
}
int pop(struct stack *var)
{
    var->index--;
    printf("\nElement Popped from Stack\n");
    return var->p[var->index + 1];
}
void displaystack(struct stack var)
{
    if (!isEmpty(var))
    {
        printf("There are %d Elements in Stack of Size %d\n\n", var.index + 1, var.size);
        printf("The Elements in the Stack are:\n");
        for (int i = 0; i <= var.index; i++)
        {
            printf("%d ", var.p[i]);
        }
    }
    else
    {
        printf("Stack is Empty\n");
    }
}
void main()
{
    struct stack stavar;
    int size;
    printf("Enter the size of Stack\n");
    scanf("%d", &size);
    createStack(&stavar, size);
    while (1)
    {
        printf("Press 1 to Push Element in Stack\n");
        printf("Press 2 to Pop Element from Stack\n");
        printf("Press 3 to Display the Elemets if Stack\n");
        printf("Press 0 to delete Stack and Exit\n");
        int choice;
        scanf("%d", &choice);
        if (choice == 1)
        {
            if (!isFull(stavar))
            {
                int value;
                printf("Enter the Element which you want to Enter in Stack\n");
                scanf("%d", &value);
                push(&stavar, value);
            }
            else
            {
                printf("Stack is Full\n");
            }
        }
        else if (choice == 2)
        {
            if (!isEmpty(stavar))
            {
                printf("The Element Popped from the Stack is %d\n", pop(&stavar));
            }
            else
            {
                printf("Stack is Empty\n");
            }
        }
        else if (choice == 3)
        {
            displaystack(stavar);
        }
        else if (choice == 0)
        {
            free(stavar.p);
            printf("Stack Deleted\n");
            exit(0);
        }
        printf("\n\n");
    }
    getch();
}
