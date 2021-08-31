# Write a program for finding a maximum of two numbers.
number1 = int(input("Enter first number: ")) # taking input form user for first number1
number2 = int(input("Enter Second number: ")) # taking input form user for second number2

# 1st way using  if else statement in function defination 
def maximum(number1, number2): # defination of function 
    if number1 > number2:
        print(" {0} is greater than {1}".format(number1, number2))
    else:
        print(" {1} is greater than {0}".format(number1, number2))

maximum(number1, number2)  #calling of function

# 2nd way --> directly we can call max function for finding greater number among two numbers which is given below 
print(" Maximum number is:", max(number1, number2)) 

#3rd way --> we can also use tertiary operator means if else in one line 
print( " Maximum number is:", number1 if number1>number2 else number2)