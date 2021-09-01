#Python program to check whether a number is Prime or not
Number = int(input("Enter number: "))

def check_prime_number(Number):
    if Number>1:
        for i in range(2,Number):
            if Number%i == 0:
                print("Entered number is not prime number!")
        else:
            print("Entered number is prime number!")
    else:
        print("You Entered wrong number!")

check_prime_number(Number)