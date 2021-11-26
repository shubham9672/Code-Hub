/**

Name = Gurjot Singh 

***/
#include <stdio.h>

int main()
{
    int r, n, rnum=0, temp;
    printf("enter a number \n");
    scanf("%d", &n);
    temp = n;
    while(n!=0)
    {
        r= n%10;
        rnum = rnum*10+r;
        n=n/10;
    }
    if (temp==rnum){
        printf("Its a palindrome");
    }
    else 
    printf("its not a palindrome");

    return 0;
}

