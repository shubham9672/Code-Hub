import random
from random import randint

//to generate random no.
num=[]
num1=[]
count=0
case=int(input(" 1. Give Data and Select Random Number from them \n 2. Generate Random numbers in range : \n"))
if case==1:
 n=int(input(" Enter total number of Data "))
 print("\n Enter Data: ")
 for i in range(0,n):
            ele=input()
            num.append(ele)
 n1=int(input(" Enter number of Random Data you want to generate : "))
 print("\n Random Data are : ")
 while(count<n1):
          random_num=random.choice(num)
          if (random_num not in num1):
              num1.append(random_num)
              print(random_num,end=' ')
              count+=1
elif (case==2):
 n=int(input(" Enter Number of numbers you want to generate "))
 n1=int(input(" Enter the First number (Smaller Number): "))
 n2=int(input(" Enter The last number (Bigger Number) : "))
 print("\n Random Numbers are : ")
 while(count<n):
          random_num=randint(n1,n2)
          if (random_num not in num1):
              num1.append(random_num)
              print(random_num,end=' ')
              count+=1
else:
      print(" Enter choice 1 or 2 ")
