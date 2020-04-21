import pprint
from tkinter import *
import numpy as np
from tkinter import ttk

pp = pprint.PrettyPrinter (width=40, compact=True)


def find_empty(board):

    for row in range(len(board)):
        for element in range(len(board[1])):
            if board[row][element] == 0:
                return [row, element]
    return False


def solve(board):

    solved_board = board
    possible_answers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    if not find_empty(solved_board):
        return True

    empty_coord = find_empty(solved_board)
    empty_x = empty_coord[0]
    empty_y = empty_coord[1]

    for answer in possible_answers:

        if is_valid(solved_board, empty_x, empty_y, answer):
            solved_board[empty_x][empty_y] = answer

            if solve(solved_board):
                write_answers(solved_board)
                return True

            solved_board[empty_x][empty_y] = 0

    return False


def is_valid(board, row, column, check):

    if row_check(board, row, check) and column_check(board, column, check) and box_check(board, row - row % 3, column - column % 3, check):
        return True

    else:
        return False


def row_check(board, row, check):

    for element in board [row]:
        if check == element:
            return False

    return True


def column_check(board, column, check):

    for row in board:
        if check == row [column]:
            return False

    return True


def box_check(board, start_row, start_col, check):

    box_length = 3

    for row in range(box_length):
        for col in range(box_length):
            if board[start_row + row][start_col + col] == check:
                return False

    return True


root = Tk()
root.title ("Sudoku solver")


title = Label(root, text="Enter known values")
title.grid(row =0, column=4)


size = [0, 1, 2, 3, 4, 5, 6, 7, 8]

entry_list = []

for row in size:
    for col in size:
        ent = Entry(root, width=5)
        ent.insert(END, "0")
        entry_list.append(ent)
        ent.grid(row=row+1, column=col)


def create_board ():

    board_list = []
    for entry in entry_list:
        board_list.append(int(entry.get()))

    board = np.array(board_list).reshape(9, 9)
    solve(board)


def write_answers (board):

    answer_list = []
    for row in board:
        for col in row:
            answer_list.append(col)

    ctr=0

    for entry in entry_list:
        entry.delete(0, END)
        entry.insert(END, answer_list[ctr])
        ctr += 1

def clear_board():

    for entry in entry_list:
        entry.delete (0, END)
        entry.insert(END, "0")

solve_button = ttk.Button(root, text="Solve", command=create_board)
solve_button.grid(row=10, column=0)

clear_button = ttk.Button(root, text="Clear", command=clear_board)
clear_button.grid(row=10, column=1)

root.mainloop()



