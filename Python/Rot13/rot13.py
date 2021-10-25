import sys

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def plus13(x):
    return alphabet[alphabet.index(x)+13]

def rot13encode(n):
    #n.strip()
    out = ''
    for i in n:
        temp = i
        if not temp.upper() in alphabet:
            out += i
        else:
            s = alphabet[(alphabet.index(i.upper())+13)%len(alphabet)]
            if i.isupper():
                out += s
            else:
                out += s.lower()
    #return "".join(list(map(lambda x:  alphabet[(alphabet.index(x.upper())+13)%len(alphabet)],list(n))))
    return out

def rot13decode(n):
    #n.strip()
    out = ''
    for i in n:
        temp = i
        if not temp.upper() in alphabet:
            out += i
        else:
            s = alphabet[(alphabet.index(i.upper())-13)%len(alphabet)]
            if i.isupper():
                out += s
            else:
                out += s.lower()
    #return "".join(list(map(lambda x:  alphabet[(alphabet.index(x.upper())+13)%len(alphabet)],list(n))))
    return out

if __name__ == "__main__":
    method = sys.argv[1]
    if method == "e":
        print(rot13encode(sys.argv[2]))
    elif method == "d":
        print(rot13decode(sys.argv[2]))
    else:
        print("python rot13.py [e|d] [string]")
    
