import string
def print_rangoli(size):
    #s is the substring pulled from ascii_lowercase
    s = string.ascii_lowercase[0:size]

    h = (size*2)-1
    w = (h*2)-1

    i = 0
    x = size-1
    #tes = "abcd"

    while x > -1:
        #tes = s[size-1:int(-size-2+x):-1] + s[0+int(x):size:1]
        tes = s[size-1:int(-size-1+x):-1] + s[1+int(x):size:1]
        j = 0
        t = ""
        while j < len(tes)-1:
            t += tes[j] + "-"
            j += 1
        t += tes[-1]
        tes = t

        print('{:-^{T}}'.format(tes,T=w))
        x -= 1

    x = 1
    while x < size:
        tes = s[size-1:int(-size-1+x):-1] + s[1+int(x):size:1]
        j = 0
        t = ""
        while j < len(tes)-1:
            t += tes[j] + "-"
            j += 1
        t += tes[-1]
        tes = t

        print('{:-^{T}}'.format(tes,T=w))
        x += 1

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
