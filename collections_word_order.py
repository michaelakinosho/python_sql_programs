from collections import Counter
my_list = list()
for x in range(0,int(input())):
    my_list.append(str(input()))

c = Counter(my_list)
print(len(c))
s_list = list(c.values())
#print(s_list)

print(*(n for n in s_list), sep = " ")
#print(*((n) for n in s_list), sep = " ")
#print(*((n) for n in s), sep = " ")
