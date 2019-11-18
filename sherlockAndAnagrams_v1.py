q = int(input())

for q_itr in range(q):
    counter = 0

    s = input()

    s_len = len(s)
    i = 0
    x = 1
    y = 0
    #for n in range(s_len):
    while i < s_len:
        x = i + 2
        while x < s_len:
            print(i, x-1," - ",i+1, x+1-1)
            print(s[i:x]," - ",s[i+1:x+1])
            #print(s[0:x]," - ",s[s_len-x:s_len])
            x += 1
        i += 1
    print(counter)
