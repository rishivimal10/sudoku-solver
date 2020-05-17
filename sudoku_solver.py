from tkinter import *
import numpy as np
from tkinter import ttk


def find_empty(board):

    for row2 in range(len(board)):
        for element in range(len(board[1])):
            if board[row2][element] == 0:
                return [row2, element]
    return False


def solve(board):

    solved_board = board
    possible_answers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    if not check_initial(solved_board):
        unsolvable()
        return False

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


def check_initial(board):

    for row2 in range(0, 9):
        st = set()
        for element in range(0, 9):
            if not board[row2][element] == 0 and board[row2][element] in st:
                return False
            else:
                st.add(board[row2][element])

    for column in range(0, 9):
        st = set()
        for row2 in range(0, 9):
            if not board[row2][column] == 0 and board[row2][column] in st:
                return False
            else:
                st.add(board[row2][column])


    return True


def is_valid(board, row2, column, check):

    if row_check(board, row2, check) and column_check(board, column, check) and box_check(board, row2 - row2 % 3, column-column % 3, check):
        return True

    else:
        return False


def row_check(board, row2, check):

    last_element = 0
    for element in board[row2]:
        if check == element:
            return False
        if not element == 0:
            if last_element == element:
                return False
            else:
                last_element = element

    return True


def column_check(board, column, check):

    last_element = 0
    for row2 in board:
        if check == row2[column]:
            return False
        if not row2[column] == 0:
            if last_element == row2[column]:
                return False
            else:
                last_element = row2[column]

    return True


def box_check(board, start_row, start_col, check):

    box_length = 3
    last_element = 0

    for row2 in range(box_length):
        for col2 in range(box_length):
            if board[start_row + row2][start_col + col2] == check:
                return False
            if not board[start_row + row2][start_col + col2] == 0:
                if last_element == board[start_row + row2][start_col + col2]:
                    return False
                else:
                    last_element = board[start_row + row2][start_col + col2]

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
    if not solve(board):
        unsolvable()


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

def unsolvable():

    label = Label(root, text="This puzzle is unsolvable")
    label.grid(row=11, column=0)
    label.after(5000, lambda: label.destroy())
    clear_board()

solve_button = ttk.Button(root, text="Solve", command=create_board)
solve_button.grid(row=10, column=0)

clear_button = ttk.Button(root, text="Clear", command=clear_board)
clear_button.grid(row=10, column=1)

root.mainloop()



