#Credit for this solution goes to Artem Akulov on hackerrank @akulov_artem
#Thanks for sharing
#My independent solution timed out on the larger datasets
py_input = open('py_input.txt','r')

_, k = [int(i) for i in py_input.readline().split()]
t = [int(i) for i in py_input.readline().split()]
s = [int(i) % k for i in py_input.readline().split()]

print(t)
print(s)
#_, k = [int(i) for i in input().split()]
#s = [int(i) % k for i in input().split()]
c= set(s)
print(c)

subset = 0
print("In the beginning subset is:",subset)
indexes = []
subset_indexes = []
for i in c:
    print("So i is:",i)
    if i == 0 or i == k / 2:
        print(" +Add 1 to subset:", 1)
        subset += 1
        indexes.append(i)
        subset_indexes.append(1)
        #print(indexes)
    else:
        #print("What is k: ",k,"What is k-i:",k-i,"What is count of k-i:",s.count(k-i),"What is i:" ,i,"What is count of i:",s.count(i))
        if (k - i) in c:
            s_index = (i, k - i)[s.count(k - i) > s.count(i)]
            if s_index not in indexes:
                print("s_index is:",s_index, "If count of k-i in s", s.count(k-i)," > count of i in s", s.count(i)," return k-i:", k-i," else return i",i)

                print(" +Add count of s_index to subset:", s.count(s_index))
                print(subset + s.count(s_index), " = ", subset, " + ", s.count(s_index))
                subset += s.count(s_index)
                indexes.append(s_index)
                subset_indexes.append(s.count(s_index))
        else:
            print(" +Add count of i to subset:", s.count(i))
            subset += s.count(i)
            indexes.append(i)
            subset_indexes.append(s.count(i))
    print("Now subset is:",subset)
    print("Latest subset_indexes is:", subset_indexes)
    print("Latest indexes is:",indexes,"\n")
print(subset)
