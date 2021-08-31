# Python Program for simple interest 
principle = int(input("Enter Principle : ")) # taking input form user for principle
rate = int(input("Enter Rate : ")) # taking input form user for rate
time = int(input("Enter Time : ")) # taking input form user for time

def simple_interest(principle, rate, time):
    si = 0
    si = (principle * rate * time) / 100
    return si

result = simple_interest(principle, rate, time)

print("Simple interest for principle = {0}, rate = {1} and time = {2} years is".format(principle, rate, time) , result)
    