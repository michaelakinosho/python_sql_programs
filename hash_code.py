s="mike"
mask = (1 << 32) - 1
print(mask)
h = 0
for character in s:
    h = (h << 5 & mask)|(h >> 27)
    h += ord(character)
print(h)
