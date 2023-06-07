#include<iostream>
using namespace std;
int main()
{
	char A[100];
	char B[100];
	gets(A);
	gets(B);
	int i,H[26]={0};
	
	for(i=0;A[i]!='\0';i++)
	 H[A[i]-97]+=1;
	 
	 for(i=0;B[i]!='\0';i++)
	 {
	  H[A[i]-97]-=1;
	  
	  if(H[A[i]-97]<0)
	  {
	   cout<<"Not an Anagram";
	    break;
       }
     }
       
       if(B[i]==0)
        cout<<"It is Anagram";
       return 0;
}
