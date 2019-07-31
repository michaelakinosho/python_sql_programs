
class MoneyDenom:

    def __init__(self):

        self.moneydenom = []
        self.load_denom()

    def __str__(self):
        i = 1
        str_denoms = 'The money denominations available are:\n'
        str_denoms += "Num\tDescription_One\t\t\t\tAmount\n"
        for n in self.moneydenom:
            str_denoms += ("{:2}\t {:<40} {:,}\n".format(self.moneydenom.index(n)+1,n["Description_One"],n["Amount"]))
        return (str_denoms)

    def load_denom(self):
        try:
            fmd = open("money_denomination.txt")
            for x in fmd:
                #print(x)
                moneydenom_dict = {"Id":x.split(",")[0],"Description_One":x.split(",")[1],"Description_Two":x.split(",")[2],"Amount":float(x.split(",")[3])}
                self.moneydenom.append(moneydenom_dict)
        except IOError:
            print("Money denomination file is missing")
        except ValueError:
            print("The data type of value is incorrect, did not match expected data type")

#my = MoneyDenom()
#print(my)
#for n in my.moneydenom:
#    print('{}\n'.format(n))
