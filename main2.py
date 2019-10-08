def testing():
    my_list = [1,2,3]
    my_set = {1,2,3}
    my_tuple = (1,2,3)

    return(my_list,my_set,my_tuple)

my_results = testing()
print(my_results[0])
print(my_results[1])
print(type(my_results[0]))
