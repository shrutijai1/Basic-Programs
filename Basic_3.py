# Python Program for Factorial of a number!

# Factorial means multiplicaion of all the numbers from 1 till that number for example  6! = 1*2*3*4*5*6 =720
# 6! = 720
number = int(input("Enter Number : ")) # taking input form user

#1st way : use of for loop
def factorial(number):
    result = 1
    for x in range(1,number+1):
        result = result * x
    return result
final_result = factorial(number)
print("Final result is:", final_result)


#2nd way:  by using if else
def factorial_using_if(number):
    if number <0:
        print(" You Enter wrong number!")
    elif number == 1 or number == 0:
        return 1
    else:
        flag = 1
        while(number>1):
            flag = flag * number
            number = number - 1
        return flag
    
factorial_of_number = factorial_using_if(number)

print("Factorial of a number:", factorial_of_number)
