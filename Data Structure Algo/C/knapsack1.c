#include<stdio.h>
#include<time.h>
int max(int x,int y)
 {
   return((x>y)?x:y);
 }
int knap(int n,int w[10],int value[10],int m,int v[10][10])
 {
   int i,j;
   for(i=0;i<=n;i++)
   for(j=0;j<=m;j++)
   {
     if(i==0||j==0)
       v[i][j]=0;
     else if(j<w[i])
       v[i][j]=v[i-1][j];
     else
       v[i][j]=max(v[i-1][j],value[i]+v[i-1][j-w[i]]);
   }
   printf("\n The table for solving knapsack problem using dynamic programming is:\n");
   for(i=0;i<=n;i++)
    {
     for(j=0;j<=m;j++)
      {
        printf("%d\t",v[i][j]);
      }
    printf("\n");
   }
 }
void main()
{
   double clk;
   clock_t starttime,endtime;
   int v[10][10],n,i,j,w[10],value[10],m,result;
   printf("Enter the number of items:\n");
   scanf("%d",&n);
   printf("Enter the weights of %d items:\n",n);
   for(i=1;i<=n;i++)
    {
    scanf("%d",&w[i]);
    }
   printf("Enter the value of %d items:\n",n);
   for(i=1;i<=n;i++)
   {
     scanf("%d",&value[i]);
   }

   printf("Enter the capacity of the knapsack:\n");
   scanf("%d",&m);
   for(i=0;i<=n;i++)
    {
    for(j=0;j<=m;j++)
     {
       v[i][j]=0;
     }
    }

   starttime=clock();
   result=knap(n,w,value,m,v);
   endtime=clock();
   clk=(double)(endtime-starttime)/CLOCKS_PER_SEC;
   printf("Solution for the knapsack problem is %d\n",v[n][m]);
   printf("%f\n",clk);
 }
