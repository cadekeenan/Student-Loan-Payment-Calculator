loan_per_year = float(input('What is the loan per year? '))
interest_rate = float(input('What is the interest rate? '))
years = int(input('Number of years: '))

total_owed = 0
counter = 0

while counter < years:
    counter += 1
    total_owed = (total_owed + loan_per_year) * (1 + interest_rate)
    print(total_owed)
    
print("Total owed at Graduation")
print("$", total_owed)

monthly_payment = float(input('What is your monthly payment? '))
monthly_interest = (interest_rate / 12)

if monthly_payment > monthly_interest * total_owed:
    print('A monthly payment of',monthly_payment, 'dollars is possible.')
    print('The minimum monthly payment for this loan would be',monthly_interest * total_owed, 'dollars.')
    
else:
    print('A monthly payment of $',monthly_payment, 'is not possible.')
    print('The minimum monthly payment for this loan would be',monthly_interest * total_owed, 'dollars.')
    
    
month = 0
while total_owed > 0:
    month += 1
    total_owed = total_owed - monthly_payment
    total_owed = total_owed * (1 + monthly_interest)
    
print('It will take', month, 'months to pay off your student loans.')
print('It will take', month / 12, 'years to pay off student loans.’)
