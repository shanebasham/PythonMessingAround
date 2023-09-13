print('Please fill out each of these questions from $1000 - $100000:')
print()
loan_size = int(input('How large is the loan? '))
credit = int(input('How good is your credit history from 1-10? '))
income = int(input('How high is your income? '))
down_payment = int(input('How large is your down payment? '))

should_loan = False

if loan_size >= 50000:
    if credit >= 7 and income >= 70000:
        should_loan = True
    elif credit >= 7 or income >= 70000:
        if down_payment >= 50000:
            should_loan = True
        else:
            should_loan = False
    else:
        should_loan = False
else:
    if credit < 4:
        should_loan = False
    else:
        if income >= 70000 or down_payment >= 70000:
            should_loan = True
        elif income >= 40000 and down_payment >= 40000:
            should_loan = True
        else:
            should_loan = False

if should_loan:
    print('\nThe decision is yes.')
else:
    print('\nThe decision is no.')
