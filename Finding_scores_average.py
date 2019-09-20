if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()

    scores_list = student_marks.get(query_name)

    i = 0
    sum_scores = 0
    while i < len(scores_list):
        sum_scores += scores_list[i]
        i += 1

    print("{:.2f}".format(round(sum_scores/len(scores_list),2)))
