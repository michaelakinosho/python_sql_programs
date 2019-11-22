q = int(input())

for q_itr in range(q):

    s = input()
    my_dict = {}
    my_list = []
    counter = 0

    s_len = len(s)
    for x in range(s_len):
        my_list = []
        s_char = s[x]
        s_count = s.count(s_char)
        #print("s count of: ", s_char, " is: ",s_count)
        if s_count > 1 and my_dict.get(s_char) == None:
            #print(s[x])
            idx = s.index(s_char)
            my_list.append(idx)
            idx += 1

            while len(my_list) < s_count:
                #print(len(my_list))
                if s[idx] == s_char:
                    my_list.append(idx)

                #print("len of my list: ", len(my_list))
                #my_dict.update({s[x]:my_list})
                idx += 1

            my_dict.update({s[x]:my_list})
    #step 1
    for n,m in my_dict.items():
        counter += sum(range(len(m)))
        print(n, sum(range(len(m))))

        i = 0
        while i < len(m):
            j = i
            while j < len(m):
                print(m[i], m[j]-1)
                if m[j]-1 > m[i]:
                    counter += 1
                j += 1
            i += 1

    print(my_dict)
    print(counter)
