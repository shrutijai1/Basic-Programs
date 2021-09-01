#Program to print ASCII Value of a character
'''
ord(): It converts the given string of length one, returns an integer representing
the Unicode code point of the character. For example, ord(‘a’) returns the integer 97.
'''
string = input("Enter string: ")

for char in range(len(string)):
    result = ord(string[char])
    print(string[char],"ASCII value is",result)