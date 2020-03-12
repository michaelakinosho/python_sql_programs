from collections import deque
d = deque()
for i in range(0,int(input())):
    method = list(input().split())
    method_name = method[0]

    if method_name == 'append':
        d.append(method[1])
    elif method_name == 'appendleft':
        d.appendleft(method[1])
    elif method_name == 'pop':
        d.pop()
    elif method_name == 'popleft':
        d.popleft()

print(*(n for n in d),sep = " ")
