Lefthand_player1 = 1
Lefthand_player2 = 1

Righthand_player1 = 1
Righthand_player2 = 1

print("Input1:Enter A for attack and S for split")
print("Input2:Enter attack combination LL or LR or RL or RR")


def error():
    print("\nInvalid input,Wait for your move.")


def status():
    print("Current Status:")
    print("Player1:", Lefthand_player1, Righthand_player1)
    print("Player2:", Lefthand_player2, Righthand_player2)


count = 1
while count > 0:
    first_move = input("player 1's move: ").upper()
    if first_move == "A":
        combination_a = input("Enter the combination: ")
        combination_1 = combination_a.upper()
        if combination_1 == "LR":
            Righthand_player2 = Righthand_player2 + Lefthand_player1
            if Righthand_player2 >= 5:
                Righthand_player2 = 0
        elif combination_1 == "RL":
            Lefthand_player2 = Lefthand_player2 + Righthand_player1
            if Lefthand_player2 >= 5:
                Lefthand_player2 = 0
        elif combination_1 == "LL":
            Lefthand_player2 = Lefthand_player2 + Lefthand_player1
            if Lefthand_player2 >= 5:
                Lefthand_player2 = 0
        elif combination_1 == "RR":
            Righthand_player2 = Righthand_player2 + Righthand_player1
            if Righthand_player2 >= 5:
                Righthand_player2 = 0
        else:
            error()
    elif first_move == "S":
        z, a, b = input("Enter your combination:").split()
        a = int(a)
        b = int(b)
        Lefthand_player1 = a
        Righthand_player1 = b
    else:
        error()
    status()
    if (Lefthand_player1 == 0 and Righthand_player1 == 0) or (
        Lefthand_player2 == 0 and Righthand_player2 == 0
    ):
        count = 0
        if Lefthand_player1 == 0 and Righthand_player1 == 0:
            print("Player2 has won!")
        else:
            print("Player1 has won!")
        break

    second_move = input("player 2's move: ").upper()
    if second_move == "A":
        combination_b = input("Enter the combination: ")
        combination_2 = combination_b.upper()
        if combination_2 == "LR":
            Righthand_player1 = Righthand_player1 + Lefthand_player2
            if Righthand_player1 >= 5:
                Righthand_player1 = 0
        elif combination_2 == "RL":
            Lefthand_player1 = Lefthand_player1 + Righthand_player2
            if Lefthand_player1 >= 5:
                Lefthand_player1 = 0
        elif combination_2 == "LL":
            Lefthand_player1 = Lefthand_player1 + Lefthand_player2
            if Lefthand_player1 >= 5:
                Lefthand_player1 = 0
        elif combination_2 == "RR":
            Righthand_player1 = Righthand_player1 + Righthand_player2
            if Righthand_player1 >= 5:
                Righthand_player1 = 0
        else:
            error()
    elif second_move == "S":
        z, a, b = input("Enter your combination:").split()
        a = int(a)
        b = int(b)
        Lefthand_player2 = a
        Righthand_player2 = b
    else:
        error()
    status()
    if (Lefthand_player1 == 0 and Righthand_player1 == 0) or (
        Lefthand_player2 == 0 and Righthand_player2 == 0
    ):
        count = 0
        if Lefthand_player1 == 0 and Righthand_player1 == 0:
            print("Player2 has won!")
        else:
            print("Player1 has won!")
