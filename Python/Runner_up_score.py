if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    mx = max(arr)
    list = []
    for i in arr:        
        if (i==mx):
            continue
        list.append(i)
    # print(arr)
    elem = max(list)
    print(elem)
