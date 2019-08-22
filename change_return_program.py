#My signature and contact details
#Written by: Michael Akinosho
#Email: michaelakinosho@moaadvisory.com

chg_list = [{"type":"quarter","amt":0.25,"count":0},{"type":"dime","amt":0.10,"count":0},{"type":"nickel","amt":0.05,"count":0},{"type":"penny","amt":0.01,"count":0}]
def change_return(cost, paid):
    try:
        if cost > paid:
            print("Additional payment of ${:.2f} required".format(cost-paid))
        else:
            change = float(paid) - float(cost)
            i = 0
            for n in chg_list:
                n_amt = n["amt"]
                while change > n_amt-0.01:
                    change = round(change - n_amt,2)
                    n["count"] += 1
                    print(change)

            #chg_list[3]["count"] = 4
            #print(type(chg_list))
            #print(chg_list)
            #print(type(chg_list[0]))
            print(chg_list)

    except ValueError:
        print("Amount entered is not a number")
    except:
        print("Something went wrong")

    finally:
        print("Thank you")

change_return(1,2.04)
