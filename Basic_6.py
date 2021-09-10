# Python Program to check Armstrong Number
# Armstrong Number is like 153 = 1*1*1 + 5*5*5 + 3*3*3 = 1+125+27 = 153
# number = first_digit*order + second_digit*order + third_digit*order + fourth_digit*order.......

number = int(input("Enter a number: "))
order = len(str(number))
copy_number = number
sum = 0

while(number>0):
    digit = number%10
    sum += digit **order 
    number = number//10
    
if sum == copy_number:
    print(copy_number,"number is Armstrong number")
else:
    print(copy_number,"number is not a Armstrong number")
    