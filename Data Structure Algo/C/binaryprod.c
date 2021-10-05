// C Program to Find Multiplication of two Binary Numbers
#include <stdio.h>
#include <conio.h>

int binaryproduct(int, int);

int main()
{
	long binary1, binary2, multiply = 0;
	int digit, factor = 1;
	//clrscr();

	printf("Enter the first binary number: ");
	scanf("%ld", &binary1);
	printf("Enter the second binary number: ");
	scanf("%ld", &binary2);

	while (binary2 != 0)
	{
		digit =  binary2 % 10;
		if (digit == 1)
		{
			binary1 = binary1 * factor;
			multiply = binaryproduct(binary1, multiply);
		}
		else
		{
			binary1 = binary1 * factor;
		}
		binary2 = binary2 / 10;
		factor = 10;
	}
	printf("Product of two binary numbers: %ld", multiply);
	getch();
	return 0;
}

int binaryproduct(int binary1, int binary2)
{
	int i = 0, remainder = 0, sum[20];
	int binaryprod = 0;

	while (binary1 != 0 || binary2 != 0)
	{
		sum[i++] =(binary1 % 10 + binary2 % 10 + remainder) % 2;
		remainder =(binary1 % 10 + binary2 % 10 + remainder) / 2;
		binary1 = binary1 / 10;
		binary2 = binary2 / 10;
	}
	if (remainder != 0)
	{
		sum[i++] = remainder;
	}
	--i;
	while (i >= 0)
	{
		binaryprod = binaryprod * 10 + sum[i--];
	}
	return binaryprod;
}
