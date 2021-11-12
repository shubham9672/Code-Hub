a=[4,3,1,2]
NumberOfSwaps=0
for i in range(len(a)):
    for j in range(i+1,len(a),1):
        if(a[i]>a[j]):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
            NumberOfSwaps+=1
print(a)
print("Array is sorted in",NumberOfSwaps,"swaps")
print("First Element:",a[0])
print("Last Element:",a[len(a)-1])