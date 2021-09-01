#Python Program for Sum of Cube of first n natural numbers
number = int(input("Enter the number:"))
result = 0
for i in range(1,number+1):
    result = result + i*i*i
    
print("Sum of cube of first n natural numbers is:",result)
    