//Java implementation of Binary search
//Time complexity O(log n)
import java.util.*;
public class binary_search
{
    public static void main(String args[]){
        Scanner in = new Scanner(System.in);
        int a[]=new int[10];
        int i,n,c=0,lb=0,ub=9;
        System.out.println("Enter 10 numbers");
        for(i=0;i<10;i++)
        {
            a[i]=in.nextInt();
        }
        System.out.println("Enter search element");
        n=in.nextInt();
        while(lb<=ub)
        {
            int p=(lb+ub)/2;
            if(a[p]<n)
            lb=p+1;
            if (a[p]>n)
            ub=p-1;
            if(a[p]==n)
            {
                c=1;
                break;
            }
        }
        if(c==1)
        System.out.println("Element found");
        else
        System.out.println("Element not found");
    }
}