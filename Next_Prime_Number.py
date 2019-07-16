#Program will prompt the user for the prime number in the nth position
#Afterwards will prompt user if the next prime number

def next_prime_number(n):
    print("For the Prime Number Pundits out there.")
    print("One is not considered a prime number.")
    print("One may be a prime :-)")

    n_list = []
    #print(n_list)
    #print(type(n_list))

    #print(type(prime_set))

    fmod = 0
    prime_num = 2
    prime_set = set()
    prime_set.add(prime_num)

    x = 0

    while len(prime_set) < n:
#IF AT THE END OF THE FOR LOOP AND FMOD IS NOT ZERO, THEN THIS NUMBER IS A PRIME NUMBER
    	fmod = n % prime_num
    	if fmod == 0:
    		prime_set.add(prime_num)
    		factors_list.append(prime_num)
    		n = n / prime_num
    	else:
    		prime_num += 1
    		for y in prime_set:
    			if prime_num % y != 0:
    				break
    	#print(x)
    	x += 1

    print(prime_set)
    print(factors_list)

def input_num():
    num_digits = 0

    try:
        num_digits = int(input("Enter a positve integer to find it's prime factors: "))
        while num_digits < 1:
            print('Please try again and enter a positive integer')
            num_digits = int(input("Enter a positve integer to find it's prime factors: "))

        num_prime_factors(num_digits)

        result = input('Find the next prime number?\nEnter Yes or No:').lower().[0]
        while result == 'y':
            num_digits += 1
            print("The next prime number is: ")
            next_prime_number(num_digits)

    except ValueError:
        print('Oops enter a whole number')
        input_num()

input_num()
