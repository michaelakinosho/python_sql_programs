from collections import namedtuple

N = int(input())
Student = namedtuple('Student',input())
average_mark = 0

for _ in range(0,N):
    record = input().split(" ")
    #print(record)
    stu = Student._make(record)
    stu = Student(record[0], record[1], record[2], record[3])
    average_mark += int(stu.MARKS)

print('{:.2f}'.format(average_mark/N))
