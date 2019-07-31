from MoneyDenom import MoneyDenom

class CashOnHand:

    def __init__(self):

        self.cashonhand = []
        #my_cashonhand = MoneyDenom()

        self.load_cashonhand()

    def __str__(self):
        i = 1
        str_coh = 'The cash on-hand by denomination is: \n'
        str_coh += "Num\tDescription\t\t\t\t\tAmount\tQuantity\n"
        for n in self.cashonhand:
            str_coh += ("{:2}\t {:<40} {:10,} {:10,}\n".format(self.cashonhand.index(n)+1,n["Description_One"],n["Amount"],n["Quantity"]))
        #print(self.cashonhand)
        return (str_coh)

    def load_cashonhand(self):
        coh_quantity = []
        try:
            my_cashonhand = MoneyDenom()
            #print(my_cashonhand.moneydenom[0])
            #for n in my_cashonhand.moneydenom:
            #    print('{} \n'.format(n))
            faqmd = open("cashonhand.txt")
            for y in faqmd:
                coh_dict = {"Id":y.split(",")[0],"Quantity":y.split(",")[1]}
                coh_quantity.append(coh_dict)

            for x in my_cashonhand.moneydenom:
                #print(x)
                cashonhand_dict = x
                i = 0
                while i < len(coh_quantity):
                    if coh_quantity[i]["Id"]==x["Id"]:
                        cashonhand_dict.update({"Quantity":int(coh_quantity[i]["Quantity"])})
                        self.cashonhand.append(cashonhand_dict)
                    i += 1

        except IOError:
            print("Cash on-hand file is missing.")
        except ValueError:
            print("The data type of value is incorrect, did not match expected data type")

    def update_cashonhand(self):
        pass

my = CashOnHand()
print(my)
#for n in my.cashonhand:
#    print('{}\n'.format(n))
