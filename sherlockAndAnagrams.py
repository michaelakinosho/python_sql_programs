q = int(input())

for q_itr in range(q):

    s = list(input())
    my_dict = {}
    counter = 0
    for x in range(len(s)):
        my_dict.update({s[x]:s.count(s[x])})

    # for x,y in my_dict.items():
    #     #x_sum = dict.values()
    #     if y > 1:
    #         counter += sum(range(0,y+1))
    print(counter)
    print(my_dict)
