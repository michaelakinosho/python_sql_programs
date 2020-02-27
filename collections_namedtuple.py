from collections import namedtuple

N = int(input())
Student = namedtuple('Student',input())
average_mark = 0

for _ in range(0,N):
    #record = input().split("\t")
    #print(record)
    stu = Student._make(input().split()).MARKS
    #stu = Student(record[0], record[1], record[2], record[3])
    #average_mark += int(stu.MARKS)
    print(stu)

print('{:.2f}'.format(average_mark/N))
