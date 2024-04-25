#TicTacToe Games
#Single & Multiplayer

#List to check who Won the game.
board = [' ' for x in range(10)]

#Print the game board
def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

#Check if there is a winner or not    
def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or(bo[1] == le and bo[2] == le and bo[3] == le) or(bo[1] == le and bo[4] == le and bo[7] == le) or(bo[2] == le and bo[5] == le and bo[8] == le) or(bo[3] == le and bo[6] == le and bo[9] == le) or(bo[1] == le and bo[5] == le and bo[9] == le) or(bo[3] == le and bo[5] == le and bo[7] == le)

#Insert 'X' or 'O'
def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

#Insert my move with Friend and Computer
def yourMove():
    run = True
    while run:
        move = input('Your move: Place \'X\' in position (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')
            
#Computer moves
def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
            
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
            
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        
    return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]
    
#Check if the board is full or not
def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

#Main function when play with Computer
def computer():
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            yourMove()
            printBoard(board)
        else:
            print("Sorry, Computer wins! :(")
            break

        if not(isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print("It's a tie!")
            else:
                insertLetter('O', move)
                print("Computer placed 'O' in position: ", move)
                printBoard(board)
        else:
            print("Hurray! You Won! :D")
            break

#To insert Friend's move
def friendMove():
    run = True
    while run:
        move = input('Friend\'s move: Place \'O\' in position (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('O', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')

#Main function when play with Friend
def friend():
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            yourMove()
            printBoard(board)
        else:
            print("Sorry, Friend wins! :(")
            break
        if isBoardFull(board):
            print("It's a tie!")
            break

        if not(isWinner(board, 'X')):
            friendMove()
            printBoard(board)
        else:
            print("Hurray! You Won! :D")
            break
        if isBoardFull(board):
            print("It's a tie!")
            break

#Main Function where the game starts
while True:
    answer = input('Do you want to play again? (Y/N): ')
    if answer.upper() == 'Y' or answer.upper() == 'YES':
        print('-----------------------------------')
        board = [' ' for x in range(10)]
        ask = input("Who do you want to play with? Computer or Friend! (C/F): ")
        print('-----------------------------------')
        if ask.upper() == 'C':
            print("Welcome to play with Computer!")
            computer()
        else:
            print("Welcome to play with your Friend!")
            friend()
    else:
        break
