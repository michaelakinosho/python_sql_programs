from itertools import groupby

A = input()

groups = []
m_list = []

for n,m in groupby(A):
    print(n)
    groups.append(list(m))

for n in groups:
    m_list.append([len(n),int(n[0])])

print(*(tuple((n)) for n in m_list), sep = " ")
