def average(array):
    # your code goes here
    DH = set(array)
    sum_DH = sum(DH)

    count_DH = len(DH)

    avg_DH = sum_DH/count_DH

    print(avg_DH)
    return(avg_DH)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    #print(result)
