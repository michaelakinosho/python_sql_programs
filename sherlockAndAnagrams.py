q = int(input())


for q_itr in range(q):

    s = input()
    my_dict = {}
    my_list = []
    counter = 0

    s_len = len(s)
    for x in range(s_len):
        s_char = s[x]
        s_count = s.count(s_char)
        print("s count of: ", s_char, " is: ",s_count)
        if s_count > 1:
            #print(s[x])
            idx = s.index(s_char)
            my_list.append(idx)
            idx += 1

            while len(my_list) < s_count:
                print(len(my_list))
                if s[idx] == s_char:
                    my_list.append(idx)

                print("len of my list: ", len(my_list))
                my_dict.update({s[x]:my_list})
                idx += 1


    for x,y in my_dict.items():
        counter += 0
        while y < s_len:
            if s[y-1] == s[y]:
                counter += 1
            elif s[y] == x:
                counter += 1

            y += 1

    #         counter += sum(range(0,y+1))
    #print(counter)
    print(my_dict)
