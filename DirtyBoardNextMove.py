#!/usr/bin/python

# Head ends here

def next_move(posr, posc, board,dirty_list):

    print("")

# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    dirty_list = []
    i = 0
    while i < 5:
        j = 0
        while j < 5:
            if board[i][j] == 'd':
                dirty_list.append(tuple(i,j))
            j += 1
        i += 1
    print(dirty_list)
    next_move(pos[0], pos[1], board, dirty_list)
