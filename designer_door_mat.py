#Replace all ______ with rjust, ljust or center.

dims = list(map(int, input().rstrip().split()))
brth = dims[0]
wth = dims[1]
se = '.|.'
dash = '-'
nd = 0
wc = "WELCOME"
hw = (brth-1)/2
se_count = 1

j = 1
for i in range(brth):
    nd = int((wth-(j*3))/2)
    if i == hw:
        print((dash*int((wth-7)/2) + wc + dash*int((wth-7)/2)))

    elif i < hw:
        #print((dash*nd).rjust(wth) + (se*j).center(j*3) + (dash*nd).ljust(wth))
        print((dash*nd) + (se*j).center(j*3) + (dash*nd))
        j += 2
    elif i > hw:
        j -= 2
        nd += 3
        print((dash*nd) + (se*j).center(j*3) + (dash*nd))


#Top Cone
#for i in range(thickness):
#    print((c*i).rjust(thickness)+c+(c*i).ljust(thickness))

#Top Pillars
#for i in range(thickness+1):
#    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
#for i in range((thickness+1)//2):
#    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
#for i in range(thickness+1):
#    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Bottom Cone
#for i in range(thickness):
#    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
