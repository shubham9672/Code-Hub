import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        Scanner scn=new Scanner(System.in);
        int n=scn.nextInt();
        int[][] a=new int[n][n];
        printNQueens(a,"",0,0);
    }

    public static void printNQueens(int[][] chess, String qsf, int row) {
        if(row==chess.length){
            // if(nq==chess.length){
                System.out.println(qsf+".");
            // }
            return;
        }
        for(int col=0;col<chess[row].length;col++){
            boolean b=safe(chess,row,col);
            // System.out.println(row+" "+col+" "+b);
            if(b){
                chess[row][col]=1;
                printNQueens(chess,qsf+row+"-"+col+", ",row+1);
                chess[row][col]=0;
            }
            
        }
    }
    
    public static boolean safe(int[][] chess,int r,int c){
        if(chess[r][c]==1){
            return false;
        }
        for(int i=0;i<chess.length;i++){
            if(chess[i][c]==1){
                return false;
            }
        }
        
        // for(int j=0;j<chess[0].length;j++){
        //     if(chess[r][j]==1){
        //         return false;
        //     }
        // }
        
        // int d1=r+c;
        int i=r;
        int j=c;
        while(i>0 && j<chess[0].length-1){
            i--;
            j++;
            if(chess[i][j]==1){
                return false;
            }
        }
        i=r;
        j=c;
        while(i<chess.length-1 && j>0){
            i++;
            j--;
            if(chess[i][j]==1){
                return false;
            }
        }
        
        // int d2=r-c;
        i=r;
        j=c;
        while(i>0 && j>0){
            i--;
            j--;
            if(chess[i][j]==1){
                return false;
            }
        }
        i=r;
        j=c;
        while(i<chess.length-1 && j<chess[0].length-1){
            i++;
            j++;
            if(chess[i][j]==1){
                return false;
            }
        }
        return true;
    }
}