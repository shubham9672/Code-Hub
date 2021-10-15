package Practise;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Random;
import java.util.StringTokenizer;

public class insertion_sort {
	public  static void main(String args[]) {
		FastScanner fs=new FastScanner();
		System.out.println("Enter the size of Array");
		int n=fs.nextInt();
		int []arr=new int[n];
		Random r=new Random();
		for(int i=0;i<n;i++)
			arr[i]=r.nextInt(100);
		System.out.println("Array before Sorting");
		Print(arr);
		InsertionSort(arr);
		System.out.println("Array after Sorting");
		Print(arr);
	}
	public static void Print(int []arr) {
		for(int val:arr)
			System.out.print(val+" ");
		System.out.println();
		return ;
	}
	public static int[] InsertionSort(int []arr) {
		for(int i=1;i<arr.length;i++){
			int val=arr[i];
			int j=i-1;
			while(j>=0&&arr[j]>val) {
				arr[j+1]=arr[j];
				j--;
			}
			arr[j+1]=val;
		}
		return arr;
	}
	static final Random random=new Random();	
	static void ruffleSort(int[] a) {
		int n=a.length;
		for (int i=0; i<n; i++) {
			int oi=random.nextInt(n), temp=a[oi];
			a[oi]=a[i]; a[i]=temp;
		}
		Arrays.sort(a);
	}

	
	static class FastScanner {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st=new StringTokenizer("");
		String next() {
			while (!st.hasMoreTokens())
				try {
					st=new StringTokenizer(br.readLine());
				} catch (IOException e) {
					e.printStackTrace();
				}
			return st.nextToken();
		}
		
		int nextInt() {
			return Integer.parseInt(next());
		}
		int[] readArray(int n) {
			int[] a=new int[n];
			for (int i=0; i<n; i++) a[i]=nextInt();
			return a;
		}
		long nextLong() {
			return Long.parseLong(next());
		}
	}
}
