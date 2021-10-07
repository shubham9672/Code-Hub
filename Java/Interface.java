import java.io.*;
interface Car
{
    void topSpeed();
    void noOfGear();
    void serviceTime();
}
class Alto implements Car
{
    Alto()
    {
        System.out.println("This is a Alto Car");
        topSpeed();
        noOfGear();
        serviceTime();
    }
    public void topSpeed()
    {
        System.out.println("Top Speed is 100km/h");
    }
    public void noOfGear()
    {
        System.out.println("No. of gears is 5");
    }
    public void serviceTime()
    {
        System.out.println("This car needs service after each 10000 km");
    }
}
class Swift implements Car
{
    Swift()
    {
        System.out.println("This is a Swift Car");
        topSpeed();
        noOfGear();
        serviceTime();
    }
    public void topSpeed()
    {
        System.out.println("Top Speed is 180km/h");
    }
    public void noOfGear()
    {
        System.out.println("No. of gears is 6");
    }
    public void serviceTime()
    {
        System.out.println("This car needs service after each 75000 km");
    }
}
class Baleno implements Car
{
    Baleno()
    {
        System.out.println("This is a Baleno Car");
        topSpeed();
        noOfGear();
        serviceTime();
    }
    public void topSpeed()
    {
        System.out.println("Top Speed is 200km/h");
    }
    public void noOfGear()
    {
        System.out.println("No. of gears is 5");
    }
    public void serviceTime()
    {
        System.out.println("This car needs service after each 7500 km");
    }
}
public class Interface
{
    public static void main(String args[])
    {
        System.out.println("This program illustrate implementation of interface");
        Alto obj1=new Alto();
        Swift obj2=new Swift();
        Baleno obj3=new Baleno();
    }
}