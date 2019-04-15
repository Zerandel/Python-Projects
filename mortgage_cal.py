#!/usr/bin/env python3

### MORTGAGE CALCULATOR ###

# The program calculates the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate. Also figure out how long it will take the user to pay back the loan.

# Firstly, we define "months" , "interest rate" and "loan".

months = int(input("Please enter mortgage term as month: "))

interest_rate = float(input("Please enter interest rate: "))

loan = float(input("Please enter loan value: "))

# Now, we create the program that calculates the monthly payment of a fixed term mortgage.

monthly_interest_rate = interest_rate / 100 / 12

payment = (monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-months))) * loan

print("Monthly payment for a $%.2f %s month mortgage at %.2f interest rate is: $%.2f" % (loan, months, interest_rate, payment))
