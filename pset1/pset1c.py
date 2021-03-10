annual_pay = int(input('Enter annual salary'))
x = annual_pay
semi_annaul_raise = 0.07
investment_return_rate = 0.04
downpayment = 0.25
house_cost = 1000000
portion_downpayment = downpayment * house_cost
epsilon = 100
current_savings = 0
count = 0
high = 10000
low = 0
guess_portion = (high + low)/2

while True:
    count += 1
    annual_pay = x
    current_savings = 0
    guess_portion = (high + low)/2
    
    for month in range(1, 37):
        current_savings = current_savings + (guess_portion/10000 * annual_pay/12) + ((0.04/12)*current_savings)
        if month % 6 == 0:
            annual_pay += annual_pay * semi_annaul_raise
    if abs(current_savings - portion_downpayment) <= epsilon:
        print("Recommended savings rate:", guess_portion/10000)
        print("Number of steps in bisection search:", count)
        break
    elif abs(current_savings - portion_downpayment) > epsilon and current_savings < portion_downpayment:
        low = guess_portion
    elif abs(current_savings - portion_downpayment) > epsilon and current_savings > portion_downpayment:
        high = guess_portion
    if abs(high - low) < 0.001:
        print("Not possible to pay the down payment in 3 years")
        break