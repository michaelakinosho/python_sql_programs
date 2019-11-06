def print_formatted(number):
    # your code goes here
    width = len(bin(number)) - 2
    for num in range(1,number+1):
        for base in 'doXb':
            print('{num:{width}{base}}'.format(num=num,base=base,width=width),end=' ')
        print()

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
