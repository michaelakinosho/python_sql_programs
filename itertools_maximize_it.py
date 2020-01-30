from itertools import starmap
A,B = map(int, input().split(" "))

my_max = 0
ttl_max = 0
m_lst = []
for x in range(A):
    m_lst = list(map(int,input().split(" ")))
    m_lst.pop(0)
    n_max = 0
    i = 0
    while i < len(m_lst):
        x = [*starmap(pow,[[m_lst[i],2]])]
        if x[0]%B > my_max:
            my_max = x[0]%B
        i += 1
    ttl_max += my_max

print(ttl_max)
    #m_lst.append(sorted(list(map(int,input().split(" "))))[-1])

    #my_max += pow(sorted(list(map(int,input().split(" "))))[-1],2)

#print(my_max)
#print(m_lst)
#print(my_max%B)
#print(A)
#print(B)

#print(m_lst)
