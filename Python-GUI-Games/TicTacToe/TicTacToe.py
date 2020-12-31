from tkinter import *

# Global Variables
from tkinter.messagebox import showinfo

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-", ]

game_not_end = True
winner = None
curPlayer = "X"
lastIndex = -1


def computerPlay():
    global board
    i = 0
    bestScore = float('-inf')
    bestMove = -1
    while i < 9:
        if board[i] != 'X' and board[i] != 'O':
            board[i] = 'O'
            score = minimax(i, 0, 'X')
            board[i] = '-'
            if score > bestScore:
                bestScore = score
                bestMove = i
        i += 1

    board[bestMove] = 'O'
    return bestMove


def minimax(loc, depth, player):
    global board

    if check_end():
        player = get_winner()
        if player == 'X':
            return -1
        else:
            if player == 'O':
                return 1
            else:
                return 0

    if player == 'X':
        i = 0
        bestScore = float('inf')
        bestMove = -1
        while i < 9:
            if board[i] != 'X' and board[i] != 'O':
                board[i] = 'X'
                score = minimax(i, depth + 1, 'O')
                board[i] = '-'
                if score < bestScore:
                    bestScore = score
                    bestMove = i
            i += 1
        return bestScore
    else:
        i = 0
        bestScore = float('-inf')
        bestMove = -1
        while i < 9:
            if board[i] != 'X' and board[i] != 'O':
                board[i] = 'O'
                score = minimax(i, depth + 1, 'X')
                board[i] = '-'
                if score > bestScore:
                    bestScore = score
                    bestMove = i
            i += 1
        return bestScore


def check_end():
    if check_win() or check_tie():
        return True
    return False


def check_win():
    return check_row() or check_col() or check_diag()


def check_row():
    global board
    if board[0] == board[1] and board[1] == board[2]:
        if board[0] == 'X' or board[0] == 'O':
            return True
    if board[3] == board[4] and board[4] == board[5]:
        if board[3] == 'X' or board[3] == 'O':
            return True
    if board[6] == board[7] and board[7] == board[8]:
        if board[6] == 'X' or board[6] == 'O':
            return True
    return False


def check_col():
    global board
    if board[0] == board[3] and board[3] == board[6]:
        if board[0] == 'X' or board[0] == 'O':
            return True
    if board[1] == board[4] and board[4] == board[7]:
        if board[1] == 'X' or board[1] == 'O':
            return True
    if board[2] == board[5] and board[5] == board[8]:
        if board[2] == 'X' or board[2] == 'O':
            return True
    return False


def check_diag():
    global board
    if board[0] == board[4] and board[4] == board[8]:
        if board[0] == 'X' or board[0] == 'O':
            return True
    if board[2] == board[4] and board[4] == board[6]:
        if board[2] == 'X' or board[2] == 'O':
            return True
    return False


def check_tie():
    global board
    i = 0
    while i < 9:
        if board[i] != 'X' and board[i] != 'O':
            return False
        i += 1
    return True


def flip_player():
    global curPlayer
    if curPlayer == "X":
        curPlayer = "O"
    else:
        curPlayer = "X"


def get_winner():
    global board

    if check_row():
        return row_same()
    if check_col():
        return col_same()
    if check_diag():
        return diag_same()
    return 'Tie'


def row_same():
    if board[0] == board[1] and board[1] == board[2]:
        return board[0]
    else:
        if board[3] == board[4] and board[4] == board[5]:
            return board[3]
        else:
            return board[6]


def col_same():
    if board[0] == board[3] and board[3] == board[6]:
        return board[0]
    else:
        if board[1] == board[4] and board[4] == board[7]:
            return board[1]
        else:
            return board[2]


def diag_same():
    if board[0] == board[4] and board[4] == board[8]:
        return board[0]
    else:
        return board[2]


def define_sign(number):
    global board, curPlayer

    if curPlayer == 'X':
        if board[number - 1] == 'X' or board[number - 1] == 'O':
            showinfo("Warning", "You are cheating! Replay!")
            root.destroy()

        board[number - 1] = 'X'
        flip_player()
        if number == 1:
            space1.config(text='X')
        if number == 2:
            space2.config(text='X')
        if number == 3:
            space3.config(text='X')
        if number == 4:
            space4.config(text='X')
        if number == 5:
            space5.config(text='X')
        if number == 6:
            space6.config(text='X')
        if number == 7:
            space7.config(text='X')
        if number == 8:
            space8.config(text='X')
        if number == 9:
            space9.config(text='X')
    else:
        compMove = computerPlay() + 1
        flip_player()
        if compMove == 1:
            space1.config(text='O')
        if compMove == 2:
            space2.config(text='O')
        if compMove == 3:
            space3.config(text='O')
        if compMove == 4:
            space4.config(text='O')
        if compMove == 5:
            space5.config(text='O')
        if compMove == 6:
            space6.config(text='O')
        if compMove == 7:
            space7.config(text='O')
        if compMove == 8:
            space8.config(text='O')
        if compMove == 9:
            space9.config(text='O')

    if check_end():
        curWinner = get_winner()
        if curWinner == 'Tie':
            showinfo("Game Result", "Tie. This game has no winner")
            root.destroy()
        else:
            showinfo("Game Result", "This game has ended, and the winner is " + curWinner)
            root.destroy()


root = Tk()

playerOneLabel = Label(root, text="Player X", font="times 20")
playerOneLabel.grid(row=0, column=1)

playerTwoLabel = Label(root, text="Player O", font="times 20")
playerTwoLabel.grid(row=0, column=2)

space1 = Button(root, width=20, heigh=10, command=lambda: define_sign(1))
space1.grid(row=1, column=1)

space2 = Button(root, width=20, heigh=10, command=lambda: define_sign(2))
space2.grid(row=1, column=2)

space3 = Button(root, width=20, heigh=10, command=lambda: define_sign(3))
space3.grid(row=1, column=3)

space4 = Button(root, width=20, heigh=10, command=lambda: define_sign(4))
space4.grid(row=4, column=1)

space5 = Button(root, width=20, heigh=10, command=lambda: define_sign(5))
space5.grid(row=4, column=2)

space6 = Button(root, width=20, heigh=10, command=lambda: define_sign(6))
space6.grid(row=4, column=3)

space7 = Button(root, width=20, heigh=10, command=lambda: define_sign(7))
space7.grid(row=8, column=1)

space8 = Button(root, width=20, heigh=10, command=lambda: define_sign(8))
space8.grid(row=8, column=2)

space9 = Button(root, width=20, heigh=10, command=lambda: define_sign(9))
space9.grid(row=8, column=3)

root.mainloop()
