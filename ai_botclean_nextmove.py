#!/usr/bin/python

# Head ends here
import pdb

def next_move(posr, posc, board):
    list_dirty = list()
    list_dirty_min = list()
    list_dirty_path = list()
    move_list =  list()
    for n in range(len(board)):
        for m in range(len(board[n])):
            if board[n][m] == 'd':
                list_dirty.append([n,m])
                list_dirty_path.append((posr-n,posc-m))
                list_dirty_min.append(abs(posr-n)+abs(posc-m))

    while len(list_dirty) > 0:
        d_index = list_dirty_min.index(min(list_dirty_min))
        closet_dirt, path_dirt = list_dirty[d_index], list_dirty_path[d_index]
        #print(posr,posc,path_dirt,closet_dirt)
        #pdb.set_trace()
        while posr != closet_dirt[0] or posc != closet_dirt[1]:
            if posr != closet_dirt[0]:
                if path_dirt[0] < 0:   #Moving UP
                    posr += 1
                    move_list.append("DOWN")
                    #print("DOWN")
                elif path_dirt[0] > 0:  #Moving DOWN
                    posr -= 1
                    move_list.append("UP")
                    #print("UP")

            if posc != closet_dirt[1]:
                #pdb.set_trace()
                if path_dirt[1] < 0:   #Moving LEFT
                    posc += 1
                    move_list.append("RIGHT")
                    #print("RIGHT")
                elif path_dirt[1] > 0:  #Moving RIGHT
                    posc -= 1
                    move_list.append("LEFT")
                    #print("LEFT")

            if posr == closet_dirt[0] and posc == closet_dirt[1]:
                #print(posr,posc,path_dirt,closet_dirt)
                #pdb.set_trace()
                move_list.append("CLEAN")
                #print("CLEAN")
                board[posr][posc] = '-'
                list_dirty.pop(d_index)
                list_dirty_path = list()
                list_dirty_min = list()

                break
        for n in range(len(board)):
            for m in range(len(board[n])):
                if board[n][m] == 'd':
                    list_dirty_path.append((posr-n,posc-m))
                    list_dirty_min.append(abs(posr-n)+abs(posc-m))

    #print(move_list)
    return(move_list[0])


# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    print(next_move(pos[0], pos[1], board))
