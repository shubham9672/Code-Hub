/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package lotterydrawing;
import java.util.Scanner;
/**
 *
 * @author JSVS
 */
public class LotteryDrawing {
    int k ,n;
    public void getInputs(){
        Scanner in = new Scanner(System.in);
        System.out.println("How many Numbers do you need to draw?");
        k = in.nextInt();
        System.out.println("What is the highest number you need to draw? ");
        n = in.nextInt();
        int []numbers = new int[n];
        int []result = new int[k];
        // creating object to access the classes
        inputData(numbers,result);
    }
    public  void inputData(int[]numbers,int[]result){
        for(int i = 0 ;i<numbers.length;i++){
            numbers[i]=i+1;
        }
        for(int i = 0 ;i<result.length;i++){
            int r = (int)(Math.random() * n);
            
            result[i] = numbers[r];
            numbers[r] = numbers[n-1];
            n--;
        }
       sortArray(result);
       System.out.println("Bet the following combinations .It'll wil make you rich!");
       for(int x : result){
           System.out.print(x+" ");
       }
       
    }
    public static int[]sortArray(int [] arr){
        for(int i = 0 ;i<arr.length;i++){
            for(int j=i+1;j<arr.length;j++){
               if(arr[i]>arr[j]){
                   int temp = arr[i];
                   arr[i]=arr[j];
                   arr[j]= temp;
               }
            }
        }
        return arr;
    }
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        //Creating objec for the class LotteryDrawing
        LotteryDrawing myobj = new LotteryDrawing();
        myobj.getInputs();
        
    }
    
}
