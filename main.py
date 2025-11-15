board = [
    ["","",""],
    ["","",""],
    ["","",""]
]

ai="0"
human="X"

def humanTurn():
    x=int(input("Give x-axis (0-2): "))
    y=int(input("Give y-axis (0-2):  "))
    if board[x][y]=="":
        board[x][y]=human
    else:
        print("Invalid input axes")
        humanTurn()
    


def findBestMove(board):
    bestScore= float('-inf')
    bestMove=None
    for i in range(3):
        for j in range(3):
            if board[i][j]=="":
                board[i][j]=ai
                score= minimax(board,0,False)
                board[i][j]=""
                if score>bestScore:
                    bestScore=score
                    bestMove=[i,j]
    board[bestMove[0]][bestMove[1]]=ai
   

scores= {"X":-1,
         "O":1,
         "Tie":0}

def minimax(board,depth,isMaximizing):

    result=checkWinner(board)
    if result!=None:
        if result == ai:
            return 1 
        elif result == human:
            return -1
        else:
            return 0
    if isMaximizing:
        bestScore=float("-inf")
        for i in range(3):
            for j in range(3):
                if board[i][j]=="":
                    board[i][j]=ai
                    score=minimax(board,depth+1,False)
                    board[i][j]=""
                    bestScore=max(bestScore,score)

        return bestScore
    else:
        bestScore=float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j]=="":
                    board[i][j]=human
                    score=minimax(board,depth+1,True)
                    board[i][j]=""
                    bestScore=min(bestScore,score)

        return bestScore

def checkWinner(b):
    # Rows
    for i in range(3):
        if b[i][0] == b[i][1] == b[i][2] != "":
            return b[i][0]

    # Columns
    for i in range(3):
        if b[0][i] == b[1][i] == b[2][i] != "":
            return b[0][i]

    # Diagonals
    if b[0][0] == b[1][1] == b[2][2] != "":
        return b[0][0]

    if b[0][2] == b[1][1] == b[2][0] != "":
        return b[1][1]

    # Check empty spots
    for i in range(3):
        for j in range(3):
            if b[i][j] == "":
                return None

    return "Tie"

    
if __name__=="__main__":
    
    while True:
        humanTurn()
        print("-------Board situation-------")
        print(board)
        winner =checkWinner(board)
        if winner!=None:
            print("----------------------------")
            print(f"Congratulations to {winner}. {winner} won.")
            break

        findBestMove(board)
        print("0 playes")
        print("-------Board situation-------")
        print(board)
        winner =checkWinner(board)
        if winner!=None:
            print("----------------------------")
            print(f"Congratulations to {winner}. {winner} won.")
            break