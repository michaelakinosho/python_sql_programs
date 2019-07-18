#My signature and contact details
#Written by: Michael Akinosho
#Email: michaelakinosho@moaadvisory.com

#Found this particular very interesting and doing the research on the formulas
#Maybe it is the accountant in me

def loan_repay_calc(p=0,r=0,t=1,cptint=1):
    print('principal: {}, rate: {}, term: {}, and compounding interval: {}'.format(p,r,t,cptint))

#Like having a function that simply captures the inputs and subsequently calls the
#function that will perform the calculations and produces the amortization schedule
#and reports
def input_num():
    principal = float(0) #Principal amount
    rate = float(0) #Annual rate, will be captured as a percent and not decimal e.g 5% and not 0.05
    term = float(0) #Term of the loan in years

    #Compounding interval; 1 for Daily, 2 for Weekly, 3 for Monthly and 4 for Continuously
    interval = int(0)
    internal_lst = [1,2,3,4]

    try:
        principal = float(input("Enter a positive principal amount\nFor example enter 400000: "))
        while principal < 0:
            print("\n")
            print("Please try again and enter a positive principal amount.")
            principal = float(input("Enter a positive principal amount\nFor example enter 400000: "))

        rate = float(input("Enter a positive annual interest rate\nFor 4.25% enter 4.25, and NOT 0.0425 and NOT 4.25%: "))
        while rate < 0:
            print("\n")
            print("Please try again and enter a positive annual interest rate.")
            rate = float(input("Enter a positive annual interest rate\nFor 4.25% enter 4.25, and NOT 0.0425 and NOT 4.25%: "))

        term = float(input("Enter a positive number of years\nFor example for 30 years enter 30 OR two and a half years enter 2.5: "))
        while term < 0:
            print("\n")
            print("Please try again and enter a positive number of years.")
            term = float(input("Enter a positive number of years\nFor example for 30 years enter 30 OR two and a half years enter 2.5: "))

        print('Selecting the number for the appropriate Compounding Interval\n')
        print('1  Daily')
        print('2  Weekly')
        print('3  Monthly')
        print('4  Continuously\n')

        interval = int(input("Enter a number for the compounding interval\nFor example for daily enter 1: "))
        while interval not in internal_lst:
            print("Please try again and enter a positive number.")
            interval = int(input("Enter a number for the compounding interval\nFor example for daily enter 1: "))

        loan_repay_calc(principal,rate,term,interval)

    except ValueError:
        print("Oops an incorrect value was entered!!")
        print("Values entered for Principal amount: {}, for Rate: {}, Term: {}, and Compounding Interval: {} .".format(principal,rate,term,interval))
        input_num()

    finally:
        print("Thank you!!")

input_num()
