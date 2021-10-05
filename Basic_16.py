# progra for check string is palindrom or not palindrom.
'''
def ispalindrom(s):
     return s == s[::-1]
s = 'madam'
 
palindrom = ispalindrom(s)
 
if palindrom:
    print("String is palindrom")
else:
    print("String is not palindrom")
    '''

orginial_string = input()
reverse_string = orginial_string [::-1]
count = 0

for x in range (len(orginial_string)):
    if orginial_string[x] == reverse_string[x]:
        count += 1

if count == len(orginial_string):
    print("String is Palindrom ")
else:
    print("String is not palindrom")