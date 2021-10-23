/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pairs;
import java.util.*;
/**
 *
 * @author JSVS
 */
public class Pairs {
        public void diff(int[]arr,int n)
    { int di=0;int dif=0;
        int diff = Integer.MAX_VALUE;
         for (int i=0; i<n-1; i++)
            for (int j=i+1; j<n; j++)
                if ((arr[i] - arr[j])< diff){
                    diff = Math.abs((arr[i] - arr[j]));
                    di=arr[j];
                    dif = arr[i];
                }
         System.out.println("The minimum difference pairs are: "+di+ " "+dif);
    }
    public void diff(int[]A)
    { int n;int di=0; int dif=0;
       n=A.length;
       int diff = Integer.MIN_VALUE;
       for (int i = 0; i < n - 1; i++)
        {
            for (int j = i + 1; j < n; j++) {
                if ((A[i]-A[j]>diff)) {
                     diff = A[i]-A[j];
                  di=A[i];
                  dif=A[j];
                }
            }
        }
       
  System.out.println("The maximum difference pairs are: "+di+ " "+dif);
    }

  
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
              int a[],j;
         System.out.println("Enter the size of the array : ");
         Scanner in=new Scanner(System.in);
         j=in.nextInt();
         a = new int[j];
         System.out.println("Enter the values :");
         for(int i=0;i<j;i++)
         {
             int k;
             k=in.nextInt();
             a[i]=k;
         }
         Pairs ob=new Pairs();
         ob.diff(a,j);
        ob.diff(a);
     }
   
        // TODO code application logic here
    }
    

