/* Write a program in c that will reverse a string using stack as an auxiliary data structure. */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 1000

/* Declare variables globally */
int top = 0;
char stack[MAX];

/* Function Prototype for push and pop operation */
void push(char);
char pop();

/*Driver code*/
int main(void)
{
    /* Create variables and base address of the block */
    char *str;
    unsigned int i;

    /* Dynamically allocate memory using malloc() */
    str = (char *)malloc(MAX * sizeof(char *));

    /*Taking string input from the user*/
    scanf("%[^\n]%*c", str);

    /*Pushing characters of the string "str" on the stack*/
    for (i = 0; i < strlen(str); i++)
    {
        push(str[i]); /*Calling push function */
    }

    /*Poping characters from the stack and store in string str */
    for (i = 0; i < strlen(str); i++)
    {
        str[i] = pop(i); /* Calling pop function */
    }

    /*Printing the reversed string */
    printf("%s\n", str);

    /* Free the memory */
    free(str);
}

/*The function defination of push*/
void push(char item)
{
    stack[top++] = item;
}

/*The function defination of pop*/
char pop()
{
    return stack[--top];
}
