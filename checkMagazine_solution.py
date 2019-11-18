mn = input().split()

m = int(mn[0])

n = int(mn[1])

magazine = input().rstrip().split()

note = input().rstrip().split()

magazine.sort()
note.sort()

counter = 0
i = 0
j = 0

while i < n and j < m:
    if note[i] == magazine[j]:
        counter += 1
        i += 1
    j += 1


if counter == n:
    print('Yes')
else:
    print('No')

#print(magazine)
#print(note)
