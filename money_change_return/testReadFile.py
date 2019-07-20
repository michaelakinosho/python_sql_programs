#import os

money_denom_list = []
fmd = open("money_denomination.txt")
for x in fmd:
    #print(x)
    money_denom_dict = {"Description_One":x.split(",")[0],"Description_Two":x.split(",")[1],"Amount":float(x.split(",")[2])}
    money_denom_list.append(money_denom_dict)

x = 0
while x < 2:
    print(money_denom_list[x]['Amount'])
    x += 1

for n in self.moneydenom:
    str_denoms += ("{} \n".format(self.moneydenom.index(n)["Description_One"]))
return (str_denoms)
