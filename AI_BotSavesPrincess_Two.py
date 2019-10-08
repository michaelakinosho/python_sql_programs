#!/usr/bin/python

def nextMove(n,r,c,grid):
#print all the moves here
    moves_list = []
    my_m = (r,c)
    i = 0
    while i < len(grid):
        if 'p' in grid[i]:
            j = grid[i].index('p')
            break
        i += 1
    my_p = (i,j)
    #print(my_m)
    #print(my_p)

    i_diff = my_p[0] - my_m[0]
    j_diff = my_p[1] - my_m[1]

    if i_diff > 0:
        x = 0
        while x < abs(i_diff):
            moves_list.append("DOWN")
            x += 1
    elif i_diff < 0:
        x = 0
        while x < abs(i_diff):
            moves_list.append("UP")
            x += 1

    if j_diff < 0:
        x = 0
        while x < abs(j_diff):
            moves_list.append("LEFT")
            x += 1
    elif j_diff > 0:
        x = 0
        while x < abs(j_diff):
            moves_list.append("RIGHT")
            x += 1

    return(moves_list[0])


n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))
