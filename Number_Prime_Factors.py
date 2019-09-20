#My signature and contact details
#Written by: Michael Akinosho
#Email: michaelakinosho@moaadvisory.com

#Program will prompt user for a number
#Will provide the user a list of prime factors for number entered

def num_prime_factors(n=1):

    print("Let's find the Prime Factors")
    n_list = []
    #print(n_list)
    #print(type(n_list))

    prime_set = set()
    #print(type(prime_set))

    factors_list = []
    fmod = 0
    prime_num = 2
    x = 0

    while n != 1:
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

    #print(prime_set)
    #print(factors_list)

    i = 0
    j = 0
    factors_set = {1}
    f_num = 0
    while i < len(factors_list):
        f_num = factors_list[i]
        factors_set.add(f_num)
        j = 0

        while j < len(factors_list):
            if i != j:
                f_num = f_num * factors_list[j]
            factors_set.add(f_num)

            j += 1

        f_num = factors_list[i]
        j = len(factors_list) - 1
        while j > 0:
            #print(j)
            if i != j:
                f_num = f_num * factors_list[j]
            factors_set.add(f_num)

            j -= 1
        i += 1
    print(factors_set)

def input_num():
    num_digits = 0

    try:
        num_digits = int(input("Enter a positve integer to find it's prime factors: "))
        while num_digits < 1:
            print('Please try again and enter a positive integer')
            num_digits = int(input("Enter a positve integer to find it's prime factors: "))

        num_prime_factors(num_digits)

    except ValueError:
        print('Oops enter a whole number')
        input_num()

input_num()
