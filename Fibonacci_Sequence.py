#My signature and contact details
#Written by: Michael Akinosho
#Email: michaelakinosho@moaadvisory.com

#This program has two parts
#The program will number prompt for a Number: num
#In the first part: what is the Fibonacci number in the position entered
#In the second part: is the position entered in the first part in the Fibonacci sequence of numbers
#of the Fibonacci sequence

def fibo_num_sequ(num=0):
    fibo_num = 0
    first_fn = 0
    second_fn = 1
    fibo_num_lst = [first_fn,second_fn]

    x = 1
    print("Position {} has Fibonacci number of: {} ".format(x,first_fn))

    x += 1
    print("Position {} has Fibonacci number of: {} ".format(x,second_fn))

    x += 1
    while len(fibo_num_lst) < num:
        fibo_num = first_fn + second_fn
        fibo_num_lst.append(fibo_num)
        print("Position {} has Fibonacci number of: {}".format(x,fibo_num))
        first_fn = second_fn
        second_fn = fibo_num
        x += 1

    if num in fibo_num_lst:
         print("The position entered above of: {} is also a Fibonacci number at position index of: {} ".format(num, fibo_num_lst.index(num)+1))
    print(fibo_num_lst)

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
