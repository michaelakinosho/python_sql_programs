def v_count(i, paths, u_list, ep_only_list):

    x = 0
    n_count = 1
    my_lst = [u_list[i]]

    #print(my_lst)
    while x < len(paths):
        j = 0
        while j < len(paths):
            if paths[x][1] == paths[j][0]:
                if u_list[i] == paths[x][0]:
                    print("u list item: {}, paths[x][0]: {}, paths[x][1]: {}".format(u_list[i],paths[x][0],paths[x][1]))
                    if paths[x][1] not in ep_only_list:
                        my_lst.append(paths[x][1])
                        if my_lst[len(my_lst)-2] == my_lst[len(my_lst)-1]:
                            my_lst.pop()
                    if paths[j][1] not in ep_only_list:
                        my_lst.append(paths[j][1])
                        if my_lst[len(my_lst)-2] == my_lst[len(my_lst)-1]:
                            my_lst.pop()

                    n_count += 1

            j += 1
        x += 1
    return(my_lst, n_count)
    #return(n_count)
