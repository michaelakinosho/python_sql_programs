#My signature and contact details
#Written by: Michael Akinosho
#Email: michaelakinosho@moaadvisory.com

#Found this particular very interesting and doing the research on the formulas
#Maybe it is the accountant in me

def loan_repay_calc(p=0,r=0,t=1,prd=1):


#Like having a function that simply captures the inputs and subsequently calls the
#function that will perform the calculations and produces the amortization schedule
#and reports
def input_num():
    principal = float(0) #Principal amount
    rate = float(0) #Annual rate, will be captured as a percent and not decimal e.g 5% and not 0.05
    term = float(0) #Term of the loan in years

    #Compounding interval; 1 for Daily, 2 for Weekly, 3 for Monthly and 4 for Continuously
    interval = int(0)

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
        while cost_per_tile < 0:
            print("\n")
            print("Please try again and enter a positive number of years.")
            term = float(input("Enter a positive number of years\nFor example for 30 years enter 30 OR two and a half years enter 2.5: "))

        print('Selecting the number for the appropriate Compounding Interval\n')
        print('1  Daily\n')
        print('2  Weekly\n')
        print('3  Daily\n')
        print('4  Daily\n')

        interval = int(input("Enter a positive number of years\nFor example for 30 years enter 30 OR two and a half years enter 2.5: "))
        while cost_per_tile < 0:
            print("\n")
            print("Please try again and enter a positive number of years.")
            term = float(input("Enter a positive number of years\nFor example for 30 years enter 30 OR two and a half years enter 2.5: "))

    except ValueError:
        print("Oops an incorrect value was entered!!")
        print("Values entered for width: {}, for length: {} and cost per tile: {}.".format(flr_width,flr_length,cost_per_tile))
        floor_tiling_cost()

    finally:
        print("Thank you!!")

floor_tiling_cost()
