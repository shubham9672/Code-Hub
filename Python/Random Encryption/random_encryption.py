import random as rn

def ard_map(x, f_min, f_max, t_min, t_max) -> int:
    return ( (t_max-t_min) * (x-f_min) / (f_max-f_min)) + t_min

def customBitGenerator(length)->int:
    out = []
    for i in range(length):
        out.append(round(rn.random()))
    return out

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

inp = input("Write your plain text:   ")
rn.seed(version=2)
rand_bits = customBitGenerator(len(inp))
out = []


#Password Encryptor#
try:
    j=0
    for i in rand_bits:
        temp = round(((((int(i)+rn.random()+alphabet.index(inp[j].upper())) + rn.randint(0,100)) + rn.random()) * rn.uniform(rn.randint(50,201), rn.randint(2, 50)   )  )  )
        out.append(alphabet[temp%len(alphabet)])
        j+=1
    print(rand_bits)
    rn.shuffle(out)
    print("".join(out))
except Exception as e:
    print(e)



#Token Generator#
'''for i in rand_bits:
    for j in inp:
        temp = round(((((int(i)+rn.random()+alphabet.index(j.upper())) + rn.randint(0,100)) + rn.random()) * rn.uniform(rn.randint(50,201), rn.randint(2, 50)   )  )  )
       out+=alphabet[temp%len(alphabet)]'''


