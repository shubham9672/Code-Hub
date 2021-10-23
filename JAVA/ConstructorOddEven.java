
package constructoroddeven;
import java.util.Scanner;

public class ConstructorOddEven {
    int number ;
   
    Scanner in = new Scanner(System.in);
    public ConstructorOddEven(){
        System.out.println("Enter any non-negative number ");
        number = in.nextInt();
        if(number<0){
            System.out.println("Negative numbers cannot be evaluated\nPlease,Try again!!");
            System.exit(0);
        }
      
        
  }
    public void checkData(){
        if(number%2==0){
            System.out.println("The Given Number "+number+" is Even");
        }else{
              System.out.println("The Given Number "+number+" is Odd"); 
        }
    }
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        //Creating an object
        String ch ;
        Scanner in = new Scanner(System.in);
        do{
        ConstructorOddEven myobj =  new ConstructorOddEven();
        myobj.checkData();
        System.out.println("Do you want to continue[y/n]: ");
        ch = in.nextLine();
   
        }while(ch.equalsIgnoreCase("Y"));
    
}
}
