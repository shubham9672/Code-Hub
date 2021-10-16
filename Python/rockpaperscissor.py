import random

l = ["Stone", "Paper", "Scissors"]
opponent = random.choice(l)
a = "s"
b = "p"
c = "sc"
flag = True

while(flag):
    flag = False
    d = input("Please enter a key which you want to choose (stone(s) paper(p) scissors(sc)) : ")
    if d==a and opponent=="Paper":
        print("You chose stone opponent chose paper hence You LOSE")
    elif d==a and opponent=="Scissors":
        print("You chose stone opponent chose scissors hence You WIN")
    elif d==a and opponent=="Stone":
        print("You both choose the same , its tie :)")
    elif d==b and opponent=="Stone":
        print("You chose paper opponent chose stone hence You WIN")
    elif d==b and opponent=="Paper":
        print("You both choose the same , its tie :)")
    elif d==b and opponent=="Scissors":
        print("You chose paper opponent chose scissors hence You LOSE")
    elif d==c and opponent=="Scissors":
        print("You both choose the same , its tie :)")
    elif d==c and opponent=="Paper":
        print("You chose scissors opponent chose paper hence You WIN")
    elif d==c and opponent=="Stone":
        print("You chose scissors opponent chose stone hence You LOSE")
    else:
        print("INVALID! Please enter 's', 'p' or 'sc' only!\n")
        flag = True

print("\nThank you for playing this game!")
print("Have you enjoyed? then share it to your friend :)")
