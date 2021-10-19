num = int(input("Enter a number: "));
if(num<0):
    print('The number must be positive')
else: 
    total = 0;
    while num!=0:
        total += num%10;
        num = num//10;
    print("The sum of the digits is: ", total);