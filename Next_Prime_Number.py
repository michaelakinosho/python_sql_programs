#My signature and contact details
#Written by: Michael Akinosho
#Email: michaelakinosho@moaadvisory.com
#Program will prompt the user for the prime number in the nth position
#Afterwards will prompt user if the next prime number

def next_prime_number(n):
    print("For the Prime Number Pundits out there.")
    print("One is not considered a prime number.")
    print("One may be a prime :-)")

    #print(n_list)
    #print(type(n_list))

    #print(type(prime_set))

    fmod = 0
    #The first prime number is two
    num = 2
    prime_list = [num]

    num += 1
    while len(prime_list) < n:
#IF AT THE END OF THE FOR LOOP AND FMOD IS NOT ZERO, THEN THIS NUMBER IS A PRIME NUMBER
        for y in prime_list:
            fmod = num%y
            if fmod == 0:
                num += 1
                break
        if fmod != 0:
            if num not in prime_list:
                prime_list.append(num)

    print(prime_list)

def input_num():
    num_digits = 0

    try:
        num_digits = int(input("Enter a positve integer to find it's prime factors: "))
        while num_digits < 1:
            print('Please try again and enter a positive integer')
            num_digits = int(input("Enter a positve integer to find it's prime factors: "))

        next_prime_number(num_digits)

        result = input('Find the next prime number?\nEnter Yes or No:').lower()[0]
        while result == 'y':
            num_digits += 1
            print("The next prime number is: ")
            next_prime_number(num_digits)
            result = input('Find the next prime number?\nEnter Yes or No:').lower()[0]

        if result != 'y':
                print('\nProgram is exiting.')
                print("Thank you for testing the program.")

    except ValueError:
        print('Oops enter a whole number')
        input_num()

input_num()
