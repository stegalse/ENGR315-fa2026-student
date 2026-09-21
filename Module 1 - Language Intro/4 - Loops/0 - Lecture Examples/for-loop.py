"""
Simple example of compounding interest with annual payments
"""

# initial bank deposit
balance = 1000

# interest rate (as a fraction) of 2.3%
rate = 0.023

# years to compound interest
years = 10

# annual contribution
contribution = 1000

# iterate over a sequence of numbers from [0,years)
for i in range(0,years):
    balance = balance*(1+rate) + contribution
    print('At end of year ', i+1, ' balance is ', balance)
    if balance > 5000:
        break #if the balance exceeds 5000, exit the loop


