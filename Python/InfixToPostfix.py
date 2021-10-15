# infix to postfix

n = int(input())
s = input()
l1 = ["(", ")", "+", "-", "*", "/", "^"]
temp = []
result = ""
for i in range(n):
    if s[i] in l1:
        if temp:
            if s[i] == "(":
                temp.append(s[i])
            elif s[i] == "^":
                if temp[-1] in ["(", "+", "-", "*", "/"]:
                    temp.append(s[i])
                else:
                    result += s[i]
            elif s[i] == "/" or s[i] == "*":
                if temp[-1] in ["(", "+", "-"]:
                    temp.append(s[i])
                else:
                    while temp and temp[-1] in ["^", "*", "/"]:
                        result += temp[-1]
                        temp.pop()
                    temp.append(s[i])
            elif s[i] in ["+", "-"]:
                if temp[-1] == "(":
                    temp.append(s[i])
                else:
                    while temp and temp[-1] in ["^", "+", "-", "*", "/"]:
                        result += temp[-1]
                        temp.pop()
                    temp.append(s[i])
            else:
                while temp[-1] != "(":
                    result += temp[-1]
                    temp.pop()
                temp.pop()
        else:
            temp.append(s[i])
    else:
        result += s[i]
while temp:
    result += temp[-1]
    temp.pop()
print(result)
