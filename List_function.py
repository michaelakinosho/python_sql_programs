if __name__ == '__main__':
    N = int(input())

    #insert
    #pirnt
    #remove
    #append
    #sort
    #pop
    #reverse

    int_list = []

    for _ in range(0,N):
        x = input().split()

        if x[0] == 'insert':
            int_list.insert(int(x[1]), int(x[2]))
        elif x[0] == 'print':
            print(int_list)
        elif x[0] == 'remove':
            int_list.remove(int(x[1]))
        elif x[0] == 'append':
            int_list.append(int(x[1]))
        elif x[0] == 'sort':
            int_list.sort()
        elif x[0] == 'pop':
            int_list.pop()
        elif x[0] == 'reverse':
            int_list.reverse()
