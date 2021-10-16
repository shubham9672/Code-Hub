def minion_game(text):
    s=0
    k=0
    count=1
    vowels = ["A","E","I","O","U"]
    for i in range(len(text)):
        if text[i] in vowels:
            k = k + (len(text)-i)
        else:
            s = s + (len(text)-i)
    if (k>s):
        print ("Kevin",k)
    elif (s>k):
        print ("Stuart",s)
    else:
        print("Draw")
s = input()
minion_game(s)
