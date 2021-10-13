def F_Sequence(num):
    first=1
    second=0
    last=0
    for i in range(num):
        last=first+second
        print(last,end=" ")
        first=second
        second=last
num=int(input("Enter number U want sequence : "))
F_Sequence(num)