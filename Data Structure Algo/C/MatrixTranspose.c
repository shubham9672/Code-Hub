//To find out transpose of a matrix.


#include<stdio.h>
#include<stdlib.h>
int main()
{
    int a[10][10], m,n,i,j,b[10][10];

    printf("enter values for m and n:");
    scanf("\t%d\t%d",&m,&n);

    printf("\nEnter matrix elements\n");
    for(i=0;i<m;i++)
    {
        for(j=0;j<n;j++)
        {
            scanf("\t%d",&a[i][j]);
        }
    }

     for(i=0;i<m;i++)
    {
        for(j=0;j<n;j++)
        {
            b[j][i]=a[i][j];
        }
    }

    printf("transpose of matrix is:\n");
     for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
           printf("\t%d",b[i][j]);
        }
          printf("\n");
    }

    return 0;
}

