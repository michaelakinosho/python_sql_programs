q = int(input())


for q_itr in range(q):

    s = input()
    my_dict = {}
    counter = 0

    s_len = len(s)
    for x in range(s_len):
        s_count = s.count(s[x])
        if s_count > 1:
            #print(s[x])
            my_dict.update({s[x]:[s.index(s[x]),s_count]})

    for x,y in my_dict.items():
        counter += 0
        while y < s_len:
            if s[y-1] == s[y]:
                counter += 1
            elif s[y] == x:
                counter += 1

            y += 1

    #         counter += sum(range(0,y+1))
    print(counter)
    print(my_dict)
