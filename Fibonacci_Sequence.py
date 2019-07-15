#This program has two parts
#The program will number prompt for a Number: num
#In the first part: is num in the Fibonacci sequence of numbers
#In the second part: what is the Fibonacci number in the num position
#of the Fibonacci sequence

def fibo_num_sequ(num=0):
    fibo_num = 0
    first_fn = 0
    second_fn = 1

    x = 1
    print("x is: {}, 1st Fibonacci number is: {}, 2nd Fibonacci number is: {}, New Fibonacci number is {}:".format(x,first_fn,second_fn,first_fn))

    while x < num:
        x += 1
        print("x is: {}, 1st Fibonacci number is: {}, 2nd Fibonacci number is: {}, New Fibonacci number is {}:".format(x,first_fn,second_fn,second_fn))
        fibo_num = first_fn + second_fn
        first_fn = second_fn
        second_fn = fibo_num

    print(fibo_num)

def input_num():
    num_digits = 0

    try:
        num_digits = int(input("What is the Fibonacci number at this position in the Fibonacci Sequence: "))
        while num_digits < 1:
            print('Please try again and enter a positive integer')
            num_digits = int(input("Enter a positve integer for a position in the Fibonacci Sequence: "))

        fibo_num_sequ(num_digits)

    except ValueError:
        print('Oops enter a whole number')
        input_num()

input_num()
