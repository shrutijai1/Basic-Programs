# Python Program for Compound interest 
principle = int(input("Enter Principle : ")) # taking input form user for principle
rate = int(input("Enter Rate : ")) # taking input form user for rate
time = int(input("Enter Time : ")) # taking input form user for time
amount = int(input("Enter Amount : ")) # taking input form user for amount

def compound_interest(principle, rate, time, amount):
    ci = 0
    amount = principle*( pow((1 + rate/100),time) )
    ci = amount - principle
    return ci

result = compound_interest(principle, rate, time,amount)

print(" Compound Interest for principle = {0}, rate = {1}, time = {2} years and amount = {3} is".format(principle, rate, time,amount) , result)
    