balance = int(input('Enter the outstanding balance on the credit card: '))
reset = balance
annual_interest_rate = float(input("Enter the annual interest rate: "))
monthly_interest_rate = annual_interest_rate/12
# increment = 10
payment = 0
while True:
    balance = reset
    payment += 10
    for i in range(12):
        remaining_bal = balance - payment
        balance = remaining_bal*monthly_interest_rate + remaining_bal
        if balance <= 0:
            break
    if balance <= 0:
        break

print('Lowest payment: ', payment)
