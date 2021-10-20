import java.util.*;
public class Bear_and_Raspberry
{
    public static void main(String arg[])
    {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int price = sc.nextInt(), quality = sc.nextInt();
        for(int i = 0; i < n - 1; i++)
        {
            int p = sc.nextInt();
            int q = sc.nextInt();
            if(p < price || q > quality)
            {
                System.out.println("Poor Alex");
                System.exit(0);
            }
            price = p;
            quality = q;
        }
        System.out.println("Happy Alex");
        sc.close();
    }   
}