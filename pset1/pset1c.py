annual_salary = float(input("Enter the annual salary: "))
portion_saved = float(input("Enter portion of salary to be saved: "))
total_cost = float(input("Enter the cost of your house: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))
portion_downpayment = 0.25
current_savings = 0.0
high = 
low = 
guess = (high + low)/2

count = 0
while current_savings <= (portion_downpayment*total_cost):
    current_savings = (current_savings) + (current_savings*(0.04/12)) + ((annual_salary/12)*portion_saved)
    count = count + 1
    if count % 6 == 0:
        annual_salary += annual_salary*semi_annual_raise

print("Number of months:", count)