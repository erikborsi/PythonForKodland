# Imagine a square chessboard.
# The queen (or queen) can move vertically, horizontally and diagonally any number of cells.
# Based on the coordinates of the two squares, determine whether the queen can move from the first to the second in one
# move.If it can, print YES. Otherwise, print NO.The program gets 4 whole numbers from 1 to 8. The first and the second
# one give the column and the row for the first square, the third and the fourth for the second square.
#
# Entry example  #1
# 1
# 1
# 2
# 2
#
# Example result  #1
# YES
#
# Entry example  # 2
# 1
# 1
# 8
# 2
#
# Example result  #2
# NO

def user_input_list_creator():
    user_input_list = []
    move = []
    for i in range(4):
        user_input = input()
        user_input_list.append(user_input)
    move_str = ''.join(user_input_list)
    for i in move_str:
        move.append(int(i))
    decision(move)


def decision(move_in):
    column_coordinate_one = move_in[0]
    column_coordinate_two = move_in[1]
    row_coordinate_one = move_in[2]
    row_coordinate_two = move_in[3]
    if column_coordinate_one == 1 and column_coordinate_two in list(range(1, 9)):
        if row_coordinate_one == 1 and row_coordinate_two in list(range(2, 9)):
            response_back(True)
        elif row_coordinate_one == 1 and row_coordinate_two == 1:
            # assuming the queen is on 1-1, so it cannot move to the same place
            response_back(False)
        elif row_coordinate_one == row_coordinate_two:
            response_back(True)
        elif row_coordinate_one in list(range(2, 9)) and row_coordinate_two == 1:
            response_back(True)
        else:
            response_back(False)
    else:
        response_back(False)


def response_back(decision_in):
    if decision_in:
        print("YES")
    else:
        print("NO")


user_input_list_creator()
