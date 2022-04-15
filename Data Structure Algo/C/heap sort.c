#include<stdio.h>
int heap[100]={0},i,j,c,root,no,temp;
void createHeapArray();
void heapify();
int main()
{
    printf("Enter total no. of elements in the array: ");
    scanf("%d",&no);
    printf("Enter the array: ");
    for(i=0;i<no;++i)
        scanf("%d",&heap[i]);
    printf("\n");
    createHeapArray();// make the array max heap
    //Print before sort
    for(i=0;i<no;++i)
        printf("%d ",heap[i]); 
    printf("\n");   
    for(j=no-1;j>=0;--j)
    {
        temp=heap[0];
        heap[0]=heap[j];
        heap[j]=temp;
        heapify();
    }
    //Print after sort  
    for(i=0;i<no;++i)
        printf("%d ",heap[i]);
    printf("\n");
    return 0;
}
void createHeapArray()
{
  for(i=1;i<no;++i)
  {
      c=i;
      do{
        root=(c-1)/2;
            if(heap[root] < heap[c])
            {
                temp=heap[root];
                heap[root]=heap[c];
                heap[c]=temp;
            }
        c=root;
      }while(c!=0);
  }
}
void heapify()
{
    root=0;
    do
    {
        c=2*root+1;
        if(heap[c]<heap[c+1] && c<j-1)
            ++c;
        if(heap[root] < heap[c] && c<=j-1)
        {
            temp=heap[c];
            heap[c]=heap[root];
            heap[root]=temp;
        }
        root=c;
    }while(c<=j-1);    
}

