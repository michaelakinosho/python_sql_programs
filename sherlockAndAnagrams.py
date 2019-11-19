q = int(input())

for q_itr in range(q):

    s = input()
    my_dict = {}
    counter = 0
    s_len = len(s)
    for x in range(s_len):
        s_count = s.count(s[x])
        if s_count > 1:
            print(s[x])
            my_dict.update({s[x]:s.index(s[x])})

    #for (x,y) in my_dict.items():


    #         counter += sum(range(0,y+1))
    print(counter)
    print(my_dict)
