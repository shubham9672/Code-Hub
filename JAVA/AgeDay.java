/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ageday;
        
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.time.LocalDate;
import java.time.Period;
import java.util.Scanner;
/**
 *
 * @author JSVS
 */
public class AgeDay {
    
    public static void getAge(String input){
    LocalDate dob = LocalDate.parse(input);
    LocalDate curDate = LocalDate.now();
    Period period  =    Period.between(dob, curDate);
    System.out.print(period.getYears()+" years "+period.getMonths()+" and "+period.getDays()+" days\n");
   
    }
    
    public static void calculateBornDay(String s1) throws ParseException {
    SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
    SimpleDateFormat sdf1 = new SimpleDateFormat("EEEEE");
    Date d = sdf.parse(s1);
    String s = sdf1.format(d);
    System.out.println("The Born Day is on "+s.toUpperCase());
  }
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws ParseException {
        // TODO code application logic here
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your name: ");
        String name = scanner.nextLine();
        System.out.print("Please enter date of birth in YYYY-MM-DD: ");
        String input = scanner.nextLine();
        scanner.close();
        System.out.print("Hello ,"+name+".Your current Age is : ");
        getAge(input);
        calculateBornDay(input);
    }
    
}

