//  Write a program to check the validity of an expression containing nested parentheses.
//  Inputs: [119 - 5 * (6 + 4 ) ]
//          { 2 + ( 2 * 3 )]

#include <stdio.h>
#include <stdlib.h>

struct Stack{
    int size;
    int top;
    char *arr;
};

int isEmpty(struct Stack *ptr){
    if(ptr->top==-1){
        return 1;
    }
    return 0;
}

int isFull(struct Stack *ptr){
    if(ptr->top==ptr->size-1){
        return 1;
    }
    return 0;
}

void push(struct Stack *ptr, char val){
    if(isFull(ptr)){
        printf("\nStack Overflow.\n");
    }
    else{
        ptr->arr[++ptr->top]=val;
    }
}

void pop(struct Stack *ptr){
    if(isEmpty(ptr)){
        printf("\nStack Underflow.\n");
    }
    else{
        ptr->arr[ptr->top--]='\0';
    }
}

char stackTop(struct Stack *ptr){
    if(isEmpty(ptr)){
        printf("\nStack Underflow.\n");
        return '\0';
    }
    else{
        return ptr->arr[ptr->top];
    }
}

int parenthesisMatch(char *sample, int len){
    struct Stack *space;
    space->size=len;
    space->top=-1;
    space->arr=(char *)malloc(sizeof(char)*len);
    for (int i = 0; sample[i]!='\0'; i++)
    {
        if(sample[i]=='(' || sample[i]=='[' || sample[i]=='{'){
            push(space, sample[i]);
        }
        else if(sample[i]==')'){
            if(stackTop(space)=='('){
                pop(space);
                continue;
            }
            else{
                return 0;
            }
        }
        else if(sample[i]==']'){
            if(stackTop(space)=='['){
                pop(space);
                continue;
            }
            else{
                return 0;
            }
        }
        else if(sample[i]=='}'){
            if(stackTop(space)=='{'){
                pop(space);
                continue;
            }
            else{
                return 0;
            }
        }
    }
    if(isEmpty(space)){
        return 1;
    }
    return 0;
}





int main(){
    char testCase[]="{ 2 + ( 2 * 3 )]";
    int len=sizeof(testCase)/sizeof(testCase[0]-1);

    if(parenthesisMatch(testCase, len)){
        printf("\n\n\nCongratulations! \nParethesis are perfectly balanced, so its a VALID EXPRESSION.");
    }
    else{
        printf("\n\n\n(0_0) \nNot a valid Expression. \nParenthesis are NOT balanced");
    }

 
    return 0;
}
