import java.util.Scanner;

public class MatrixMultiplication {

    static void enterMatrices(int a[][], int b[][], int r1, int c1, int r2, int c2) {
        Scanner scan_mat = new Scanner(System.in);
        
        System.out.print("\nEnter elements of matrix A:\n");    
        for (int i = 0; i < r1; ++i) 
            for (int j = 0; j < c1; ++j) 
                a[i][j] = scan_mat.nextInt();

        System.out.print("\nEnter elements of matrix B:\n");    
        for (int i = 0; i < r2; ++i) 
            for (int j = 0; j < c2; ++j) 
                b[i][j] = scan_mat.nextInt();
        
        scan_mat.close();
    }

    static void multiplyMatrices(int a[][], int b[][], int c[][], int r1, int c1, int r2, int c2) {
        for (int i = 0; i < r1; ++i) 
            for (int j = 0; j < c2; ++j) 
                c[i][j] = 0;

        for (int i = 0; i < r1; ++i) 
            for (int j = 0; j < c2; ++j) 
                for (int k = 0; k < c1; ++k) 
                    c[i][j] += a[i][k] * b[k][j];
    }
    
    static void printMatrix(int c[][], int r1, int c2) {
    
        System.out.println("\nOutput Matrix:");
        for (int i = 0; i < r1; ++i) 
            for (int j = 0; j < c2; ++j) {
                System.out.print(c[i][j] + "\t");
                if (j == c2 - 1)
                    System.out.print("\n");
            }
    }
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter the no: of rows and columns for matrix A: ");
        int r1 = scan.nextInt(), c1 = scan.nextInt();
        System.out.print("Enter the no: of rows and columns for matrix B: ");
        int r2 = scan.nextInt(), c2 = scan.nextInt();

        while (c1 != r2){
            System.out.println("Invalid matrix size! Enter rows and columns.");
            System.out.print("Enter rows and columns for matrix A: ");
            r1 = scan.nextInt();
            c1 = scan.nextInt();
            System.out.print("Enter rows and columns for matrix B: ");
            r2 = scan.nextInt();
            c2 = scan.nextInt();
        }

        int a[][] = new int[10][10];
        int b[][] = new int[10][10];
        int c[][] = new int[10][10];
        
        enterMatrices(a, b, r1, c1, r2, c2);
        multiplyMatrices(a, b, c, r1, c1, r2, c2);
        printMatrix(c, r1, c2); 
        scan.close();
    }
}
