#My signature and contact details
#Written by: Michael Akinosho
#Email: michaelakinosho@moaadvisory.com

#Found this particular program very interesting and doing the research on the formulas
#Maybe it is the accountant in me

from math import exp

def loan_repay_calc():
    loan_dict = input_num()
    #print(loan_dict)S
    print('Original loan amount: {}, annual rate: {}%, term in years: {}, compounding interval: {}, number of payments per year: {}'
    .format(loan_dict["principal"],loan_dict["rate"],loan_dict["term"],loan_dict["comp_int"],loan_dict["comp_freq_pay"]))
    tot_pay_back = float(0)
    p = loan_dict["principal"]
    r = loan_dict["rate"]/100
    t = loan_dict["term"]
    comp_int = loan_dict["comp_int"]
    prd = loan_dict["comp_freq_pay"]
    intv_int_rate = float(r)/float(12)
    
    #Number of payment periods
    num_of_pay = t * prd

    if comp_int in [1,2,3]:
        tot_pay_back = (p*intv_int_rate)/(1-(1+intv_int_rate)**(-t*prd))
        tot_pay_back = tot_pay_back * (t*prd)
    elif comp_int == 4:
        tot_pay_back = p * (exp(1)**(r*t))
    else:
        print('Compounding interval is not known')

    each_pay_amt = round(tot_pay_back/num_of_pay,2)
    #declaring and initializing loan amount balance

    pay_back_bal = p
    
    #declaring and initializing current period interest paid
    cur_prd_int = float(0)
    cur_prd_prin = float(0)

    print("Loan plus Interest\t\tNumber_of_Payments\t\tPayment_Amount\t\tLoan_Amount\t\tInterest_Amount")
    print("{:10,.2f}\t{:20.0f}\t{:20,.2f}\t{:20,.2f}\t{:10,.2f}".format(tot_pay_back,num_of_pay,each_pay_amt,p,tot_pay_back-p))

    print("Payment #\tPayment Amount\tInterest Paid\tPrincipal Paid\tLoan Balance")
    x = 1
    while pay_back_bal > 0:
        cur_prd_int = round(intv_int_rate * pay_back_bal,2)
        cur_prd_prin = round(each_pay_amt - cur_prd_int,2)
        if round(each_pay_amt,2) != round((cur_prd_int+cur_prd_prin),2):
            print("Stopped amortization schedule generation")
            print("Interval payment of:{} is not equal to sum of Interest paid: {} and Principal paid: {}"
            .format(each_pay_amt,cur_prd_int,cur_prd_prin))
            break
        if cur_prd_prin > pay_back_bal:
            cur_prd_prin = pay_back_bal
            each_pay_amt = cur_prd_int + cur_prd_prin
        pay_back_bal = round(pay_back_bal - cur_prd_prin,2)
        print(" {:5,.0f}{:15,.2f}\t\t{:10,.2f}\t\t{:10,.2f}\t\t{:10,.2f}"
        #print(" {}\t\t\t{:.2f}\t\t{:10.2f}\t\t{}\t\t{}"
        .format(x,each_pay_amt,cur_prd_int,cur_prd_prin,pay_back_bal))
        x += 1
        if x > 10 and x%10 == 1:
            print("Payment #\tPayment Amount\tInterest Paid\tPrincipal Paid\tLoan Balance")

#Like having a function that simply captures the inputs and subsequently calls the
#function that will perform the calculations and produces the amortization schedule
#and reports
def input_num():
    principal = float(0) #Principal amount
    rate = float(0) #Annual rate, will be captured as a percent and not decimal e.g 5% and not 0.05
    term = float(0) #Term of the loan in years

    #Compounding interval; 1 for Daily, 2 for Weekly, 3 for Monthly and 4 for Continuously
    interval = int(0)
    interval_tuple = ("Daily","Weekly","Monthly","Continuously")

    pay_freq = int(0)

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

        print('Selecting the number for the appropriate Compounding Interval')

        for x in interval_tuple:
            print('{} {}'.format(interval_tuple.index(x)+1, x))

        #print('1  Daily')
        #print('2  Weekly')
        #print('3  Monthly')
        #print('4  Continuously\n')

        interval = int(input("Enter a number for the compounding interval based on the list provided\nFor example for Continuously enter 4: "))
        while interval<1 or interval>4:
            print("Please try again and enter a positive number.")
            interval = int(input("Enter a number for the compounding interval based on the list provided\nFor example for Continuously enter 4: "))
        if interval == 1:
            pay_freq = 360
        elif interval == 2:
            pay_freq = 52
        elif interval == 3:
            pay_freq = 12
        #Adding the ability to change the number of payments per years for the continously compounding option
        #May add an input here later
        elif interval == 4:
            pay_freq = 12

        input_dict = {"principal":principal,"rate":rate,"term":term,"comp_int":interval,"comp_freq_pay":pay_freq}
        return input_dict

    except ValueError:
        print("Oops an incorrect value was entered!!")
        print("Values entered for Principal amount: {}, for Rate: {}, Term: {}, Compounding Interval: {}, and Number of Payments per Year: {} ."
        .format(principal,rate,term,interval,pay_freq))
        input_num()

    finally:
        print("Thank you, we have all the inputs we need to continue!!")

loan_repay_calc()
