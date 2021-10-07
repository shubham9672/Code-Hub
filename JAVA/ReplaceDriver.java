import java.util.Scanner;
public class ReplaceDriver{
   public static String replace(String str, char c1, char c2){
       if(str.length()<1){
           return str;
       }
       else{
           char first=c1==str.charAt(0)? c2 :str.charAt(0);
           return first+ replace(str.substring(1),c1,c2);
       
       }
   }
public static void main(String[] args)
{ Scanner r= new Scanner(System.in);
  String str= new String();
  System.out.println("Enter the string");
  str=r.nextLine();
  System.out.println("Enter the character to be replaced");
  char c1= r.next().charAt(0);
  System.out.println("Enter the character to be replaced with");
  char c2=r.next().charAt(0);
  System.out.print("The modified string is "+ replace(str,c1,c2));
}
}