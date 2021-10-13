#saurajit test python
import os
os.system('clear');
board=[' ' for x in range(10)]

def insertLetter(letter, pos):
    board[pos]=letter

def spaceIsFree(pos):
    return board[pos]==' '

def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def isWinner(bo,le):
    return (bo[7]==le and bo[8]==le and bo[9]==le) or (bo[4]==le and bo[5]==le and bo[6]==le) or (bo[1]==le and bo[2]==le and bo[3]==le) or (bo[1]==le and bo[4]==le and bo[7]==le) or (bo[2]==le and bo[5]==le and bo[8]==le) or (bo[3]==le and bo[6]==le and bo[9]==le) or (bo[1]==le and bo[5]==le and bo[9]==le) or (bo[3]==le and bo[5]==le and bo[7]==le)


def playerMove():
    run = True
    while run:
        move = input('Please select a position to place \'X\' (1-9): ')
        #if user don't give any valid move it will ask to enter value again and again
        try:
            move = int(move)#if move value not int then go to except
            if move > 0 and move < 10: #if move value lies between 1-9
                if spaceIsFree(move):
                    run= False
                    insertLetter('X',move)
                else:
                    print('Sorry, this space is occupied')
            else:
                print('Please insert a number within the range i.e (1-9)!!')
        except:
            print('please type a integer no. (1-9)')

def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0] #enumetare gives all the indices and the actual value of thing in our list 
    move = 0
    #we made a copy of our current board and check if we can make a move and thas a winning move or not
    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:] #due to '[:]' computer understands that we don't want a referance in boardcopy we want a copy of current board  
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move= selectRandom(cornersOpen)
        return move
    if 5 in possibleMoves:
        move=5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
    if len(edgesOpen) > 0:
        move= selectRandom(edgesOpen)
    
    return move

def selectRandom(li):  #remaining
    import random
    ln= len(li)
    r=random.randrange(0,ln)
    return li[r]

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True
def main():
    print('Welcome to tic tac toe')
    printBoard(board)
    while not(isBoardFull(board)):
        #for player
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('Sorry, O\'s won')
            break
        #for computer
        if not(isWinner(board, 'X')):
            move=compMove() #computer move done later
    
            if move == 0:
                print('Tie game')
            else:
                insertLetter('O', move)
                print('computer placed an \'O\'in position ', move , ':')
                import os
                os.system('clear')
                printBoard(board)
        else:
            print('X\'s won ')
            break
    if isBoardFull(board):
        print('Tie Game')

main()
while True:
    answer= input('Play again')
    if answer.lower() == 'y' or answer.lower() == 'yes':
        board = [' ' for x in range(10)]
        print('--------------------------')
        main()
    else:
        break
