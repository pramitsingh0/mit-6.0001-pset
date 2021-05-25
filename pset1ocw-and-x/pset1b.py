#prompt the user for his annual_salary
annual_salary = float(input("Enter the annual salary: "))
#prompt the user for his portion_saved
portion_saved = float(input("Enter portion of salary to be saved: "))
#prompt the user for cost of the dream house. extract the down payment for it
total_cost = float(input("Enter the cost of your house: "))
#prompt the user for semi_annual_raise
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))
#after every multiple of 6 months annual salary raised by that much
#portion to be in downpayment in this case is protion_downpayment*total_cost
portion_downpayment = 0.25
current_savings = 0.0
count = 0
#saving are invested at return rate of 0.04 per annum.
#this needs to be done every month until current_savings <= downpayment
while current_savings <= (portion_downpayment*total_cost):
    current_savings = (current_savings) + (current_savings*(0.04/12)) + ((annual_salary/12)*portion_saved)
    count = count + 1
    if count % 6 == 0:
        annual_salary += annual_salary*semi_annual_raise


print("Number of months:", count)
