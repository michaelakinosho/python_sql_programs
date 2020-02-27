from collections import namedtuple

N, Student, my_list = int(input()), namedtuple('Student',input()), []

for _ in range(0,N):

    my_list.append(int(Student._make(input().split()).MARKS))

print('{:.2f}'.format(sum(my_list)/N))
