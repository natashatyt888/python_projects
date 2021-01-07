string = input("Enter a string: ")
if string.lower() == string[::-1].lower():
    print(string + " is a palindrome!")
else:
    print(string + " is not a palindrome!")