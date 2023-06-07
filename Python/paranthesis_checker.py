'''
Given an expression string x. Examine whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.
'''

def ispar(x):
    stack=[]
    for i in range(len(x)):
        if x[i]=='(' or x[i]=='{' or x[i]=='[':
            stack.append(x[i])
        else:
            if len(stack)==0:
                return False
            top=stack[-1]
            stack.pop()
            if not (x[i]==')' and top=='(' or x[i]=='}' and top=='{' or x[i]==']' and top=='['):
                return False
    if len(stack)==0:
        return True
    return False

s=str(input())
if(ispar(s)):
    print("Balanced")
else:
    print("Not balanced")
