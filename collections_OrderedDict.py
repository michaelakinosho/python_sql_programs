from collections import OrderedDict
ordered_dictionary = OrderedDict()
for i in range(0,int(input())):
    ord_dict = list((input().split()))
    net_price = int(ord_dict[-1])
    ord_dict.pop(-1)
    item_name = " ".join(ord_dict)

    #print(ord_dict)
    if item_name in ordered_dictionary:
        ordered_dictionary[item_name] += net_price
    else:
        ordered_dictionary[item_name] = net_price

    #print(ordered_dictionary[ord_dict[0]])

for x, y in ordered_dictionary.items():
    print(x, y)
