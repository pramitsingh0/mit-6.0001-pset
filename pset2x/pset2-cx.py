balance = int(input('Enter the outstanding balance on the credit card: '))
reset = balance
annual_interest_rate = float(input("Enter the annual interest rate: "))
monthly_interest_rate = annual_interest_rate/12
# increment = 10
high = balance
low = 0
count = 0

while True:
    balance = reset
    # payment += 10
    payment = (high + low)/2
    for month in range(12):
        
        remaining_bal = balance - payment
        balance = remaining_bal*monthly_interest_rate + remaining_bal
        if balance <= 0:
            break
    if balance 
    
    if balance <= 0:
        break

print('Lowest payment: ', payment)
