#!/usr/bin/python

def displayPathtoPrincess(n,grid):
#print all the moves here
    moves_list = []
    my_m = (int(n/2),int(n/2))
    if grid[0][0] == 'p':
        my_p = (0,0)
    elif grid[0][n-1] == 'p':
        my_p = (0,n-1)
    elif grid[n-1][0] == 'p':
        my_p = (n-1,0)
    elif grid[n-1][n-1] == 'p':
        my_p = (n-1,n-1)

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

    for y in moves_list:
        print(y)
    #print(my_m)
    #print(my_p)

m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
