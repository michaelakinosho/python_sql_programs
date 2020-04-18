from collections import Counter

M = Counter(sorted(list(map(str,input()))))
my_list = list(M.items())
my_val = list(M.values())
my_val.sort(reverse=True)
#print(my_list)
#print(my_val)

for i in my_val[0:3]:
    j = 0
    while j < len(my_list):
        if i == my_list[j][1]:
            print(my_list[j][0],my_list[j][1])
            my_list.pop(j)
            break
        j += 1
    #print(i[0],i[1])
