import java.io.*;
public class PrimeFactorization{

    public static void primeFactors(int num){
        int number=num;
        if(number<=1)
            return;
        for(int counter=2;(counter*counter)<=number;counter++){
            while(number%counter==0){
                System.out.print(counter+" ");
                number=number/counter;
            }
        }
        if(number>0){
            System.out.print(number+" ");
        }
    }

    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter an integer: ");
        int n = Integer.parseInt(br.readLine());
        System.out.print("The Prime Factors of "+n+" are: ");
        primeFactors(n);
    }
}
