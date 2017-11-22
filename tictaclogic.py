import random
def decide_turn():
    if random.randint(0,1) ==0:
        return 'computer'
    else:
        return 'player'

def drawboard(board):
    print (" " + board[7]+ "|" + board[8] + "|" + board[9] + " ")
    print("----------")
    print(" " + board[4] + "|" + board[5] + "|" + board[6] + " ")
    print("----------")
    print(" " + board[1] + "|" + board[2] + "|" + board[3] + " ")
    print("----------")

def getuserposition(board):
    pos=' '
    print("Enter the position you want to move(1-9)")
    pos = int(input())
    while pos not in '1 2 3 4 5 6 7 8 9'.split() and not isspace(board,int(pos)):
        print("Enter the position you want to move(1-9)")
        pos = int(input())
    return pos

def move(board,pos,symbol):
    board[pos]=symbol


def iswinner(board,symbol):
    return ((board[1]==symbol and  board[2]==symbol and board[3]==symbol )or
    (board[4]==symbol and board[5]==symbol and board[6]==symbol) or
    (board[7]==symbol and  board[8]==symbol and board[9]==symbol)  or
    (board[1]==symbol and board[5]==symbol and board[9]==symbol ) or
    (board[5]==symbol and board[3]==symbol and board[7]==symbol ) or
    (board[1]==symbol and board[4]==symbol and board[7]==symbol ) or
    (board[2]==symbol and board[5]==symbol and board[8]==symbol ) or
    (board[3]==symbol and board[6]==symbol and board[9]==symbol ) )

def boardfull(board):
    for i in range(1,10):
        if  isspace(board,i):
            return False
    return True

def isspace(board,pos1):
    return board[pos1]==' '

def boardcopy(board):
    roughboard=[]
    for i in board:
        roughboard.append(i)
    #print("debugging")
    drawboard(roughboard)
    #print("debugging")
    return roughboard

def getcompposition(board,comps):
    if comps=='X':
        users='O'
    else:
        users='X:'
    boardcopy1=boardcopy(board)
    boardcopy2 = boardcopy(board)
    #print("this is used to test the value of boardcopy")
    #drawboard(boardcopy1)
    #print("Ending")
    for i in range(1,10):
        if isspace(boardcopy1,i):
            move(boardcopy1,i,comps)
            #print("this is used to test the value of boardcopy")
            #drawboard(boardcopy1)
            #print("sample")
            if iswinner(boardcopy1,comps):
                return i

    for i in range(1,10):
        if isspace(boardcopy2,i):
            move(boardcopy2,i,users)
            print("this is used to test the value of boardcopy")
            drawboard(boardcopy2)
            print("Ending")
            if iswinner(boardcopy2,users):

                return i


    pos2=recommendations(board,[1,3,7,9])
    if pos2!=None:
            return pos2
    if isspace(board,5):
            return 5
    else:
            return recommendations(board,[2,4,6,8])

def recommendations(board,list1):
    recom=[]
    for i in list1:
        if isspace(board,i):
            recom.append(i)

    if len(recom)!=0:
        return random.choice(recom)
    else:
         return None

def playagain():
    print("press yes to play again")
    return input().lower().startswith("yes")



while True:
    board=[' ']*10
    print ("Welcome to tic tac toe game")
    print("Enter your choice on X or O")
    userchoice=input()
    while(userchoice.upper()=='X' or 'O'):
        if(userchoice.upper()=='X'):
            users='X'
            comps='O'
            break
        elif(userchoice.upper()=='O'):
            users='O'
            comps='X'
            break

    print ("User choice is: %s \n Computer choice is: %s " %(users,comps))
    print ("lets decide who's going to play first")
    turn=decide_turn()
    print("The" + turn + "is going to play first")
    startedplaying=True
    while startedplaying:
        if turn.lower()=='player':
            pos=getuserposition(board)
            move(board,pos,users)
            drawboard(board)
            if(iswinner(board,users)):
                print("You won")
                drawboard(board)
                startedplaying=False
            else:
                if(boardfull(board)):
                    print("Game is tie")
                    drawboard(board)
                    startedplaying=False
                else:
                    turn='computer'
        else:
            print("Computer's move")
            pos_comp=getcompposition(board,comps)
            move(board,pos_comp,comps)
            drawboard(board)
            if (iswinner(board,comps)):
                print("Computer won!!!, better luck next time")
                drawboard(board)
                startedplaying=False
            else:
                if (boardfull(board)):
                    print("Game is tie")
                    drawboard(board)
                    startedplaying = False
                else:
                    turn='player'

    if not playagain():
             break

