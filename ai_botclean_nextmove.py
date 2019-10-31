#!/usr/bin/python

# Head ends here

def next_move(posr, posc, board):
    list_dirty = list()
    list_dirty_min = list()
    list_dirty_path = list()
    for n in range(len(board)):
        for m in range(len(board[n])):
            if board[n][m] == 'd':
                list_dirty.append([n,m])
                list_dirty_path.append((posr-n,posc-m))
                list_dirty_min.append(abs(posr-n)+abs(posc-m))

    while len(list_dirty) > 0:
        d_index = list_dirty_min.index(min(list_dirty_min))
        closet_dirt, path_dirt = list_dirty[d_index], list_dirty_path[d_index]
        while posr != closet_dirt[0] and posc != closet_dirt[1]:
            if posr != closet_dirt[0]:
                if path_dirt[0] < 0:   #Moving UP
                    posr -= 1
                    print("UP")
                elif path_dirt[0] > 0:  #Moving DOWN
                    posr += 1
                    print("DOWN")

            if posc != closet_dirt[1]:
                if path_dirt[1] < 0:   #Moving LEFT
                    posc -= 1
                    print("LEFT")
                elif path_dirt[1] > 0:  #Moving RIGHT
                    posc += 1
                    print("RIGHT")

            if posr == closet_dirt[0] and posc == closet_dirt[1]:
                board[posr][posc] = '-'
                list_dirty.pop(d_index)
                list_dirty_path = list()
                list_dirty_min = list()
                for n in list_dirty:
                    list_dirty_path.append(posr-list_dirty[n][0],posc-list_dirty[n][1])
                    list_dirty_min.append(abs(posr-list_dirty[n][0])+abs(posc-list_dirty[n][1]))

                break

    print("")
    for n in range(len(board)):
        print(board[n])

# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
