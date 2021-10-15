#include<stdio.h>  
int main() {
	int num = 889;
	int* p;
	p = &num; //storing the address of num variable    
	printf("Address of pointer variable p is %x \n", p);
	printf("Value of pointer variable p is %d \n", *p);
	return 0;
}