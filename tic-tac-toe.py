table = [' ' for x in range(10)]

def insertLetter(letter, position):
    board[position] = letter

def printTable():
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

def spaceFree(position):
    return board[position] == ' '

def isWinners(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal)

def main():
    print('This is Tic Tac Toe presented to you by Python')
    printtable()

    while not(isBoardFull (board)):
        if not (isWinners(board, 'O')):
            playerMove()
            printTable()

        else:
            print('O\'s won this time!')
            break
        
    if isBoardFull(board):
        print('Tie Game')



def isBoardFull(board):
    pass

 