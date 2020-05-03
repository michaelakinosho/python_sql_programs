py_input = open('py_input.txt','r')

h = [int(i) for i in py_input.readline().split()]

word = [str(i) for i in py_input.readline().rstrip()]

print(ord(word[0])-97)
print(h)
print(word)

tall = 1
temp = 0
for i in range(len(word)):
    temp = h[ord(word[i])-97]
    tall = (tall,temp)[temp > tall]

print(len(word)*1*tall)
