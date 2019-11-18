mn = input().split()

m = int(mn[0])

n = int(mn[1])

magazine = input().rstrip().split()

note = input().rstrip().split()

magazine.sort()
note.sort()

counter = 0

for word in note:
    x = note.count(word)
    y = magazine.count(word)
    if word in magazine and x == 1:
        counter += 1
    elif word in magazine:
        if x == y:
            counter = counter + x

if counter == n:
    print('Yes')
else:
    print('No')

#print(magazine)
#print(note)
