strings_count = int(input())
strings = []

for _ in range(strings_count):
    strings.append(input())


queries_count = int(input())


for _ in range(queries_count):
    query = input()
    print(strings.count(query))
