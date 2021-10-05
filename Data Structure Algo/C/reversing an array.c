#include <stdio.h>
#include <stdlib.h>

int main ()
{
	int a[5];
	int i,n,temp;
	printf("enter no of elements needed\n");
	scanf("%d",&n);
		
	printf("enter elements\n");
	for (i=0;i<n;i++)
	{
		scanf("%d\n",&a[i]);
	}
	
	for(i=0;i<n/2;i++)
	{
		temp=a[i];
		a[i]=a[n-1-i];
		a[n-1-i] = temp;
	
	}
	printf("reversed array\n");
	for(i=0;i<n;i++)
	{
		printf("%d\n",a[i]);
	}

	return 0;
}
//output
enter no of elements needed
5
enter elements
1
2
3
4
5
6
reversed array
5
4
3
2
1
