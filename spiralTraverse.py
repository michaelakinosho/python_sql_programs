def spiralTraverse(array):
    n = len(array)
    if n <= 1:
        return array[0]

    m = len(array[0])
    print(n,m)

      
    newArray = []
    row_limit, col_limit = n, m
    current_loop = 0
    i, j = current_loop, current_loop
    num_of_loops = sum(divmod(5,2,))
    current_loop = 0
    num_items = n*m
    current_item = 0
    while current_loop < num_of_loops:

        #traverse to the right
        while j < col_limit:
            if current_item < num_items:
                newArray.append(array[i][j])
                current_item += 1
            else:
                return newArray
            
            j += 1
        
        #traverse downwards
        j -= 1
        i += 1
        while i < row_limit:
            if current_item < num_items: 
                newArray.append(array[i][j])
                current_item += 1
            else:
                return newArray
            
            i += 1
            
        #traverse to the left
        i -= 1
        j -= 1
        while j > 0 + current_loop:
            if current_item < num_items:
                newArray.append(array[i][j])
                current_item += 1
            else:
                return newArray
            
            j -= 1
            
        #traverse upwards
        
        while i > 0 +  current_loop:
            if current_item < num_items:
                newArray.append(array[i][j])
                current_item += 1
            else:
                return newArray
            
            i -= 1

        row_limit, col_limit = row_limit - 1, col_limit - 1
        current_loop += 1
        i, j = current_loop, current_loop

    return newArray
  
array = [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]
print(spiralTraverse(array))

array = [[1,2,3],[8,9,4],[7,6,5]]
print(spiralTraverse(array))

array = [[1]]
print(spiralTraverse(array))