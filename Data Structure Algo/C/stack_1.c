# include<stdio.h>
int a[10];
int ind=-1;
void push(int num)
{
	if(ind<9)
	{
		a[++ind]=num;
		
	}
	else
	{
		printf("Stack full. Cannot add any more elements.\n");
	}
	
}
int pop()
{
	if(ind==-1)
	{
		printf("Stack empty.\n");
		return -12;
	}
	  
	int X=a[ind--];
	return X;
}
void display()
{
	if(ind==-1)
       printf("Stack is empty\n");
    else
    {
    int i;
       for(i=0;i<=ind;i++)
       {
       	  printf("\n %d",a[i]);
	   }
	   printf("\n");
   }
	
}
void main()
{
	int x,ch,num;
	
	
	do
	{
		printf("\n\nEnter 1 to push \n      2 to pop \n      3 to display\n\n");
		scanf("%d",&ch);
	switch (ch)
	{
		case 1:
		       printf("The element you want to insert\n");
		       scanf("%d",&num);
		       push(num);
		       break;
		case 2:x=pop();
		       break;
		       
		case 3:display();
		       break;
		
		case 0: break;
		
	}
    }
	while(1);
}
