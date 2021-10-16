import CurrentStatus
import Attack
import DeadHand
import GameDecision

if __name__ == "__main__":
    p1L , p1R, p2L, p2R = 1, 1, 1, 1

    CurrentStatus.printPlayersCurrentStatus(p1L, p1R, p2L, p2R)

    gameOver = 0

    while(gameOver == 0):
        print("Enter Move For Player 1 :: ")
        move = input()
        if(move == 'A'):
            print("Enter The Move Combination :: ")
            move1, move2 = input().split()
            if(move1 == 'L'):
                if(move2 == 'R'):
                    p2R = Attack.AttackOnOpposition(p1L, p2R)
                    p2R = DeadHand.CheckDeadHand(p2R)
                elif(move2 == 'L'):
                    p2L = Attack.AttackOnOpposition(p1L, p2L)
                    p2L = DeadHand.CheckDeadHand(p2L)
                else:
                    print("INVALID MOVE !!! WAIT FOR YOUR NEXT TURN !!!")
            elif(move1 == 'R'):
                if(move2 == 'L'):
                    p2L = Attack.AttackOnOpposition(p1R, p2L)
                    p2L = DeadHand.CheckDeadHand(p2L)
                elif(move2 == 'R'):
                    p2R = Attack.AttackOnOpposition(p1R, p2R)
                    p2R = DeadHand.CheckDeadHand(p2R)
                else:
                    print("INVALID COMBINATION !!! WAIT FOR YOUR NEXT TURN !!!")
            else:
                print("INVALID COMBINATION !!! WAIT FOR YOUR NEXT TURN !!!")
        elif(move == 'S'):
            print("Enter The Move Combination:: ")
            move, split1, split2 = input().split()
            left = int(split1)
            right = int(split2)

            left = DeadHand.CheckDeadHand(left)
            right = DeadHand.CheckDeadHand(right)

            if (left + right) <= (p1L + p1R):
                if(left + right) == (p1L + p1R):
                    p1L = left
                    p1R = right
                else:
                    if(move == 'L'):
                        p1L = left
                        p1R = p1R + right
                        p1R = DeadHand.CheckDeadHand(p1R)
                    elif(move == 'R'):
                        p1R = right
                        p1L = p1L + left
                        p1L = DeadHand.CheckDeadHand(p1L)
                    else:
                        print("INVALID NUMBER OF SPLIT COMBINATION !!! WAIT FOR YOUR NEXT TURN !!!")
            else:
                print("INVALID NUMBER OF SPLIT COMBINATIONS !!! WAIT FOR YOUR NEXT TURN / MOVE !!!")
        else:
            print("INVALID MOVE !!! WAIT FOR YOUR NEXT TURN !!!")

        CurrentStatus.printPlayersCurrentStatus(p1L, p1R, p2L, p2R)

        gameOver = GameDecision.checkGameOver(p2L, p2R)
        if gameOver:
            winner = 'Player 1'
            break


        print("Enter Move For Player 2 :: ")
        move = input()
        if (move == 'A'):
            print("Enter The Move Combination :: ")
            move1, move2 = input().split()
            if(move1 == 'L'):
                if (move2 == 'R'):
                    p1R = Attack.AttackOnOpposition(p2L, p1R)
                    p1R = DeadHand.CheckDeadHand(p1R)
                elif (move2 == 'L'):
                    p1L = Attack.AttackOnOpposition(p2L, p1L)
                    p1L = DeadHand.CheckDeadHand(p1L)
                else:
                    print("INVALID MOVE !!! WAIT FOR YOUR NEXT TURN !!!")
            elif (move1 == 'R'):
                if (move2 == 'L'):
                    p1L = Attack.AttackOnOpposition(p2R, p1L)
                    p1L = DeadHand.CheckDeadHand(p1L)
                elif (move2 == 'R'):
                    p1R = Attack.AttackOnOpposition(p2R, p1R)
                    p1R = DeadHand.CheckDeadHand(p1R)
                else:
                    print("INVALID COMBINATION !!! WAIT FOR YOUR NEXT TURN !!!")
            else:
                print("INVALID COMBINATION !!! WAIT FOR YOUR NEXT TURN !!!")
        elif (move == 'S'):
            print("Enter The Move Combination:: ")
            move, split1, split2 = input().split()
            left = int(split1)
            right = int(split2)

            left = DeadHand.CheckDeadHand(left)
            right = DeadHand.CheckDeadHand(right)

            if (left + right) <= (p2L + p2R):
                if (left + right) == (p2L + p2R):
                    p2L = left
                    p2R = right
                else:
                    if (move == 'L'):
                        p2L = left
                        p2R = p2R + right
                        p2R = DeadHand.CheckDeadHand(p2R)
                    elif (move == 'R'):
                        p2R = right
                        p2L = p2L + left
                        p2L = DeadHand.CheckDeadHand(p2L)
                    else:
                        print("INVALID NUMBER OF SPLIT COMBINATION !!! WAIT FOR YOUR NEXT TURN !!!")
            else:
                print("INVALID NUMBER OF SPLIT COMBINATIONS !!! WAIT FOR YOUR NEXT TURN / MOVE !!!")
        else:
            print("INVALID MOVE !!! WAIT FOR YOUR NEXT TURN !!!")

        CurrentStatus.printPlayersCurrentStatus(p1L, p1R, p2L, p2R)

        gameOver = GameDecision.checkGameOver(p1L, p1R)
        if(gameOver == 1):
            winner = 'Player 2'

    print("  ")
    print("WINNER OF GAME IS:: " + winner)