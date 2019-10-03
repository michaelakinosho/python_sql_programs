#!/usr/bin/python

def displayPathtoPrincess(n,grid):
#print all the moves here
    i = 0
    j = 0
    my_m = (int(n/2),int(n/2))
    if grid[i][j] == 'p':
        my_p = (i,j)
    elif grid[i][j+n-1] == 'p':
        my_p = (i,j+n-1)
    elif grid[i+n-1][j] == 'p':
        my_p = (i+n-1,j)
    elif grid[i+n-1][j+n-1] == 'p':
        my_p = (i+n-1,j+n-1)

    i_diff = my_p[0] - my_m[0]
    j_diff = my_p[1] - my_m[1]

    if i_diff > 0:
        print("DOWN"*abs(i_diff))
    elif i_diff < 0:
        print("UP"*abs(i_diff))

    if j_diff < 0:
        print("LEFT"*abs(j_diff))
    elif j_diff > 0:
        print("RIGHT"*abs(j_diff))

    #print(my_m)
    #print(my_p)

m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
