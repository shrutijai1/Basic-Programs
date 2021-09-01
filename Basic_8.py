#Python program to print all Prime numbers in an Interval
# prime number are divisible by 1 or itself.
start = int(input("Enter the number from which you want to start printing prime numbers:"))
End = int(input("Enter the number till you want to print prime numbers:"))

def prime_number(start,End):
    for i in range(start,End+1):
        if i>0:
            for j in range(2,i):
                if i%j == 0:
                    break
            else:
                print(i)
            
prime_number(start,End)