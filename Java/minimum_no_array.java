import java.io.*;

class proko{
    

    public static void main(String args[]){
        int arr[]= {10,20,30,0,50,60};
        int l= arr.length;
        int min=arr[0];

        for(int i=0;i<l;i++){
            if(arr[i]<min){
                min=arr[i];
            }
            
            
        }
        System.out.println(min);
   }
}
