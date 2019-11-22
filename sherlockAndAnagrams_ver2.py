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

                idx += 1

            my_dict.update({s[x]:my_list})

    for n,m in my_dict.items():
        #step 1
        counter += sum(range(len(m)))
        print("In step 1 count of: ",n, sum(range(len(m))))

        i = 0
        my_str = ""
        while i < len(m)-2:
            j = 1
            while j < len(m)-1-i:
                #print(str(m[i]) + str(m[i]+j))
                k = 1
                while k < len(m)-1:
                    print(str(m[i]) + str(m[i]+j) + str(m[i]+k) + str(m[i]+j+k) )
                    k += 1
                j += 1
            i += 1

    print(my_dict)
    print(counter)
