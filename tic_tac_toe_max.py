# 0,0  0,1  0,2
# 1,0  1,1  1,2
# 2,0  2,1  2,2

import random
import time



def main():
    board = create_board()
    result = None
    while True:
        player_move(board)
        print_it(board)
        result = check_result(board)
        if result != None:
            break

        computer_move(board)
        print_it(board)
        result = check_result(board)
        if result != None:
            break
    print(result)


def create_board():
    return [[" "," "," "] for _ in range(3)]



def print_it(board):
    for row in range(len(board)):
        print(" " + (" | ".join(board[row])))
        if row < 2:
            print("-----------")
    print()


#The format for input should be “x, y” where x is the horizontal axis and y is the vertical axis.
def player_move(board):
    while True:
        try:
            move = input("Enter your move(x axis, y axis): ")
            positions = move.split(",")
            r,c = int(positions[0]),int(positions[1])
            if board[r][c] == " " :
                board[r][c] = "X"
                break
            else:
                print("Position alredy taken, choose another slot")
        except (ValueError, IndexError):
            print("Invalid input format, please try again")


#the computer will play randomly
#Every time the computer makes its move, the state of the board should be printed out.
def computer_move(board):
    print("Computer turn:")
    for _ in range(3):
        time.sleep(0.5)
        print(".")
    while True:
        r = random.randint(0,2)
        c = random.randint(0,2)
        if board[r][c] == " ":
            board[r][c] = "O"
            break


#If either the player or the computer wins, the state of the board should be printed out and the winner announced.
#The program should exit at that point.

def check_result(board):
    #checking for a tie
    if " " not in (board[0] + board[1] + board[2]):
        return "Its a tie!"


    win_result = None
    #checking rows (win)
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            win_result = row[0]
            break

    #checking columns (win)
    for i in range(3):
        column = [row[i] for row in board]
        if column[0] == column[1] == column[2] != " ":
            win_result = column[0]
            break

    #checking diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        win_result = board[1][1]

    elif board[2][0] == board[1][1] == board[0][2] != " ":
        win_result = board[1][1]

    if win_result == "X":
        return("You win!")

    elif win_result == "O":
        return("Computer wins!")


main()

#main
#change add

#edit new edit
