import java.util.Scanner;
class Main {
    static final double PI = 3.14;
    static void calculateShape(double a, double b, double c) {
        double p = (a + b + c) / 2;
        System.out.println(Math.sqrt(p * (p - a) *(p - b) * (p - c)));

    }

    static void calculateShape(double a, double b) {
        System.out.println(a * b);
    }

    static void calculateShape(double r) {
        System.out.println(PI * r * r);
    }

    public static void main(String[] args) {
        // put your code here

        Scanner scn = new Scanner(System.in);
        String shape = scn.nextLine();
        switch (shape) {
            case ("triangle"):
                double a = scn.nextFloat();
                double b = scn.nextFloat();
                double c = scn.nextFloat();
                calculateShape(a, b, c);
                break;
            case ("rectangle"):
                double a1 = scn.nextFloat();
                double b1 = scn.nextFloat();
                calculateShape(a1, b1);
                break;
            case ("circle"):
                double r = scn.nextFloat();
                calculateShape(r);
                break;
            default:
                System.out.println("No such shape");
        }
    }
}


