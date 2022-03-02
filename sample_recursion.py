def sample_recursion(num):

    if num > 0:
        
        num -= 1
        print(num)
        ttl = sample_recursion(num)
    
    


sample_recursion(4)