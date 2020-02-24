
for x in range(int(input())):
    A = input()
    A_set = set(map(int, input().split()))
    B = input()
    B_set = set(map(int, input().split()))

    print(A_set.issubset(B_set))
    #print(z)
