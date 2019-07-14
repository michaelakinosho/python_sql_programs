#This program has two parts
#The program will number prompt for a Number: num
#In the first part: is num in the Fibonacci sequence of numbers
#In the second part: what is the Fibonacci number in the num position
#of the Fibonacci sequence

def fibo_num_sequ():
    fibo_num = 0
    first_fn = 0
    second_fn = 1

    x = 1
    print("x is: {}, 1st Fibonacci number is: {}, 2nd Fibonacci number is: {}, New Fibonacci number is {}:".format(x,first_fn,second_fn,first_fn))

    num = 1

    while x < num:
        x += 1
        print("x is: {}, 1st Fibonacci number is: {}, 2nd Fibonacci number is: {}, New Fibonacci number is {}:".format(x,first_fn,second_fn,second_fn))
        fibo_num = first_fn + second_fn
        first_fn = second_fn
        second_fn = fibo_num

    print(fibo_num)

fibo_num_sequ()
